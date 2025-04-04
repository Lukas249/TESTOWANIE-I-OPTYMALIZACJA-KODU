import cv2

image = cv2.imread("zdj.jpg")

(h,w) = image.shape[:2]

for i in range(3):
    for j in range(3):
        startY = i * int(h / 3)
        endY = startY + int(h / 3)

        startX = j * int(w / 3)
        endX = startX + int(w / 3)

        fragment = image[startY:endY, startX:endX]

        cv2.imshow(f"Zdjecie{i*3 + j + 1}", fragment)
        cv2.waitKey(500)
