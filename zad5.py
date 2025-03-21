import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

(h, w) = canvas.shape[:2]

for s in range(0, 175, 10):
    cv2.rectangle(canvas, (w // 2 - s, h // 2 - s), (w // 2 + s, h // 2 + s), (255,255,255))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)