
import cv2

image = cv2.imread("zdj.jpg")

flipType = int(input("Podaj sposób odbicia (1 - poziomo, 0 - pionowo, -1 - poziomo i pionowo): "))

if -1 <= flipType <= 1:
    flipped = cv2.flip(image, flipType)

    cv2.imshow("Flipped", flipped)

    cv2.waitKey(0)