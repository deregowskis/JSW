import cv2
import numpy as np
org_img = "/Users/bilibala/Desktop/work/dataset/digits/red_compressed_number_2.png"

# img = cv2.imread(org_img)
# img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
# grayscaleimg = cv2.resize(img, (100, 50), interpolation=cv2.INTER_CUBIC)
# grayscaleimg = cv2.cvtColor(grayscaleimg, cv2.COLOR_BGR2GRAY)  # 生成灰度图

img = cv2.imread(org_img)
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
grayscaleimg = img
grayscaleimg = cv2.cvtColor(grayscaleimg, cv2.COLOR_BGR2GRAY)  # 生成灰度图


if grayscaleimg is None:
    print("Could not read the image.")

cv2.imwrite("Test_gray_org.jpg", grayscaleimg)
cv2.imshow("Display window", grayscaleimg)
k = cv2.waitKey(0)
# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread(org_img, cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)