import cv2

image = cv2.imread("zdj.jpg")

print(f'channels: {image.shape[2]}')