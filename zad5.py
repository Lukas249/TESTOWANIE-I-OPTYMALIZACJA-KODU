import cv2

image = cv2.imread("face.jpg")

(h, w) = image.shape[:2]

cv2.imshow("Twarz", image[0:800, 620:1315])

cv2.waitKey(0)