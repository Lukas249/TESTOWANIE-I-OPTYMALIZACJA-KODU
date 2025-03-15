import cv2

image = cv2.imread("zdj.jpg")

(b, g, r) = image[0, 0]

print("Pixel (0,0). Blue: {} Green: {} Red: {}".format(b, g, r))