
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter

root = customtkinter.CTk()
root.title("Title")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#fUNCTIONS
def resize_image(event):
    global new_height, new_width
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo

image = Image.open('Assignment\download.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)


root.mainloop()
