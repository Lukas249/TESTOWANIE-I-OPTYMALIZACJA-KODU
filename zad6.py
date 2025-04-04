import cv2

image = cv2.imread("zdj.jpg")

leftTop = image[0:100, 0:100]

image[100:200, 100:200] = leftTop

cv2.imshow("Zdjecie", image)

cv2.waitKey(0)