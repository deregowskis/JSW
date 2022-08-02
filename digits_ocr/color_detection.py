# import the necessary packages
import numpy as np
import argparse
import cv2
from PIL import Image, ImageEnhance

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
ap.add_argument("-o", "--output", help = "path to the output")
args = vars(ap.parse_args())

# load the image and apply contrast and saturation filtres
org = cv2.imread(args["image"])
pil_image = Image.fromarray(org)
contrast_filter = ImageEnhance.Contrast(pil_image)
pil_image = contrast_filter.enhance(1.6)
saturation_filter = ImageEnhance.Color(pil_image)
pil_image = saturation_filter.enhance(1.5)
image = np.asarray(pil_image)

# define GBR boundaries:
lower = np.array([0,0,170],dtype="uint8")
upper = np.array([170,170,255],dtype="uint8")

# provide mask and convert to gray scale
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)

# find the area with the biggest amount of red pixels:
height,width,channels = output.shape
count = height*width
ymin = 0
ymax = 0
xmin = 0
xmax = 0


for i in range(int(2*width/3-1)):
	for j in range(int(height/2-1)):
		moving_frame = gray[j:int(height/2+j),i:int(width/3+i)]
		black_pixels_count = np.sum(moving_frame == 0)
		if count > black_pixels_count:
			ymin = j
			ymax = int(height/2+j)
			xmin = i
			xmax = int(width/3+i)
			count = black_pixels_count

#save output
cropped_number = Image.fromarray(cv2.imread(args["image"])).crop((xmin,ymin,xmax,ymax))
cropped_number_arr = np.asarray(cropped_number)
crop_height, crop_width, crop_channels = cropped_number_arr.shape
crop_count = crop_height*crop_width

angle = ""

for i in range(xmin,xmax-150):
	for j in range(ymin,ymax-50):
		moving_frame = gray[ymin+j:max(ymin+j+50,ymax),xmin+i:max(xmin+i+150,xmax)]
		black_pixels_count = np.sum(moving_frame == 0)
		if crop_count > black_pixels_count:
			angle = "poziomo"
			crop_count = black_pixels_count

for i in range(xmin,xmax-50):
	for j in range(ymin,ymax-150):
		moving_frame = gray[ymin+j:max(ymin+j+150,ymax),xmin+i:max(xmin+i+50,xmax)]
		black_pixels_count = np.sum(moving_frame == 0)
		if crop_count > black_pixels_count:
			angle = "pionowo"
			crop_count = black_pixels_count


#cropped_number.save(args["output"])
print(angle)
#optional visualization

contour = cv2.rectangle(org,(xmin,ymin),(xmax,ymax),(0,255,0),2)
frame_output = Image.fromarray(org)
#frame_output.save(args["output"])
cv2.imshow("sialala",np.asarray(org))
cv2.waitKey(0)