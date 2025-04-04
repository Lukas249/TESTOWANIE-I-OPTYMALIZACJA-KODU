import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

cv2.imshow("Prawa polowa", image[0:h, int(w/2):w])

cv2.waitKey(0)