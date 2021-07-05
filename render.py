import numpy as np
import cv2 as cv
import subprocess
import os
from tkinter import *
from tkinter import filedialog

filepath = ""
outputpath = ""
window = Tk()


def selectFile():
    global filepath
    filepath = filedialog.askopenfilenames(filetypes=[(
        'JPG files', '*.jpg'), ('PNG files', '*.png'), ('all files', '.*')], title="Select files", multiple=True)
    print(f"Selected {len(filepath)} files")
    return


def selectOutputPath():
    global outputpath
    outputpath = filedialog.askdirectory()
    os.chdir(outputpath)
    print(f"Save to: {outputpath}")
    return


def render():
    print("Processing...")
    index = 0
    for img in filepath:
        img = cv.imread(img)
        h = img.shape[0]
        speed = 60
        time = h//speed
        cmd = f'ffmpeg -r 1 -loop 1 -t {time+1} -i r{index}.jpg -filter_complex "color = white:s = 1280x720, fps = fps = 60[bg];[bg][0]overlay = y = {speed}-t*{speed}:shortest = 1[video]" -preset ultrafast -map [video] output{str(index)}.mp4'
        subprocess.call(cmd, shell=True)
        index += 1

    print("Done!")
    return


button1 = Button(window, text="Select Files", command=selectFile)
button1.pack()
button3 = Button(window, text="Select Output Folder", command=selectOutputPath)
button3.pack()
button4 = Button(window, text="Render", command=render)
button4.pack()
window.mainloop()
