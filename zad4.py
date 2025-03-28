import cv2

image = cv2.imread("zdj.jpg")

cv2.imshow("Original", image)

flipped_h = cv2.flip(image, 1)

cv2.imshow("Flipped Horizontally", flipped_h)

flipped_v = cv2.flip(image, 0)

cv2.imshow("Flipped Vertically", flipped_v)

flipped_b = cv2.flip(image, -1)

cv2.imshow("Flipped Horizontally and Vertically", flipped_b)

cv2.waitKey(0)