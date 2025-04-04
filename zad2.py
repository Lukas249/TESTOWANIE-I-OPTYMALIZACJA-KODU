import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

upperFragment = image[0:int(h/2), 0:w]
bottomFragment = image[int(h/2):h, 0:w]

cv2.imshow("Dolna polowa", bottomFragment)

cv2.waitKey(0)