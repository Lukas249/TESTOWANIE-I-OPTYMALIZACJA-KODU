import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

(cX, cY) = (w // 3, h // 3)

centerFragment = image[cY:cY*2, cX:cX*2]

cv2.imshow("Fragment", centerFragment)

cv2.waitKey(0)