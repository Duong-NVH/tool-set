from pathlib import Path
from tkinter import filedialog
from tkinter import *
import cv2
import numpy as np
print("Duong Dep Trai Pro Vip")

filepath = ""
outputpath = ""
imgList = []
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


def join():
    print("Processing...")
    global imgList
    global filepath
    # chunk = len(filepath)//10+1
    # for i in range(0, chunk-1):
    #     for j in range(0, 10):
    #         n = cv2.imread(filepath[i*10+j])
    #         imgList.append(n)
    #     img_v = cv2.vconcat(imgList)
    #     cv2.imwrite(f'{outputpath}/r{i}.jpg', img_v)
    #     imgList.clear()
    #     print(f"r{i}.jpg")

    # for k in range(len(filepath)//10*10, len(filepath)):
    #     n = cv2.imread(filepath[k])
    #     imgList.append(n)
    # im_v = cv2.vconcat(imgList)
    # cv2.imwrite(f'{outputpath}/r{chunk-1}.jpg', im_v)
    # imgList.clear()
    # print(f"r{chunk-1}.jpg")

    for img in filepath:
        n = cv2.imread(img)
        imgList.append(n)
    im_v = cv2.vconcat(imgList)
    cv2.imwrite(f'{outputpath}/m1.jpg', im_v)

    print("Done!")
    return


button1 = Button(window, text="Select Files", command=selectFile)
button1.pack()
button3 = Button(window, text="Select Output Folder", command=selectOutputPath)
button3.pack()
button2 = Button(window, text="Join", command=join)
button2.pack()
window.mainloop()
