import cv2
import numpy as np

triangle1 = np.zeros((300, 300), dtype="uint8")

pts = np.array([[0, 300], [150,0], [300,300]], np.int32)
cv2.fillPoly(triangle1, [pts], color=255)

cv2.imshow("Triangle1", triangle1)

circle1 = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle1, (150, 150), 150, 255, -1)

cv2.imshow("Circle1", circle1)

bitwiseAnd1 = cv2.bitwise_and(triangle1, circle1)
bitwiseOr1 = cv2.bitwise_or(triangle1, circle1)
bitwiseXor1 = cv2.bitwise_xor(triangle1, circle1)
bitwiseNot1 = cv2.bitwise_not(triangle1)

cv2.imshow("AND1", bitwiseAnd1)
cv2.imshow("OR1", bitwiseOr1)
cv2.imshow("XOR1", bitwiseXor1)
cv2.imshow("NOT1", bitwiseNot1)

cv2.waitKey(0)
cv2.destroyAllWindows()

triangle2 = np.zeros((300, 300), dtype="uint8")

pts = np.array([[0, 300], [150,0], [300,300]], np.int32)
cv2.fillPoly(triangle2, [pts], color=255)

cv2.imshow("Triangle2", triangle2)

circle2 = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle2, (100, 100), 100, 255, -1)

cv2.imshow("Circle2", circle2)

bitwiseAnd2 = cv2.bitwise_and(triangle2, circle2)
bitwiseOr2 = cv2.bitwise_or(triangle2, circle2)
bitwiseXor2 = cv2.bitwise_xor(triangle2, circle2)
bitwiseNot2 = cv2.bitwise_not(circle2)

cv2.imshow("AND2", bitwiseAnd2)
cv2.imshow("OR2", bitwiseOr2)
cv2.imshow("XOR2", bitwiseXor2)
cv2.imshow("NOT2", bitwiseNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()