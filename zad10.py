import cv2

image = cv2.imread("zdj.jpg")

(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

for r in range(0, 360, 15):
    M = cv2.getRotationMatrix2D((cX, cY), 15, 1.0)
    image = cv2.warpAffine(image, M, (w, h))
    cv2.imshow(f"Obrot (stopnie): {r}", image)
    cv2.waitKey(500)
