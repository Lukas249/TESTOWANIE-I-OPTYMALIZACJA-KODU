import cv2

image1 = cv2.imread("zdj.jpg")

(B, G, R) = cv2.split(image1)

R = cv2.add(R, 100)

merged = cv2.merge([B, G, R])

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.imshow("Image", merged)

cv2.waitKey(0)
