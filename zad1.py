import cv2

image = cv2.imread("zdj.jpg")

cv2.imshow("Lewy rog", image[0:100, 0:100])

cv2.waitKey(0)