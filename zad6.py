import cv2

img = cv2.imread("osoba.jpg")

cv2.circle(img, (87, 117), 12, (0,0,255), -1)

cv2.circle(img, (135, 110), 12, (0,0,255), -1)

cv2.rectangle(img, (90, 165), (140, 150), (0, 255, 0), -1)

cv2.circle(img, (110, 120), 75, (255, 0, 0))

cv2.imshow("Canvas", img)
cv2.waitKey(0)