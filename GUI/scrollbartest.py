# Import Libraries
from tkinter import *
import customtkinter
from tkinter import font
import json
import os

# Import External Classes
from program_classes.user_class import user

# App Class
class DCM(customtkinter.CTk):
    # class variables
    bg_colour = "#1A1A1A"
    gray_1 = "#2A2A2A"
    gray_2 = "#8f8f8f"
    blue_1 = "#195FA6"
    white_1 = "#D9D9D9"

    # init function to initialize the window
    def __init__(self):
        super().__init__()
        self.title("G29 - MECHTRON 3K04 - DCM")
        self.geometry("1000x700")
        self.resizable(height=False, width=False)
        self.create_login_screen()

    def on_enter(self, event):
        event.widget.config(font=("TkDefaultFont", 12, "underline"))

    def on_leave(self, event):
        event.widget.config(font=("TkDefaultFont", 12))

    def create_login_screen(self):
        # ... [rest of the create_login_screen method]

# Main
if __name__ == "__main__":
    dcm = DCM()
    dcm.mainloop()