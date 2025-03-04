import cv2

cv2.namedWindow("Zdjecie", cv2.WINDOW_NORMAL)
cv2.resizeWindow('Zdjecie', 900, 600)

image = cv2.imread("zdj.jpg")

cv2.imshow("Zdjecie", image)

cv2.waitKey(0)