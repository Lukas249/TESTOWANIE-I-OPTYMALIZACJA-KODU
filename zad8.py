import cv2
import imutils

image = cv2.imread("zdj.jpg")

cv2.imshow("Przed", image)

(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)

rotated30_1 = cv2.warpAffine(image, M, (w, h))

M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)

rotated30_2 = cv2.warpAffine(rotated30_1, M, (w, h))

M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)

rotated30_3 = cv2.warpAffine(rotated30_2, M, (w, h))

cv2.imshow("Po (3*30)", rotated30_3)

(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)

rotated90 = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Po (90)", rotated90)

cv2.waitKey(0)