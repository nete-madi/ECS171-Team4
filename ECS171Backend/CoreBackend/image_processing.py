import cv2
import numpy as np

from CoreBackend import box_extraction as be
from CoreBackend import page_recognition as pr

def main():
    pass

def process_image(image_path):
	img = cv2.imread(image_path)
	# page = pr.pageRecognition(img)
	# cv2.imshow('img', img)
	# cv2.waitKey(0)
	page = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	boxes = be.get_boxes(page)
	boxes = [cv2.bitwise_not(box) for box in boxes]
	boxes = [cv2.threshold(box, 127, 255, cv2.THRESH_BINARY)[1] for box in boxes]

	# Zoom into digit/letter
	# boxes = [cv2.GaussianBlur(box, (5,5),0) for box in boxes]
	boxes = [crop_img(box) for box in boxes]
	boxes = [cv2.resize(box, (28,28)) for box in boxes]
	boxes = [np.reshape(box, (28,28,1)) for box in boxes]
	return boxes

def crop_img(img):
    coords = cv2.findNonZero(img)  # Find all non-zero points (text)
    if coords is None: return np.zeros((28,28))
    x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box

    if w > h:
        out = np.zeros((w,w))
        out[int(w / 2 - h / 2):int(w / 2 + h / 2), :] = img[y:y + h, x:x + w]
        return out
    else:
        out = np.zeros((h,h))
        out[:, int(h / 2 - w / 2):int(h / 2 + w / 2)] = img[y:y + h, x:x + w]
        return out


if __name__ == "__main__":
    main()
