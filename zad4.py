import cv2

img = cv2.imread("znak.jpg")

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
    cv2.imshow("bilateralFilter({}, {}, {})".format(diameter, sigmaColor, sigmaSpace), blurred)
    cv2.waitKey(0)

# 1. Które metody najmocniej rozmywają tekst?
#    blur i GaussianBlur – szczególnie przy dużych kernalach tekst staje się nieczytelny.

# 2. Które pozwalają zachować jego czytelność?
#    medianBlur i bilateralFilter – lepiej zachowują krawędzie znaków, tekst pozostaje czytelny nawet przy większych wartościach kernela.