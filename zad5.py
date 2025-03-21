import cv2
import imutils

print("Przesunięcie obrazu")

tx = int(input("Podaj x:"))
ty = int(input("Podaj y:"))

img = cv2.imread("zdj.jpg")

(h, w) = img.shape[:2]

cv2.imshow("Przed przesunieciem", img)

shifted = imutils.translate(img, tx, ty)

cv2.imshow("Po przesunieciu", shifted)

cv2.waitKey(0)