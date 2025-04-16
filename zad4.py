import cv2

image = cv2.imread("closing.png")

cv2.imshow("Image", image)

cv2.waitKey(0)

kernelSizes = [(3, 3), (5, 5), (7, 7)]

# size (5,5) radzi sobie najlepiej - łączy małe przerwy, ale nie łączy dwóch osobnych elementów

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(
        kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

# Eliptyczny kernel lepiej łączy obiekty, które mają okrągłe kształty

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernelSize)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(
        kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)
