import cv2

def findCorners(img):
    # return coordinates of document's 4 corners
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(img, 100, 200)

def transformPerspective(img):
    # return top-down view of image
    pass

def main():
    img = imread('./PageSample.JPG')
    findCorners(img)
