import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

(b, g, r) = image[cY, cX]

print("Pixel ({}, {}). Blue: {} Green: {} Red: {}".format(cX, cY, b, g, r))