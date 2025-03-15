import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

x = int(input("Podaj x:"))
y = int(input("Podaj y:"))

if not (0 <= x < w and 0 <= y < h):
    print("podane współrzędne wychodzą poza wymiar zdjęcia.")
    exit()

image[y, x] = (0, 0, 0)
