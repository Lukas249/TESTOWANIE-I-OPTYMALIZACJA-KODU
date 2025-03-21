import cv2

image = cv2.imread("zdj.jpg")

cv2.imshow("Przed", image)

(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Po", rotated)

cv2.waitKey(0)