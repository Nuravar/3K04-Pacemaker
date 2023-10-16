import os
import customtkinter
import tkinter
import hashlib
import numpy as np
import matplotlib.pyplot as plt


class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, from_, to, ranges_and_increments, unit):
        super().__init__(master)

        self.ranges_and_increments = self.process_ranges_and_increments(ranges_and_increments)
        self.label = customtkinter.CTkLabel(self, text=title)
        self.label.pack(side='left', padx=5)

        self.value_var = tkinter.DoubleVar()  # Create a DoubleVar
        self.value_var.set(from_)  # Set its initial value

        self.slider = customtkinter.CTkSlider(self, from_=from_, to=to, command=self.update_slider_value, variable=self.value_var)
        self.slider.pack(side='left', padx=5)

        self.value_label = customtkinter.CTkLabel(self, textvariable=self.value_var)
        self.value_label.pack(side='left', padx=5)

        self.unit = unit
        self.value_label = customtkinter.CTkLabel(self, text=self.unit)
        self.value_label.pack(side='left', padx=5)

    def update_slider_value(self, value):
        corrected_value = self.variable_increment(value, self.ranges_and_increments)
        formatted_value = "{:.2f}".format(corrected_value)  # Format the value to two decimal places with unit
        self.value_var.set(formatted_value)

    def variable_increment(self, value, rangeAndInc):
        value = int(value)
        for (start, end, increment) in rangeAndInc:
            if start <= value <= end:
                return round((value - start) / increment) * increment + start
        return value

    def process_ranges_and_increments(self, ranges):
        # if ranges is just a single value, then create a list of one tuple
        if isinstance(ranges, (int, float)):
            return [(0, float('inf'), ranges)]
        return ranges

class ParametersWindow(customtkinter.CTkToplevel):
    DEFAULT_VALUES = [60, 120, 120, 150, 3500, 400, 750,  3500, 400, 250, 250 , 320 , 250 , 4, 30 , 8, 5]
    values = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x400")
        self.title("Parameters")
        # Ensure this window always pops up on top
        self.focus()
        self.overall_frame = customtkinter.CTkScrollableFrame(self)
        self.overall_frame.pack(padx=20, pady=20, fill='both', expand=False)
        
        units = ["ppm", "ppm", "ppm", "ms", "µV", "µs", "µV", "µV", "µs", "µV", "ms", "ms", "ms", "", "sec", "", "min"]

        # Define unique slider ranges for each of the 17 variables
        slider_ranges = [
            (30, 175, [(30, 50, 5), (50, 90, 1), (90, 175, 5)]),  #lower rate limit x x 
            (50, 175, 5), # Upper Rate Limit x x 
            (50, 175, 5), # Maximum Sensor Rate x 
            (70, 300, 10), # Fixed AV Delay x
            (500, 7000, [(500, 3200, 100), (3200, 3500, 300), (3500, 7000, 500)]), # Atrial Amplitude   x x 
            (50, 1900, [(50,100,50),(100,1900,100)]),  # Atrial Pulse Width x x 
            (250, 10000, [(250,500,250), (500,750,250), (1000,10000,500)]),  # Atrial Sensitivity x 
            (500, 7000, [(500, 3200, 100), (3200, 3500, 300), (3500, 7000, 500)]),  # Ventricular Amplitude xx
            (50, 1900, [(50,100,50),(100,1900,100)]), # Ventricular Pulse Width x 
            (25000, 1000000, [(250,500,250), (500,750,250), (0,75000,1000,250), (1000,10000,500)]), # Ventricular Sensitivity x 
            (150, 500, 10), # Absolute Refractory Period x  
            (150, 500, 10), # Ventricular Refractory Period x 
            (150, 500, 10), # Post-Ventricular Atrial Refractory Period x 
            (0, 7, 1), # Activity Threshold x 
            (10, 50, 10), # Reaction Time x 
            (1, 16, 1), # Response Factor x
            (2, 16, 1) # Recovery Time x 
        ]

        titles = [
            "Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Fixed AV Delay",
            "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "Ventricular Amplitude",
            "Ventricular Pulse Width", "Ventricular Sensitivity", "Absolute Refractory Period",
            "Ventricular Refractory Period", "Post-Ventricular Atrial Refractory Period", "Activity Threshold",
            "Reaction Time", "Response Factor", "Recovery Time"
        ]

        if not ParametersWindow.values:
           ParametersWindow.values = ParametersWindow.DEFAULT_VALUES

        self.frames = []
        for (title, value, (from_, to_, increment), unit) in zip(titles, self.values, slider_ranges, units):
            frame = InputFrame(self.overall_frame, title, from_, to_, increment, unit)
            frame.slider.set(value)  # Set the slider to the default value
            frame.pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)

        # Save Button
        self.save_button = customtkinter.CTkButton(self, text="Save Options", command=self.save_options, fg_color="#1d3557", hover_color="#457B9D")
        self.save_button.pack(side='left', padx=20, pady=20)

        # Reset to Default Button
        self.reset_button = customtkinter.CTkButton(self, text="Reset to Default", command=self.reset_to_default, fg_color="#1d3557", hover_color="#457B9D")
        self.reset_button.pack(side='right', padx=20, pady=20)

    def save_options(self):
        for i, frame in enumerate(self.frames):
            self.values[i] = frame.slider.get()
        print(self.values)

    def reset_to_default(self):
        ParametersWindow.values = ParametersWindow.DEFAULT_VALUES.copy()  # Reset to default values
        self.update_values()

    def update_values(self):
        for i, frame in enumerate(self.frames):
            frame.slider.set(self.values[i])

    def variable_increment(value, rangeAndInc):
        value = int(value)
        for (start, end, increment) in rangeAndInc:
            if start <= value <= end:
                return round((value - start) / increment) * increment + start
        return value

