import cv2
import imutils

image = cv2.imread("zdj.jpg")

cv2.imshow("Przed", image)

rotated1 = imutils.rotate(image, 60)

cv2.imshow("Po (imutils)", rotated1)

(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)

rotated2 = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Po (warpAffine)", rotated2)

cv2.waitKey(0)