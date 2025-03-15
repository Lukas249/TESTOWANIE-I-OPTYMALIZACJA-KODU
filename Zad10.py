import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

(b1, g1, r1) = image[50, 50]
(b2, g2, r2) = image[200, 200]

print("Pixel1 (50, 50) - Red: {}, Green: {}, Blue: {}".format(r1, g1, b1))
print("Pixel2 (200, 200) - Red: {}, Green: {}, Blue: {}".format(r2, g2, b2))

print("Difference Pixel1 - Pixel2 = Red: {}, Green: {}, Blue: {}".format(int(r1)-int(r2), int(g1)-int(g2), int(b1)-int(b2)))

cv2.waitKey(0)