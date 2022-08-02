# import the necessary packages
from cv2 import CV_32FC1
import numpy as np
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

area = 0
cords = 0

for i in range(len(contours)):
    cnt = contours[i]
    x,y,w,h = cv2.boundingRect(cnt)
    this_area = w*h
    if this_area>area:
        area=this_area
        cords = x,y,w,h

height,width,channels = image.shape

contoured = cv2.rectangle(image,(max(int(cords[0]*0.9),0),max(int(cords[1]*0.9),0)),(min(int((cords[0]+cords[2])*1.1),width),min(int((cords[1]+cords[3])*1.1),height)),(0,255,0),2)
cv2.imshow("sialala",contoured)
cv2.waitKey(0)
