import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

(h, w) = canvas.shape[:2]

cv2.line(canvas, (w // 2, h // 2), (w - 1, h - 1),  (255, 0, 0), 2)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)