import customtkinter


class checkboxFrame(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        #creates a checkbox
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox1")
        self.checkbox_1.grid(row=0, column=0, padx=20, pady=(0, 20), sticky="w")

        #creates a second checkbox
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        #the benefits of using a frame clbit ass is because the class itself is separate from the class App funciton we can just add another checkbox without any other changes
        #creates a third checkbox
        self.checkbox_3 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_3.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")

# we should use classes because it makes the code cleaner and more compact
class App(customtkinter.CTk):
    def __init__(self): #initializes, for all tkinter code, you find replace app with self
        super().__init__()
        #initializing the size and tite
        self.title("Pacemaker GUI")
        self.geometry("400x200")

        #creates padding for the the columns and rows -- makes them equally spaced
        self.grid_columnconfigure((0,1), weight =1)
        self.grid_rowconfigure((0,1), weight =1)

        #creating a frame -- a container for the button
        ## this is the gray background behind each checkbox
        self.checkbox_frame = checkboxFrame(self) #we call the frame class we created above -- think of this as a component we just place into the main frame
        self.checkbox_frame.grid(row=0, column = 0, padx = 10, pady =(10,0), sticky ="nsw")


        #creates the button 
        self.button = customtkinter.CTkButton(self, text = "press here", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    #creates command for the button above 
    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()  