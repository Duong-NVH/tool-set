import cv2
import numpy as np

# read input image
img = cv2.imread('x0.jpg')

# define border color
lower = (0, 80, 110)
upper = (0, 120, 150)

# threshold on border color
mask = cv2.inRange(img, lower, upper)

# dilate threshold
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

# recolor border to white
img[mask == 255] = (255, 255, 255)

# convert img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# otsu threshold
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]

# apply morphology open
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
morph = 255 - morph

# find contours and bounding boxes
bboxes = []
bboxes_img = img.copy()
contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
for cntr in contours:
    x, y, w, h = cv2.boundingRect(cntr)
    if w > 500:
        bboxes.append((x, y, w, h))


def takeFirst(elem):
    return elem[1]


bboxes.sort(key=takeFirst)

for i, bbox in enumerate(bboxes):
    (x, y, w, h) = bbox
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite(f"cropped{i}.jpg", crop_img)


cv2.waitKey(0)
