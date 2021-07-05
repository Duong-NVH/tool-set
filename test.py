from tkinter.constants import FALSE, TRUE
import cv2 as cv


img = cv.imread("x0.jpg")

h, w, cc = img.shape

rate = h/800
new_weight = round(w/rate)

isLeftBtnDown = FALSE

preview = cv.resize(img, (new_weight, 800))


def draw_circle(event, x, y, flags, param):
    global isLeftBtnDown

    if event == cv.EVENT_LBUTTONUP:
        isLeftBtnDown = FALSE

    if event == cv.EVENT_LBUTTONDOWN:
        isLeftBtnDown = TRUE

    if isLeftBtnDown and event == cv.EVENT_MOUSEMOVE:
        cv.circle(preview, (x, y), 20, (255, 255, 255), -1)
