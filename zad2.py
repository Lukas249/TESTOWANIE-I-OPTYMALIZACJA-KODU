import cv2

img = cv2.imread("zdj.jpg")

ksizes = [5, 9, 15]
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for i in range(3):
    (diameter, sigmaColor, sigmaSpace) = params[i]
    ksize = ksizes[i]

    blur = cv2.blur(img, (ksize, ksize))
    cv2.imshow(f"Blur ({ksize},{ksize})", blur)
    cv2.waitKey(0)

    gblur = cv2.GaussianBlur(img, (ksize, ksize), 0)
    cv2.imshow(f"GaussianBlur ({ksize},{ksize})", gblur)
    cv2.waitKey(0)

    mblur = cv2.medianBlur(img, ksize)
    cv2.imshow(f"MedianBlur ({ksize},{ksize})", mblur)
    cv2.waitKey(0)

    bblur = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
    cv2.imshow(f"BilateralFilter ({diameter},{sigmaColor},{sigmaSpace})", bblur)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
#    Im większy kernel, tym silniejsze i bardziej rozmyte są efekty.
#    Detale znikają, szum jest bardziej wygładzany.
# Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
#     5x5 – daje dobrą równowagę między usunięciem szumu a zachowaniem szczegółów.
