import cv2

image = cv2.imread("zdj.jpg", cv2.IMREAD_GRAYSCALE)

(h, w) = image.shape[:2]

luminance = 0
x = 0
y = 0

for row in range(h):
    for column in range(w):
        if luminance < image[row, column]:
            luminance = image[row, column]
            y = row
            x = column

print("Max luminance = {}. Pixel ({}, {})".format(luminance, x, y))

cv2.waitKey(0)