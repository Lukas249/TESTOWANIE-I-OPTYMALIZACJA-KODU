import pandas as pd
import cv2

image = cv2.imread("j.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image", image)

kernelSizes = [(3, 3), (5, 5), (7, 7)]

results = []

for size in kernelSizes:
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, size)
    kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, size)

    kernels = [kernel_ellipse, kernel_rect]

    for j in range(0, 2):
        kernel = kernels[j]

        for i in range(0, 3):
            dilated = cv2.dilate(image.copy(), kernel, iterations=i + 1)

            white_pixels = cv2.countNonZero(dilated)
            results.append((size, i, white_pixels, j))

df = pd.DataFrame(results, columns=["Rozmiar kernela", "Liczba iteracji", "Liczba białych pikseli", "Typ kernela"])

print(df)
