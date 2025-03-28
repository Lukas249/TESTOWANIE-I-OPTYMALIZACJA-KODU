import cv2

image = cv2.imread("zdj.jpg")

(h,w) = image.shape[:2]

for i in range(100, 301, 20):
    resized = cv2.resize(image, (int(w*i/100), int(h*i/100)), interpolation=cv2.INTER_AREA)
    cv2.imshow(f"Resized {i}", resized)
    cv2.waitKey(500)