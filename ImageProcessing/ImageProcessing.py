import sys
import os
sys.path.insert(1,os.path.join('..','..','ECS171-Team4','BoxExtraction'))
import box_extraction as be

sys.path.insert(1,os.path.join('..','..','ECS171-Team4','PageRecognition'))
import PageRecognition as pr



import cv2
image_name = 'test.png'
img = cv2.imread(image_name)
warped = pr.pageRecognition(img)
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img', warped)

# cv2.waitKey(0)
# cv2.waitKey(0)


# image_name = 'scanned_image.png'
# img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
boxes = be.get_boxes(warped)
cv2.imshow("img", boxes[0])