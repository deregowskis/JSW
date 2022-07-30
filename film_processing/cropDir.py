import os
from PIL import Image
export_file_path = ''
image_input_folder_path = '/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v2/'
image_cropped_output_folder_path = '/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v2_cropped/'

# get the path/directory
for images in os.listdir(image_input_folder_path):
    # check if the image ends with png
    if images.endswith(".png"):
        left = 0.3
        right = 0.8
        top = 0.4
        bottom = 0.8
        img_path = image_input_folder_path + images
        im = Image.open(img_path)
        width, height = im.size

        left = width * float(left)
        right = width * float(right)
        top = height * float(top)
        bottom = height * float(bottom)

        print(width, height, left, right, top, bottom)
        cropped_im = im.crop((left, top, right, bottom))
        # (replace the path below with a path to folder where all cropped images will be stored)
        # new_path = path.strip('/')
        cropped_im.save(f"{image_cropped_output_folder_path}{images}")