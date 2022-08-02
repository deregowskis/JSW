import numpy as np
import cv2
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])
ret,thresh = cv2.threshold(image,3,255,cv2.THRESH_BINARY)
cv2.imwrite('/Users/output_red.png',thresh)