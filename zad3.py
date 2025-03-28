import cv2

image = cv2.imread("zdj.jpg")

cv2.imshow("Original", image)

flipped = cv2.flip(image, -1)

cv2.imshow("Flipped", flipped)

cv2.waitKey(0)