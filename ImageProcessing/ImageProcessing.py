import cv2
# import numpy as np

import sys
import os
sys.path.insert(1,os.path.join('..','..','ECS171-Team4','BoxExtraction'))
import box_extraction as be

sys.path.insert(1,os.path.join('..','..','ECS171-Team4','PageRecognition'))
import PageRecognition as pr

def main():
    image_name = 'test.png'
    boxes = process_image(image_name)
    # cv2.imshow('boxes', np.concatenate(boxes))
    # cv2.waitKey(0)

def process_image(image_path):
    img = cv2.imread(image_path)
    page = pr.pageRecognition(img)
    page = cv2.cvtColor(page, cv2.COLOR_BGR2GRAY)

    boxes = be.get_boxes(page)
    boxes = [cv2.resize(box, (28,28)) for box in boxes]
    boxes = [box.reshape((28,28,1)) for box in boxes]

    return boxes

if __name__ == "__main__":
    main()