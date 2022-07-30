from PIL import Image
path = "/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1/3.png"
#{'frameID': 3, 'frameStamp': 32.0, 'estTime': 1.92, 'image_name': '/Users/bilibala/Desktop/work/dataset/wozy_film_dataset/frame_output/v1/3.png'}

# left = 0.4815884530544281
# top = 0.7256478071212769
# right = 0.562042236328125
# bottom = 0.8418394923210144

left = 0.3
right = 0.8
top = 0.4
bottom = 0.8

im = Image.open(path)
width, height = im.size

left = width * float(left)
right = width * float(right)
top = height * float(top)
bottom = height * float(bottom)

print(width, height, left, right, top, bottom)
cropped_im = im.crop((left, top, right, bottom))
# (replace the path below with a path to folder where all cropped images will be stored)
# new_path = path.strip('/')
cropped_im.save('3_b.png')