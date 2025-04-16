import cv2

image = cv2.imread("closing.png")

cv2.imshow("Image", image)

cv2.waitKey(0)

shapes = [
    cv2.MORPH_RECT,
    cv2.MORPH_ELLIPSE,
    cv2.MORPH_CROSS
]

kernel_sizes = [(3, 3), (5, 5)]

for shape_type in shapes:
    for size in kernel_sizes:
        kernel = cv2.getStructuringElement(shape_type, size)

        eroded = cv2.erode(image, kernel, iterations=1)
        cv2.imshow(f"Erozja", eroded)
        cv2.waitKey(0)

        dilated = cv2.dilate(image, kernel, iterations=1)
        cv2.imshow(f"Dylatacja", dilated)
        cv2.waitKey(0)

        opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        cv2.imshow(f"Otwarcie", opened)
        cv2.waitKey(0)

        closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        cv2.imshow(f"Zamknięcie", closed)
        cv2.waitKey(0)

        gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
        cv2.imshow(f"Gradient", gradient)
        cv2.waitKey(0)

# Erozja – zmniejsza obiekty, usuwa cienkie elementy
#
# Dylatacja – pogrubia obiekty, łączy przerwy
#
# Otwarcie – usuwa szumy
#
# Zamknięcie – łączy przerwy wewnątrz obiektów
#
# Gradient morfologiczny – uwydatnia kontury