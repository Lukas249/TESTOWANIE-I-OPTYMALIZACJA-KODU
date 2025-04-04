import cv2

print("Wycinanie fragmentu obrazu")
startX = int(input("start x: "))
endX = int(input("end x: "))

startY = int(input("start y: "))
endY = int(input("end y: "))

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

if 0 <= startX <= endX and startX <= endX <= w and 0 <= startY <= endY and startY <= endY <= h:
    cv2.imshow("Fragment", image[startY:endY, startX:endX])
    cv2.waitKey(0)
else:
    print("Podaj poprawny fragment")
