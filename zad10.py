import cv2

image = cv2.imread("zdj.jpg")

(h,w) = image.shape[:2]

resized = cv2.resize(image, (800, h), interpolation=cv2.INTER_AREA)

cv2.imwrite("resized_output.jpg", resized)