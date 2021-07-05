import cv2
import numpy as np

img = cv2.imread("testt.jpg")
# 2 160
# alpha = 2.0
# beta = -200

# new = alpha * img + beta
# new = np.clip(new, 0, 255).astype(np.uint8)
img[:, :, 0] = np.zeros([img.shape[0], img.shape[1]])

cv2.imwrite("0000.png", img)
