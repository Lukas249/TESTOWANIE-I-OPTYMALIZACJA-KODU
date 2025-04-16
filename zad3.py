import cv2

image = cv2.imread("opening.png")

cv2.imshow("Image", image)

cv2.waitKey(0)

# size (5,5) radzi sobie najlepiej - usuwa szum, ale nie usuwa elementów

kernelSizes = [(3, 3), (5, 5), (7, 7)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(
    kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)
