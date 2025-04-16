import cv2

image = cv2.imread("j.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image", image)

cv2.waitKey(0)

# Eliptyczny kernel daje łagodniejsze efekty widoczne na zakrzywionych obiektach

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
eroded_rect = cv2.erode(image.copy(), kernel_rect, iterations=1)
cv2.imshow("Eroded RECT", eroded_rect)
cv2.waitKey(0)

kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
eroded_ellipse = cv2.erode(image.copy(), kernel_ellipse, iterations=1)
cv2.imshow("Eroded ELLIPSE", eroded_ellipse)
cv2.waitKey(0)
