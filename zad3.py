import cv2

img = cv2.imread("rubiks_cube.png")

cv2.imshow("Original", img)
cv2.waitKey(0)

ksizes = [5, 9, 15]
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for i in range(3):
    (diameter, sigmaColor, sigmaSpace) = params[i]
    ksize = ksizes[i]

    bilateral = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(f"Bilateral ({diameter},{sigmaColor},{sigmaSpace})", bilateral)
    cv2.waitKey(0)

    gaussian = cv2.GaussianBlur(img, (ksize, ksize), 0)
    cv2.imshow(f"GaussianBlur ({ksize},{ksize})", gaussian)
    cv2.waitKey(0)

    medianBlur = cv2.medianBlur(img, ksize)
    cv2.imshow(f"medianBlur ({ksize},{ksize})", medianBlur)
    cv2.waitKey(0)

    blur = cv2.blur(img, (ksize, ksize))
    cv2.imshow(f"Blur ({ksize},{ksize})", blur)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Czy rozmycie dwustronne skutecznie redukuje szum?
#    Tak, skutecznie wygładza obraz, zwłaszcza szum o niskiej częstotliwości.

# Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
#    Tak, lepiej niż blur i GaussianBlur – krawędzie pozostają wyraźne.

# Jakie wartości parametrów dają najlepsze rezultaty?
#     (11, 61, 39) – ładnie wygładza i zachowuje detale.
