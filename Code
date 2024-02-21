
#Importing modules
from tkinter import *
import customtkinter as ctk
import pyttsx3
import googletrans
from textblob import*

#Variables 
geo = '500x600'
Main_name = "Project"


#Setting up Tkinter
Window = ctk.CTk()
Window.title(Main_name)
Window.geometry(geo)
#Grid Configuration
Grid.rowconfigure(Window,0,weight=1) #automatically weight is set to 0, so if there is any extra room it won't fill but it will now fill because its set to 1
Grid.columnconfigure(Window,0,weight=1)
Grid.rowconfigure(Window,1,weight=1)
#Buttons
Button1 = ctk.CTkButton(Window, text="Button1")
Button2 = Button(Window, text="button2")
Button1.grid(row=0,column=0,sticky="NSEW") #Sticky = NSEW allows it dynamically resize itself
Button2.grid(row=1,column=0,sticky="NSEW")




Window.mainloop()

