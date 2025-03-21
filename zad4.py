import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

(h, w) = canvas.shape[:2]

cv2.rectangle(canvas, (w // 2 - 50, h // 2 - 50), (w // 2 + 50, h // 2 + 50), (255, 0, 0))
cv2.circle(canvas, (w // 2, h // 2), 30, (0, 0, 255))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)