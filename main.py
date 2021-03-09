from tkinter import *
import PIL
from PIL import Image, ImageDraw
from tkinter import colorchooser, ttk


def clear_canvas():
    draw_canvas.delete(ALL)


def start_paint(e):
    global lastx, lasty
    draw_canvas.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def eraser_on():
    global eraser_mode
    eraser_mode = True
    erase_button.config(relief=SUNKEN)
    draw_button.config(relief=RAISED)


def pen_on():
    global eraser_mode
    eraser_mode = False
    erase_button.config(relief=RAISED)
    draw_button.config(relief=SUNKEN)


def change_pen_size(placeholder):
    global penwidth
    penwidth = slider.get()


def change_pen_colour():
    global pen_colour
    new_colour = colorchooser.askcolor()[1]
    pen_colour = new_colour


def change_bg_colour():
    new_colour = colorchooser.askcolor()[1]
    draw_canvas.config(bg=new_colour)


def paint(e):
    global pen_colour
    global lastx, lasty
    global eraser_mode
    global penwidth

    x, y = e.x, e.y
    if not eraser_mode:
        draw_canvas.create_line((lastx, lasty, x, y), width=round(penwidth), fill=pen_colour, capstyle=ROUND)
        draw.line((lastx, lasty, x, y), width=round(penwidth))
    else:
        draw_canvas.create_line((lastx, lasty, x, y), width=round(penwidth), fill=draw_canvas["bg"], capstyle=ROUND)
        draw.line((lastx, lasty, x, y))

    lastx, lasty = x, y


root = Tk()
root.title("Hawky's Paint")

lastx, lasty = None, None
eraser_mode = False
penwidth = 5
pen_colour = "black"

top_button_frame = Frame(root)
top_button_frame.pack()
canvas_frame = Frame(root)
canvas_frame.pack(expand=YES, fill=BOTH)
button_frame = Frame(root)
button_frame.pack()

draw_canvas = Canvas(canvas_frame, width=660, height=480, bg='white')

image1 = PIL.Image.new('RGB', (660, 480), 'white')
draw = ImageDraw.Draw(image1)

draw_canvas.bind('<1>', start_paint)
draw_canvas.pack(expand=YES, fill=BOTH)

clear_button = Button(button_frame, text="Clear Canvas", command=clear_canvas, width=10)
clear_button.grid(row=0, column=1, padx=2, pady=2)

erase_button = Button(button_frame, text="Eraser", command=eraser_on, width=10)
erase_button.grid(row=0, column=2, padx=2, pady=2)

draw_button = Button(button_frame, text="Draw", command=pen_on, width=10)
draw_button.grid(row=0, column=3, padx=2, pady=2)

Label(button_frame, text='Pen Width:').grid(row=0,column=4)
slider = ttk.Scale(button_frame,from_= 5, to = 100,command=change_pen_size,orient=HORIZONTAL)
slider.set(penwidth)
slider.grid(row=0,column=5,ipadx=30)

colour_button = Button(top_button_frame, text="Change Pen Colour", command=change_pen_colour, width=21)
colour_button.grid(row=0, column=0, padx=2, pady=2)

bg_colour_button = Button(top_button_frame, text="Change Background Colour", command=change_bg_colour, width=21)
bg_colour_button.grid(row=0, column=1, padx=2, pady=2)


root.mainloop()
