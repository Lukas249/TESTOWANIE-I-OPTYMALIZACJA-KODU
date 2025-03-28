import cv2

image = cv2.imread("zdj.jpg")
cv2.imshow("Original", image)

(h,w) = image.shape[:2]

d = (w*4, h*4)

resized_inter_cubic = cv2.resize(image, d, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Resized INTER_CUBIC", resized_inter_cubic)

resized_inter_lanczos4 = cv2.resize(image, d, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Resized INTER_LANCZOS4", resized_inter_lanczos4)

cv2.waitKey(0)