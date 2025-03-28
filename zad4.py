import cv2

image = cv2.imread("zdj.jpg")
cv2.imshow("Original", image)

(h,w) = image.shape[:2]

dim = (w*3, h*3)

resized_inter_nearest = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST)

cv2.imshow("Resized INTER_NEAREST", resized_inter_nearest)

resized_inter_linear = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Resized INTER_LINEAR", resized_inter_linear)

resized_inter_cubic = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Resized INTER_CUBIC", resized_inter_cubic)

resized_inter_lanczos4 = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Resized INTER_LANCZOS4", resized_inter_lanczos4)

cv2.waitKey(0)