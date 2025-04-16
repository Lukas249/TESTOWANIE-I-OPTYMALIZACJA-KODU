import cv2

image = cv2.imread("dokument.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Original Image", image)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)
