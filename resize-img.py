import numpy as np
import cv2 as cv
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


def resize():
    print("Processing...")
    index = 0
    for img in filepath:
        img = cv.imread(img)
        txtr = cv.imread("D:/lazy manga/texture.jpg")
        h, w, cc = img.shape
        ww1 = w/1280
        hh1 = h/720
        color = (255, 255, 255)
        result = np.full((720, 1280, cc), color, dtype=np.uint8)
        if ww1 > hh1:
            h1 = round(h*1280/w)
            if h1 % 2 != 0:
                h1 += 1
            dst = cv.resize(img, (1280, h1))
            yy = (720-h1)//2
            result[yy:yy+h1, 0:1280] = dst
            print("h")

        else:
            w1 = round(w*720/h)
            if w1 % 2 != 0:
                w1 += 1
            dst = cv.resize(img, (w1, 720))
            xx = (1280-w1)//2
            result[0:720, xx:xx+w1] = dst
            print("w")
        # ovl = cv.addWeighted(txtr, 0.2, result, 1, 0)
        cv.imwrite(f'{outputpath}/{index}.jpg', result)
        print(f"---image-{index}.jpg---")
        index += 1

    print("Done!")
    return


button1 = Button(window, text="Select Files", command=selectFile)
button1.pack()
button3 = Button(window, text="Select Output Folder", command=selectOutputPath)
button3.pack()
button4 = Button(window, text="Resize", command=resize)
button4.pack()
window.mainloop()
