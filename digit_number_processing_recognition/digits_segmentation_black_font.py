import numpy as np
import cv2

# org_img = "/Users/bilibala/Desktop/work/dataset/digits/red_compressed_number_2.png"
org_img = "/Users/bilibala/Desktop/work/dataset/digits/test_img.png"

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
    grayscaleimg = cv2.resize(img, (100, 50), interpolation=cv2.INTER_CUBIC)
    grayscaleimg = cv2.cvtColor(grayscaleimg, cv2.COLOR_BGR2GRAY)  # 生成灰度图

    # ####
    row_nz = []
    # 将每行展成一个list,即有50个list
    for row in grayscaleimg.tolist():
        # print(f"len(row): {len(row)}")
        # print(f"row.count(0): {row.count(0)}")
        row_nz.append(len(row) - row.count(0))
    # row_nz里存储每行值和不为0的列数 eg.[0, 0, 0, 0, 0, 0, 7, 15, 16, 9, 10, 9, 9, 11, 14, 25, 32, 24, 20, 13, 7, 7,
    # 7, 9, 10, 10, 9, 9, 9, 14, 19, 14, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 50
    # 代表在第6行(0开始)有7列元素不为0

    # 找到上界(即第一个开始出现笔画的行号) 记为第upper_y列
    upper_y = 0
    for i, x in enumerate(row_nz):
        # if x >= 1:  # 若一行中出现大于两个地方有笔画(255)
        if x < 100:
            upper_y = i
            break

    # 找到下界(即最后一个出现笔画的行号) 记为第lower_y列
    lower_y = 0
    for i, x in enumerate(row_nz[::-1]):
        # if x >= 1:
        if x < 100:
            lower_y = len(row_nz) - i
            break
    print(lower_y)
    print(upper_y)
    # 按上下界进行切割，将没有笔画的上部分和下部分都丢弃，留下中间带有笔画的区域
    sliced_y_img = grayscaleimg[upper_y: lower_y, :]

    # 同理，按列切割，此时grayscaleimg为 (lower_y - upper_y)x100 矩阵
    col_nz = []
    # 将每行展成一个list,即有100个list
    for col in sliced_y_img.T.tolist():
        col_nz.append(len(col) - col.count(0))

    p = len(sliced_y_img)
    # 寻找每个字符的左边界和右边界,column_boundary_list存储每个字符的起始列号
    column_boundary_list = []
    # record = False
    for i, x in enumerate(col_nz[:-1]):
        # 如果第i列无笔画(和为0)，第i+1列有笔画，可以认为i列是某个字符的左边界
        # if col_nz[i] <= 1 and col_nz[i + 1] > 1:
        if col_nz[i] >= len(sliced_y_img) and col_nz[i + 1] < len(sliced_y_img):
            column_boundary_list.append(i)
        # 如果第i列有笔画，第i+1列无笔画，可以认为i列是某个字符的右边界
        # elif col_nz[i] >= 1 and col_nz[i + 1] < 1:
        elif col_nz[i] < len(sliced_y_img) and col_nz[i + 1] >= len(sliced_y_img):
            column_boundary_list.append(i + 1)
    # 此时若书写32, column_boundary_list里存储的类似于[20, 31, 56, 89]，即20-31列代表'3', 56-89列代表'2'

    # 存储分割后的图片
    img_list = []  # img_list存储每幅图的矩阵
    xl = [column_boundary_list[i:i + 2] for i in range(0, len(column_boundary_list), 2)]
    for x in xl:
        s = len(x)
        if len(x) == 2 and x[1] - x[0] > 5:
            s = fill(sliced_y_img[:, x[0]:x[1]])  # 从sliced_y_img截取每幅图的列,进行背景填充
            img_list.append(s)                    # 将填充后的矩阵存入img_list


    img_list = [x for x in img_list if x.shape[1] > 5]

    for i in range(len(img_list)):
        img = img_list[i]
        cv2.imwrite(f"test_segmented_black{i}.jpg", img)

    print("数字位数为: ", len(img_list))  # 输出总的字符数，即图片数

tmp()