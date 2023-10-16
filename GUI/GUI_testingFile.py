import customtkinter

class checkboxFrame(customtkinter.CTkFrame):
    def __init__(self, master,title, values):
        super().__init__(master)
        #title initilization
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []
        #title placement
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        #creates a certain number of checkboxes depending on the value entered
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

        # how to create 3 hardcoded checkboxes
        # self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox1")
        # self.checkbox_1.grid(row=0, column=0, padx=20, pady=(0, 20), sticky="w")
        # #creates a second checkbox
        # self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # self.checkbox_2.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        # #the benefits of using a frame clbit ass is because the class itself is separate from the class App funciton we can just add another checkbox without any other changes
        # #creates a third checkbox
        # self.checkbox_3 = customtkinter.CTkCheckBox(self, text="checkbox 3")
        # self.checkbox_3.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")

    #to add functionality to the buttons, we use a get function to check what checkboxes are pressed -- this will be checked when the button is pressed
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        # code for appending the hardcoded checkboxes
        # if self.checkbox_1.get() == 1:
        #     checked_checkboxes.append(self.checkbox_1.cget("text"))
        # if self.checkbox_2.get() == 1:
        #     checked_checkboxes.append(self.checkbox_2.cget("text"))
        # if self.checkbox_3.get() == 1:
        #     checked_checkboxes.append(self.checkbox_3.cget("text"))

        return checked_checkboxes

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
        self.checkbox_frame = checkboxFrame(self, "Values", values=["value 1", "value 2", "value 3"]) #we call the frame class we created above -- think of this as a component we just place into the main frame
        self.checkbox_frame.grid(row=0, column = 0, padx = 10, pady =(10,0), sticky ="nsw")
        
        #creating a second instance of the above checkbox class beside the first class
        self.checkbox_frame2 = checkboxFrame(self, "Options", values=["option 1", "option 2"]) 
        self.checkbox_frame2.grid(row=0, column = 1, padx = 10, pady =(10,0), sticky ="nsew")

        #creates the button 
        self.button = customtkinter.CTkButton(self, text = "press here", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    #creates command for the button above and prints what checkboxes have been pressed
    def button_callback(self):
        print("checked checkboxes:", self.checkbox_frame.get())
        print("checked checkboxes 2:", self.checkbox_frame2.get()) 

app = App()
app.mainloop()  