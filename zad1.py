import cv2

img = cv2.imread("zdj.jpg")

cv2.imshow("Original", img)
cv2.waitKey(0)

ksizes = [5, 9, 15]
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for i in range(3):
    (diameter, sigmaColor, sigmaSpace) = params[i]
    ksize = ksizes[i]

    blurred = cv2.blur(img, (ksize,ksize))
    cv2.imshow("Blur({}, {})".format(ksize,ksize), blurred)
    cv2.waitKey(0)

    blurred = cv2.GaussianBlur(img, (ksize,ksize), 0)
    cv2.imshow("GaussianBlur({}, {})".format(ksize,ksize), blurred)
    cv2.waitKey(0)

    blurred = cv2.medianBlur(img, ksize)
    cv2.imshow("medianBlur({}, {})".format(ksize,ksize), blurred)
    cv2.waitKey(0)

    blurred = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
    cv2.imshow("bilateralFilter({},{},{})".format(diameter, sigmaColor, sigmaSpace), blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# 1. Najlepiej szum usuwa (np typu salt i paper): medianBlur, ale również rozmywa obrazek
# 2. Najwięcej szczegółów zachowuje: bilateralFilter
# 3. Zalety/Wady metod:
#    - blur: mocno zaciera obraz i detale.
#    - GaussianBlur: rozmywa bardziej naturalnie niż blur, dobrze działa na szum Gaussa, ale też gubi krawędzie.
#    - medianBlur: usuwa szum punktowy
#    - bilateralFilter: najlepszy balans – zmniejsza szum, a jednocześnie zachowuje ostrość krawędzi.