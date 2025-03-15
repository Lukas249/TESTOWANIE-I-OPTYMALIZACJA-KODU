import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

cv2.imshow("Before", image)

image[50:100, 50:100] = (255, 255, 255)

cv2.imshow("After", image)

cv2.waitKey(0)