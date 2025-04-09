import cv2

image = cv2.imread("zdj.jpg")
(B, G, R) = cv2.split(image)

cv2.imwrite("R.jpg", R)
cv2.imwrite("G.jpg", G)
cv2.imwrite("B.jpg", B)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

cv2.waitKey(0)