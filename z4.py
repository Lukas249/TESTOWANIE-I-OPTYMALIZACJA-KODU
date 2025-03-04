import cv2

image = cv2.imread("zdj.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite('nowy.jpg', image)