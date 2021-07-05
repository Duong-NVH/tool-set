from tkinter import *
from tkinter import filedialog
from pathlib import Path
from PIL import Image
import pathlib

filepath=""
markpath=""
outputpath=""
window = Tk()

def selectFile():
    global filepath
    filepath = filedialog.askopenfilenames(filetypes=[('JPG files', '*.jpg'),('JPEG files', '*.jpeg'),('PNG files', '*.png'),('all files', '.*')],title="Select files", multiple=True)
    print(f"Selected {len(filepath)} files")
    return


def selectOutputPath():
    global outputpath
    outputpath = filedialog.askdirectory()
    print(f"Save to: {outputpath}")
    return

def overlay():
    print("Processing...")
    global markpath
    index=1
    for img in filepath:
        theimage= Image.open(pathlib.Path(img))
        mark= Image.open('2lazy4manga.png')
        theimage.paste(mark,(0,0),mark)
        theimage.save(f'{outputpath}/image-{index}.jpg')
        print(f"---image-{index}.jpg---")
        index +=1

    print("Done!")
    return

button1 = Button(window,text="Select Files",command=selectFile)
button1.pack()
button3 = Button(window,text="Select Output Folder",command=selectOutputPath)
button3.pack()
button4 = Button(window,text="Overlay",command=overlay)
button4.pack()
window.mainloop()