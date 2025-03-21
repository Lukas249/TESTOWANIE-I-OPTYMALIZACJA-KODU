import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

(h, w) = canvas.shape[:2]

cv2.circle(canvas, (40,40), 40, (255, 0, 0))
cv2.circle(canvas, (w // 2, h // 2), 60, (0, 0, 255))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)