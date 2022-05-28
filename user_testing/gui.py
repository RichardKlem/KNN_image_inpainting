# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
from matplotlib import image
import random

label1 = None
label2 = None
win = None
i = 1
mask = False
swaped = False

def get_shape(file):
    img = image.imread(file)
    h, w, _ = img.shape
    return h, w

def add_image(file, order, win):
    h, w = get_shape(file)
    rely = 0.25

    if order == 2:
        rely = 0.75

    frame = Frame(win, width=w, height=h)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=rely)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open(file))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()

def button_callback_up():
    # default baseline
    global i, swaped

    file1 = 'output/baseline/' + str(i).rjust(4, '0') + '.png'
    file2 = 'output/modified/' + str(i).rjust(4, '0') + '.png'

    if swaped:
        tmp = file1
        file1 = file2
        file2 = tmp

    with open("results.txt", "a") as f:
        f.write(f"{file1}\t\t 1\n")
        f.write(f"{file2}\t\t 0\n")

def button_callback_down():
    # default modified
    global i, swaped

    file1 = 'output/baseline/' + str(i).rjust(4, '0') + '.png'
    file2 = 'output/modified/' + str(i).rjust(4, '0') + '.png'

    if swaped:
        tmp = file1
        file1 = file2
        file2 = tmp

    with open("results.txt", "a") as f:
        f.write(f"{file1}\t\t 0\n")
        f.write(f"{file2}\t\t 1\n")

def button_callback_next():
    global label1, label2, win, i, swaped

    i += 1

    swaped = random.choice([True, False])

    file1 = 'output/baseline/' + str(i).rjust(4, '0') + '.png'
    file2 = 'output/modified/' + str(i).rjust(4, '0') + '.png'

    h, w = get_shape(file1)
    frame1.width = w
    frame1.height = h
    frame2.width = w
    frame2.height = h

    img1 = ImageTk.PhotoImage(Image.open(file1))
    img2 = ImageTk.PhotoImage(Image.open(file2))

    if swaped:
        tmp = img1
        img1 = img2
        img2 = tmp

    if h > 512:
        ratio = h / 512
        w = int(w / ratio)
        img1 = Image.open(file1)
        img1 = img1.resize((w, 512), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(file2)
        img2 = img2.resize((w, 512), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)

    label1.configure(image=img1)
    label1.image = img1
    label2.configure(image=img2)
    label2.image = img2

def button_callback_mask():
    global label1, label2, win, i, mask, swaped

    mask = not mask

    file1 = 'output/baseline/' + str(i).rjust(4, '0') + '.png'
    file2 = 'output/modified/' + str(i).rjust(4, '0') + '.png'

    if mask:
        file1 = 'output/masks/' + str(i).rjust(4, '0') + '_mask.png'
        file2 = 'output/masks/' + str(i).rjust(4, '0') + '_mask.png'

    if swaped:
        tmp = file1
        file1 = file2
        file2 = tmp

    h, w = get_shape(file1)
    frame1.width = w
    frame1.height = h
    frame2.width = w
    frame2.height = h

    img1 = ImageTk.PhotoImage(Image.open(file1))
    img2 = ImageTk.PhotoImage(Image.open(file2))

    if h > 512:
        ratio = h / 512
        w = int(w / ratio)
        img1 = Image.open(file1)
        img1 = img1.resize((w, 512), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(file2)
        img2 = img2.resize((w, 512), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)


    label1.configure(image=img1)
    label1.image = img1
    label2.configure(image=img2)
    label2.image = img2

win = Tk()

win.geometry("1920x1080")

file1 = "output/baseline/0001.png"
file2 = "output/modified/0001.png"
mask = "output/masks/0001_mask.png"

h, w = get_shape(file1)

frame1 = Frame(win, width=w, height=h)
frame1.pack()
frame1.place(anchor='center', relx=0.5, rely=0.25)

img1 = ImageTk.PhotoImage(Image.open(file1))

label1 = Label(frame1, image = img1)
label1.pack()

frame2 = Frame(win, width=w, height=h)
frame2.pack()
frame2.place(anchor='center', relx=0.5, rely=0.75)

img2 = ImageTk.PhotoImage(Image.open(file2))

label2 = Label(frame2, image = img2)
label2.pack()

# add_image("output/baseline/0001.png", 1, win)
# add_image("output/modified/0001.png", 2)

b1 = Button(win, text ="Up", command = button_callback_up)
b2 = Button(win, text ="Down", command = button_callback_down)
b3 = Button(win, text ="Next", command = button_callback_next)
b4 = Button(win, text ="Mask", command = button_callback_mask)


b1.place(x=60, y=60)
b2.place(x=60, y=110)
b3.place(x=60, y=200)
b4.place(x=60, y=250)

win.mainloop()
