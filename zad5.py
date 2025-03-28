import cv2

image = cv2.imread("zdj.jpg")

cv2.imshow("Original", image)

(h, w) = image.shape[:2]

cx = int(w / 2)
cy = int(h / 2)

fragment = image[cy - 100:cy + 100, cx - 100:cx + 100]

flipped_fragment = cv2.flip(fragment, -1)

(fh, fw) = flipped_fragment.shape[:2]

image[cy - 100:cy + 100, cx - 100:cx + 100] = flipped_fragment[0:fh, 0:fw]

cv2.imshow("After", image)

cv2.waitKey(0)
