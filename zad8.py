import cv2

image = cv2.imread("zdj.jpg")

(h,w) = image.shape[:2]

for endX in range(200, w, 10):
    cv2.imshow("Zdjecie", image[0:h, (endX - 200):endX])
    cv2.waitKey()