import numpy as np
import cv2
from tkinter import *
from tkinter import filedialog

filepath = ""
outputpath = ""
window = Tk()


def selectFile():
    global filepath
    filepath = filedialog.askopenfilenames(filetypes=[(
        'JPG files', '*.jpg'), ('JPEG files', '*.jpeg'), ('PNG files', '*.png'), ('all files', '.*')], title="Select files", multiple=True)
    print(f"Selected {len(filepath)} files")
    return


def selectOutputPath():
    global outputpath
    outputpath = filedialog.askdirectory()
    print(f"Save to: {outputpath}")
    return


def takeFirst(elem):
    return elem[1]


def cropSlide():
    print("Processing...")
    path_index = 0
    for path in filepath:
        print(path)
        img = cv2.imread(path)
        lower = (0, 80, 110)
        upper = (0, 120, 150)
        mask = cv2.inRange(img, lower, upper)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
        img[mask == 255] = (255, 255, 255)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        morph = 255 - morph
        bboxes = []
        contours = cv2.findContours(
            morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        for cntr in contours:
            x, y, w, h = cv2.boundingRect(cntr)
            if w > img.shape[1]*0.5:
                bboxes.append((x, y, w, h))
        bboxes.sort(key=takeFirst)
        for i, bbox in enumerate(bboxes):
            (x, y, w, h) = bbox
            crop_img = img[y:y+h, x:x+w]
            cv2.imwrite(f"{outputpath}/{path_index+i}.jpg", crop_img)
        print(f"{path_index}")
        path_index += len(bboxes)

    print("Done!")
    return


button1 = Button(window, text="Select Files", command=selectFile)
button1.pack()
button3 = Button(window, text="Select Output Folder", command=selectOutputPath)
button3.pack()
button4 = Button(window, text="Crop", command=cropSlide)
button4.pack()
window.mainloop()
