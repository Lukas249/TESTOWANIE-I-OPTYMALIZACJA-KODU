import cv2
import numpy as np

img = cv2.imread("zdj.jpg")
cv2.imshow("Original", img)
cv2.waitKey(0)

noisy_img = img.copy()
noise = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.randu(noise, 0, 255)

noisy_img[noise < 2] = 0
noisy_img[noise > 253] = 255

cv2.imshow("Noisy (Salt & Pepper)", noisy_img)
cv2.waitKey(0)

ksize = 5

blurred = cv2.blur(noisy_img, (ksize, ksize))
cv2.imshow("Blur", blurred)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(noisy_img, (ksize, ksize), 0)
cv2.imshow("GaussianBlur", blurred)
cv2.waitKey(0)

# - MedianBlur najlepiej radzi sobie z szumem typu salt i pepper

blurred = cv2.medianBlur(noisy_img, ksize)
cv2.imshow("MedianBlur", blurred)
cv2.waitKey(0)

blurred = cv2.bilateralFilter(noisy_img, 11, 61, 39)
cv2.imshow("BilateralFilter", blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()
