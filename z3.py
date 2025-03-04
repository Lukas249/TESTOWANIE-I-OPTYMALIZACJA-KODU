import cv2

image = cv2.imread("zdj.jpg", cv2.IMREAD_GRAYSCALE)

if len(image.shape) == 2:
    print("channels: 1")
else:
    print(f'channels: {image.shape[2]}')