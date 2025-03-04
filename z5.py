import cv2

image1 = cv2.imread("zdj.jpg")
image2 = cv2.imread("nowy.jpg")

cv2.imshow("Wyświetlony obraz1", image1)
cv2.imshow("Wyświetlony obraz2", image2)

if(cv2.waitKey(0) > 0):
    cv2.destroyWindow('Wyświetlony obraz1')

if(cv2.waitKey(0) > 0):
    cv2.destroyWindow('Wyświetlony obraz2')