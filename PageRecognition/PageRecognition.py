import cv2

def resize(img, height=800):
    """ Resize image to given height """
    rat = height / img.shape[0]
    return rat, cv2.resize(img, (int(rat * img.shape[1]), height))

def findCorners(img):
    # return coordinates of document's 4 corners
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img_blur = cv2.blur(img, (3,3))
    img = cv2.bilateralFilter(resize(img), 9, 75, 75)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 4)
    img = cv2.medianBlur(img, 11)
    edges = cv2.Canny(img, 200, 250)

    cv2.imshow('img', img)
    cv2.imshow('edge', edges)
    cv2.waitKey(0)
    return

def transformPerspective(img):
    # return top-down view of image
    pass

def main():
    img = cv2.imread('./PageSample2.JPG')
    findCorners(img)

if __name__ == "__main__":
    main()
