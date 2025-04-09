import cv2

image1 = cv2.imread("zdj.jpg")

(B, G, R) = cv2.split(image1)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

cv2.waitKey(0)

image2 = cv2.imread("circles.jpg")

(B, G, R) = cv2.split(image2)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

cv2.waitKey(0)