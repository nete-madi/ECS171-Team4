import cv2
import numpy as np

def resize(img, height=800):
    """ Resize image to given height """
    rat = height / img.shape[0]
    return rat, cv2.resize(img, (int(rat * img.shape[1]), height))

def findCorners(img, sigma):
    """ return ndarray with contains the coordinates of document's 4 corners """
    # Resize the image for easier detection
    rat, resized_img = resize(img)
    # Grayscale the image
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    # BilateralFilter the image
    fltrd_img = cv2.bilateralFilter(gray_img, 5, 20, 20)

    # Find the edges of the the filtered image
    fltrd_edged_img = autoCanny(fltrd_img, sigma)

    # Get the different contours of the image
    contours,_ = cv2.findContours(fltrd_edged_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    max_cnt = contours[0]
    max_area = cv2.contourArea(max_cnt)

    for cnt in contours:
        curr_area = cv2.contourArea(cnt)
        if curr_area > max_area:
            max_area = curr_area
            max_cnt = cnt

    # Approximate the polygon for the biggest contour
    epsilon = 0.1*cv2.arcLength(max_cnt,True)
    corners = cv2.approxPolyDP(max_cnt,epsilon,True)
    # Use the ratio saved from downsizing the image to upsize the polygon to the original images size
    scaled_corners = np.int0(corners/rat)

    return scaled_corners


def autoCanny(resized_img, sigma):
    """Simple method for canny edge detection without the need for setting thesholds"""
    # Auto canny courtesy of:
    # https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
    # compute the median of the single channel pixel intensities
    v = np.median(resized_img)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged_img = cv2.Canny(resized_img, lower, upper)
    return edged_img


def transformPerspective(img):
    # return top-down view of image
    pass

def main():
    img = cv2.imread('./LaptopSample.jpeg')
    corners = findCorners(img, .5)

    # Draw the polygon on the original image
    cv2.drawContours(img, [corners], -1, (0,255,0), 3)
    cv2.imshow("img", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
