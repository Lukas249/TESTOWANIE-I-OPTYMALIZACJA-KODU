import cv2

image = cv2.imread("zdj.jpg")
#image = cv2.imread("zdj2.jpg") # bledna sciezka

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Wyswietlony obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()