class App(customtkinter.CTk):
    def __init__(self): #initializes, for all tkinter code, you find replace app with self
        super().__init__()
        self.title('Pacemaker')
        self.geometry('800x400')
        # self.custom_font = customtkinter.CTkFont(family="Calibri", size=14, weight='bold')
        self.create_welcome_screen()
        
    def create_welcome_screen(self):
        self.welcome_frame = customtkinter.CTkFrame(self)
        self.welcome_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.welcome_frame, text='Welcome!').pack(pady=20)
        customtkinter.CTkButton(self.welcome_frame, text='Login', command=self.show_login_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        customtkinter.CTkButton(self.welcome_frame, text='Create an Account', command=self.show_register_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        customtkinter.CTkButton(self.welcome_frame, text='Continue as Guest', command=self.show_main_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)

    def show_login_screen(self):
        self.welcome_frame.pack_forget()
        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.login_frame, text='Login Screen').pack(pady=20)

        # Entry for username
        customtkinter.CTkLabel(self.login_frame, text='Username').pack()
        self.username_entry = customtkinter.CTkEntry(self.login_frame)
        self.username_entry.pack(pady=10)

        # Entry for password
        customtkinter.CTkLabel(self.login_frame, text='Password').pack()
        self.password_entry = customtkinter.CTkEntry(self.login_frame, show="*")  # Password entry
        self.password_entry.pack(pady=10)

        # Login Button
        customtkinter.CTkButton(self.login_frame, text='Login', command=self.login, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        customtkinter.CTkButton(self.login_frame, text='Back', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
    
    def show_register_screen(self):
        self.welcome_frame.pack_forget()
        self.register_frame = customtkinter.CTkFrame(self)
        self.register_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.register_frame, text='Create Account Screen').pack(pady=20)

        # Entry for username
        customtkinter.CTkLabel(self.register_frame, text='Username').pack()
        self.create_username_entry = customtkinter.CTkEntry(self.register_frame)
        self.create_username_entry.pack(pady=10)

        # Entry for password
        customtkinter.CTkLabel(self.register_frame, text='Password').pack()
        self.create_password_entry = customtkinter.CTkEntry(self.register_frame, show="*")  # Password entry
        self.create_password_entry.pack(pady=10)

        # Entry for password re-entry
        customtkinter.CTkLabel(self.register_frame, text='Re-Type Password').pack()
        self.create_password_check = customtkinter.CTkEntry(self.register_frame, show="*")  # Password check
        self.create_password_check.pack(pady=10)

        # Register Button
        customtkinter.CTkButton(self.register_frame, text='Register', command=self.register, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        customtkinter.CTkButton(self.register_frame, text='Back', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)

    def register(self):
        username = self.create_username_entry.get()
        password = self.create_password_entry.get()
        password_check = self.create_password_check.get()

        # Check if the number of accounts exceeds 10
        if len(self.get_user_list()) >= 10:
            error_message = "Error: Maximum number of accounts reached."
            print(error_message)
            # self.show_error_message(error_message)
            return

        # Check if the username already exists
        if self.username_exists(username):
            error_message = f"Error: Username '{username}' already exists. Choose a different username."
            print(error_message)
            # self.show_error_message(error_message)
            return

        # Check if the entered password matches the password check
        if password != password_check:
            error_message = "Error: Passwords do not match. Please re-enter your password."
            print(error_message)
            # self.show_error_message(error_message)
            return

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Save the username and hashed password to the file
        with open("user_accounts.txt", "a") as file:
            file.write(f"{username}:{hashed_password}\n")

        success_message = f"Registered: Username - {username}"
        print(success_message)
        #self.show_info_message(success_message)
        self.show_main_screen()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hash the entered password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Check if the file exists, if not, create it
        if not os.path.exists("user_accounts.txt"):
            open("user_accounts.txt", "w").close()

        # Check if the provided username and hashed password match any record in the file
        user_list = self.get_user_list()
        for user in user_list:
            stored_username, stored_hashed_password = user.split(":")
            if username == stored_username and hashed_password == stored_hashed_password:
                success_message = f"Logged in: Username - {username}"
                print(success_message)
                self.show_main_screen()
                return

        error_message = "Login failed: Invalid username or password."
        print(error_message)
        self.show_error_message(error_message)

    def show_error_message(self, message):
        # Display error message to the user *** NOT DONE ***
        print(f"Error: {message}")

    def show_info_message(self, message):
        # Display info message to the user *** NOT DONE ***
        print(f"Info: {message}")

    def get_user_list(self):
        # Check if the file exists, if not, return an empty list
        if not os.path.exists("user_accounts.txt"):
            return []

        try:
            with open("user_accounts.txt", "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []
    
    def username_exists(self, username):
        user_list = self.get_user_list()
        return any(user.split(":")[0] == username for user in user_list)

    def back_to_welcome(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.create_welcome_screen()
    
    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)

    def show_main_screen(self):
        for widget in self.winfo_children():
            widget.pack_forget()

        self.main_frame = customtkinter.CTkFrame(self)  
        self.main_frame.pack(fill='both', expand=True)

        self.nav_bar = customtkinter.CTkFrame(self.main_frame)
        self.nav_bar.pack(fill='x')
        customtkinter.CTkButton(self.nav_bar, text='Sign Out', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        customtkinter.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        self.optionmenu_var = customtkinter.StringVar(value="Select Pacing Mode")
        self.optionmenu = customtkinter.CTkOptionMenu(self.nav_bar, values=["AOO", "AAI","VOO","VVI"], command=self.optionmenu_callback, variable=self.optionmenu_var)
        self.optionmenu.pack(side="right")

        self.toplevel_window = None

        self.switch_var = customtkinter.StringVar(value="on")
        self.switch = customtkinter.CTkSwitch(self.nav_bar, text="🌙", command=self.theme_event, variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.pack(side="left")
        
        self.body_frame = customtkinter.CTkScrollableFrame(self.main_frame)
        self.body_frame.pack(fill='both', expand=True, pady=20)
        customtkinter.CTkLabel(self.body_frame, text='Main Body Content').pack()


        self.footer_frame = customtkinter.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill='x', side='bottom')
        
        customtkinter.CTkButton(self.footer_frame, text='Print Report', command=None, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        customtkinter.CTkLabel(self.footer_frame, text='Heart Murderers Ltd.').pack(side='right', padx=(0,200))  

        self.connection = customtkinter.CTkLabel(self.footer_frame, text="Finding Connection", text_color="#E63946", justify="right").pack(side = 'left') #initial state is not connected
        #self.show_parameters_popup() # makes the paramater popup appear when the main screen is launched

    

    def theme_event(self):
        print("switch toggled, current value:", self.switch_var.get())
        if self.switch_var.get() == "on":
            customtkinter.set_appearance_mode("dark")
            self.switch.configure(text="🌙")
        else: 
            customtkinter.set_appearance_mode("light")
            self.switch.configure(text="☀")       

    def show_parameters_popup(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ParametersWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.update_values()  # Update the values in the window
            self.toplevel_window.focus()  # if window exists focus it



if __name__ == '__main__':
    app = App()
    app.mainloop()  