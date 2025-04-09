import cv2

image1 = cv2.imread("zdj.jpg")

image2 = image1.copy()

cv2.rectangle(image1, (50, 50), (100, 100), (255, 0, 0), -1)

cv2.rectangle(image2, (100,100), (150, 150), (255, 0, 0), -1)

result = cv2.bitwise_xor(image1, image2)

cv2.imshow("Zdjecie 1", image1)
cv2.imshow("Zdjecie 2", image2)

cv2.imshow("Diff", result)

cv2.waitKey(0)