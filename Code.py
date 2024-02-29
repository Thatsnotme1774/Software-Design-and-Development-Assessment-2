from tkinter import *
import customtkinter as ctk
import pyttsx3
import googletrans
from textblob import*
from tkinter import PhotoImage
from PIL import Image, ImageTk


#Variables 
geo = '500x600'
Main_name = "Project"

Window = ctk.CTk()
Window.title(Main_name)
Window.geometry(geo)

#frame

#Buttons



def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ctk.CTkImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('Assignment\download.png')
copy_of_image = image.copy()
photo = ctk.CTkImage(image)
label = ctk.CTkLabel(Window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

Window.mainloop()
