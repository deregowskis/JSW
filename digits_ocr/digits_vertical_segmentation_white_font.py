import numpy as np
import cv2
from PIL import Image, ImageFilter
import tensorflow as tf
from OCR_predict import recognize

# 0-255
# black-white
font_threshold = 220

# org_img = "/Desktop/work/digits/Test_gray_org.jpg"
org_img = "/home/bilibala/Desktop/work/dataset/digit_numbers_classification_filtered/cropped_numbers_fil/0_9_RQ0sd_f1.png"
# org_img = "/Desktop/work/wozy_number_recognition/output/0_9_2.png"
# 进行外围的背景填充，防止reshape使数字拉伸变形
def fill(x):
    s1, s2 = x.shape[0], x.shape[1]
    size = max(s1, s2)                             # 找到宽或长里最大的值作为基准
    s = np.zeros((size+8, size+8), dtype='uint8')  # 填充大小设置为4
    s[4:s1+4, 4:s2+4] = x

    return s

def grayImage(img):
    im_gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    thresh = 127
    im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(img, im_bw)
    return im_bw
def tmp():
    # 按行切割,此时grayscaleimg为 50x100 矩阵，50 行，100列，每个元素不是0就是255
    # grayscaleimg = cv2.resize(org_img, (100, 50), interpolation=cv2.INTER_CUBIC)
    # grayscaleimg = cv2.cvtColor(grayscaleimg, cv2.COLOR_BGR2GRAY)  # 生成灰度图
    # grayscaleimg = grayImage(org_img)
    # ###
    # grayscaleimg = cv2.imread(org_img)
    img = cv2.imread(org_img)
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    grayscaleimg = img
    # grayscaleimg = cv2.resize(img, (100, 50), interpolation=cv2.INTER_CUBIC)
    grayscaleimg = cv2.cvtColor(grayscaleimg, cv2.COLOR_BGR2GRAY)  # 生成灰度图

    # ####
    col_nz = []
    # 将每行展成一个list,即有50个list
    for col in grayscaleimg.T.tolist():
        # count number greater than font_threshold
        count = len([1 for i in col if i > font_threshold])
        col_nz.append(len(col) - count)
    # row_nz里存储每行值和不为0的列数 eg.[0, 0, 0, 0, 0, 0, 7, 15, 16, 9, 10, 9, 9, 11, 14, 25, 32, 24, 20, 13, 7, 7,
    # 7, 9, 10, 10, 9, 9, 9, 14, 19, 14, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 50
    # 代表在第6行(0开始)有7列元素不为0

    # left and right bounder
    upper_y = 0
    for i, x in enumerate(col_nz):
        # if x >= 1:  # 若一行中出现大于两个地方有笔画(255)
        if x < len(grayscaleimg)-10:
            upper_y = i
            break

    # left and right bounder
    lower_y = 0
    for i, x in enumerate(col_nz[::-1]):
        # if x >= 1:
        if x < len(grayscaleimg)-10:
            lower_y = len(col_nz) - i
            break
    # print(lower_y)
    # print(upper_y)
    # 按上下界进行切割，将没有笔画的上部分和下部分都丢弃，留下中间带有笔画的区域
    # sliced_y_img is the image after left and right cropping
    sliced_y_img = grayscaleimg[:, upper_y: lower_y]

    # 同理，按列切割，此时grayscaleimg为 (lower_y - upper_y)x100 矩阵
    # row_nz is the list of plotted and non-plotted area (len(row) - count) in each row
    # count is the amount of plotted area
    row_nz = []
    # 将每行展成一个list,即有100个list
    for row in sliced_y_img.tolist():
        count = len([1 for i in row if i > font_threshold])
        row_nz.append(len(row) - count)

    p = len(sliced_y_img)
    # find the upper and lower boundary between digits ,column_boundary_list stores the initial location of digits
    row_boundary_list = []
    # record = False
    t = len(sliced_y_img[0])

    # threshold_row_segmentation:
    # if threshold_row_segmentation equals the length of first row of the image,
    # it means, in the first row, nothing was ploted
    threshold_row_segmentation = len(sliced_y_img[0])
    # the case when the digit starts from the very beginning of an image
    if row_nz[0] < threshold_row_segmentation:
        row_boundary_list.append(0)
    # we do not consider the last line, because it needs to be treated as a closed ending
    for i, x in enumerate(row_nz[:-1]):
        # 如果第i(row)无笔画(和为0)，第i+1(row)有笔画，可以认为i(row)是某个字符的Up边界
        # if col_nz[i] <= 1 and col_nz[i + 1] > 1:
        if row_nz[i] >= threshold_row_segmentation and row_nz[i + 1] < threshold_row_segmentation:
            row_boundary_list.append(i)
        # 如果第i(row)有笔画，第i+1(row)无笔画，可以认为i(row)是某个字符的Bottom边界
        # elif col_nz[i] >= 1 and col_nz[i + 1] < 1:
        elif row_nz[i] < threshold_row_segmentation and row_nz[i + 1] >= threshold_row_segmentation:
            row_boundary_list.append(i + 1)
    # 此时若书写32, column_boundary_list里存储的类似于[20, 31, 56, 89]，即20-31列代表'3', 56-89列代表'2'

    # 存储分割后的图片
    threshold_character_gap = 5
    img_list = []  # img_list存储每幅图的矩阵
    xl = [row_boundary_list[i:i + 2] for i in range(0, len(row_boundary_list), 2)]
    # tmp = []
    # x1 = []
    # x0 = []
    # x1 = [21,96,135,177]
    # x0 = [12, 52, 99, 135]
    # for i in range(4):
        # s = len(x)
        # if len(x) == 2 and x[1] - x[0] >= threshold_character_gap:
        #     tmp.append(x[1] - x[0])
        #     x1.append(x[1])
        #     x0.append(x[0])
            # s = fill(sliced_y_img[x[0]:x[1],:])  # 从sliced_y_img截取每幅图的列,进行背景填充
            # img_list.append(s)                    # 将填充后的矩阵存入img_list
            # img_list.append(sliced_y_img[x[0]:x[1], :])
            # img_list.append(sliced_y_img[x0[i]:x1[i], :])
    for x in xl:
        s = len(x)
        if len(x) == 2 and x[1] - x[0] >= threshold_character_gap:
            # s = fill(sliced_y_img[x[0]:x[1],:])  # 从sliced_y_img截取每幅图的列,进行背景填充
            # img_list.append(s)                    # 将填充后的矩阵存入img_list
            img_list.append(sliced_y_img[x[0]:x[1], :])
    # ---------------Simple filter--------------------------
    img_list = [x for x in img_list if x.shape[1] > 5]

    # tmp_digit_list = []
    # new_xl = []
    # for x in xl:
    #     tmp_digit_list.append(x[1] - x[0])
    # for value in tmp_digit_list:

    for i in range(len(img_list)):
        img = img_list[i]
        cv2.imwrite(f"output_tmp/0_9_{i}.png", img)
    print("Total digits: ", len(img_list))

    # # 存图和识别
    # tr = []  # tr存储每个字符的预测值
    #
    # # 循环每幅图的矩阵
    # for i, img in enumerate(img_list):
    #     # path = r".\result\%s.jpg" % i                               # 每幅图的存储地址，默认存储至\result下
    #     path = f"/home/bilibala/Desktop/work/wozy_number_recognition/0_9_{i}.jpg"
    #     mg = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 转为cv格式
    #     mg1 = mg.filter(ImageFilter.SMOOTH_MORE)                    # 添加平滑，模糊锯齿点
    #     mg1.save(path)                                              # 存储图像至result
    #     a = recognize(mg1)                                          # 调用recongnize函数识别单个字符，返回对应的预测值
    #     tr.append(a)
    #
    # print(tr)
tmp()