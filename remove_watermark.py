import tkinter
import numpy as np
import cv2 as cv
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

filepath = ""
outputpath = ""
preview = ""
mask = ""
rate = 1
isLeftBtnDown = FALSE
brushsize = 5
intensity = 10

window = Tk()
# window.iconphoto(False, tkinter.PhotoImage(file='approved.png'))
window.geometry("350x180")
window.title("BOSS WATERMARK REMOVER V.01")
window.resizable(0, 0)

style = Style()

style.configure('TButton', font=('calibri', 16),
                borderwidth='4', height=6, width=24)


def selectFile():
    global filepath
    filepath = filedialog.askopenfilenames(filetypes=[(
        'JPG files', '*.jpg'), ('PNG files', '*.png'), ('all files', '.*')], title="Select files", multiple=True)
    print(f"Selected {len(filepath)} files")
    button2["state"] = NORMAL
    return


def selectOutputPath():
    global outputpath
    outputpath = filedialog.askdirectory()
    print(f"Save to: {outputpath}")
    button4["state"] = NORMAL
    return


def mask():
    global preview
    global mask
    global rate
    img = cv.imread(filepath[0])
    h, w, cc = img.shape
    rate = h/800
    new_weight = round(w/rate)
    mask = np.zeros([h, w, 1], dtype=np.uint8)

    preview = cv.resize(img, (new_weight, 800))

    cv.namedWindow(winname="Press ESC to exit after you're done")

    cv.setMouseCallback("Press ESC to exit after you're done", draw_circle)

    while True:
        cv.imshow("Press ESC to exit after you're done", preview)

        if cv.waitKey(10) & 0xFF == 27:
            break

    cv.destroyAllWindows()
    button3["state"] = NORMAL
    return


def draw_circle(event, x, y, flags, param):
    global isLeftBtnDown

    if event == cv.EVENT_LBUTTONUP:
        isLeftBtnDown = FALSE

    if event == cv.EVENT_LBUTTONDOWN:
        isLeftBtnDown = TRUE

    if isLeftBtnDown and event == cv.EVENT_MOUSEMOVE:
        cv.circle(preview, (x, y), brushsize, (255, 255, 255), -1)
        cv.circle(mask, (round(x*rate), round(y*rate)),
                  round(brushsize*rate), (255, 255, 255), -1)


def removeWatermark():
    print("Processing...")
    index = 0
    for img in filepath:
        img = cv.imread(img)
        dst = cv.inpaint(img, mask, intensity, cv.INPAINT_NS)

        cv.imwrite(f'{outputpath}/{index}.jpg', dst)
        print(f"{(index+1)/len(filepath)*100}%")
        index += 1

    print("Done!")
    return


button1 = Button(window, text="Select Files", command=selectFile)
button1.pack()
button2 = Button(window, text="Create Mask", command=mask, state=DISABLED)
button2.pack()
button3 = Button(window, text="Select Output Folder",
                 command=selectOutputPath, state=DISABLED)
button3.pack()
button4 = Button(window, text="Remove Watermark",
                 command=removeWatermark, state=DISABLED)
button4.pack()
l1 = tkinter.Label(text="duongnvh.work@gmail.com", fg="white", bg="black",
                   font=('calibri', 11)).pack()

window.mainloop()
