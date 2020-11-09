import cv2
import numpy as np
import matplotlib.pyplot as plt
import shutil
import os

def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)   

def sort_boxes(boxes, image_height):
    return sorted(boxes, key=lambda box: box[0][0] + box[0][1] * image_height)

def save_boxes(boxes, original):

    png_path = 'all_pngs/'
    contours_path = 'contours/'
    create_directory(png_path)
    create_directory(contours_path)
    
    image_number = 1
    for square, approx in boxes:
        x = square[0]
        y = square[1]
        w = square[2]
        h = square[3]

        # save actual square
        square_box = original[y:y+h, x:x+w]
        cv2.imwrite(png_path + 'square_box_{}.png'.format(image_number), square_box)
        
        # save contour for reference
        img_copy = original.copy()
        cv2.drawContours(img_copy, [approx], contourIdx = 0, color = (0), thickness =5)
        cv2.imwrite(contours_path +'contours_{}.png'.format(image_number), img_copy)
        image_number += 1

def get_boxes(image_name):
    # 1. conversion to gray scale
    # 2. binarization of the image. Using thresholding 

    # read image and apply grayscale
    img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    # create a copy to extract fields from it later
    original = img.copy()
    # thresholding - simplest method of segmenting images (process of partitionning a digital image into multiple segments, goal is to simplify image into a representation that is easier to analyze)
    # takes in grescale image. Used to create a binary image, returns threshold image
    _, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # mode cv2.RETR_TREE: way to find contours 
    # method cv2.CHAIN_APPROX_SIMPLE: approximation method for the detection. contour line indicates a line representing a boundary of the same intensities
    # returned contours is a list of points consisting of the contour lines
    contours, _ = cv2.findContours(image=threshold, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


    min_box_area = 750
    max_box_area = 1000
    image_number = 1
    rejects_number = 1
    accepted_boxes = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # reducing the number of points in a curve with a reduced set of points
        # curve = series of short line segments
        # approximated curve = subset of points in original curve
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        img_copy = original.copy()
        # draw an approximate rectangle around the contour
        x,y,w,h = cv2.boundingRect(cnt)
        if len(approx) == 4 and area > min_box_area and area < max_box_area:
            accepted_boxes.append([[x,y,w,h], approx])
    
    accepted_boxes = sort_boxes(accepted_boxes, original.shape[1])
    save_boxes(accepted_boxes, original)

image_name = 'patient-info-form-page-003.jpg'
get_boxes(image_name)
