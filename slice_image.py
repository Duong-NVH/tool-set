from tkinter import filedialog
from tkinter import *
from PIL import Image
import pathlib


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


def sliceImage():
    print("Processing...")
    index = 1
    for img in filepath:
        im = Image.open(pathlib.Path(img))
        width, height = im.size
        im1 = im.crop((0, 0, width, 720))
        im2 = im.crop((0, (height-720)/2, width, (height-720)/2+720))
        im3 = im.crop((0, height-720, width, height))
        im1.save(f"{outputpath}/img-{index}.jpg")
        im2.save(f"{outputpath}/img-{index+1}.jpg")
        im3.save(f"{outputpath}/img-{index+2}.jpg")
        index += 3

    print("Done!")
    return


button1 = Button(window, text="Select Files", command=selectFile)
button1.pack()
button3 = Button(window, text="Select Output Folder", command=selectOutputPath)
button3.pack()
button4 = Button(window, text="slice", command=sliceImage)
button4.pack()
window.mainloop()
