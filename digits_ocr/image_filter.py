import cv2
import os
from PIL import Image, ImageEnhance

# path_0 = "/home/bilibala/Desktop/work/dataset/digit_numbers_classification/cropped_numbers/"
path_0 = "/home/bilibala/Desktop/work/wozy_number_recognition/output/"
# path_0_filtered = "/home/bilibala/Desktop/work/dataset/digit_numbers_classification/cropped_numbers_fil/"
path_0_filtered = "/home/bilibala/Desktop/work/wozy_number_recognition/output/"
str_directory = path_0
b_directory = os.fsencode(path_0)
str_output_directory = path_0_filtered
for file in os.listdir(b_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".png"):
        img = cv2.imread(os.path.join(str_directory, filename))
        output_filename = filename.split(".", 1)[0]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh_output = cv2.threshold(gray, 160, 255, cv2.THRESH_TOZERO)
        # cutted_image = thresh_output
        cutted_image = cv2.resize(thresh_output, (28, 28), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(f"{str_output_directory}{output_filename}_f1.png", cutted_image)
        continue
    else:
        print("Hi stranger")
        continue

