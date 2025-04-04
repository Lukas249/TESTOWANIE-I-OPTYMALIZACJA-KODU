import cv2

image = cv2.imread("zdj.jpg")

fragment = image[0:300, 0:300]

cv2.imwrite("cropped_image.jpg", fragment)