import os
import customtkinter as ctk
import hashlib
#import numpy as np
#import matplotlib.pyplot as plt

# The code provides an interface to adjust and save parameters for a pacemaker.
# It also provides a user login and registration system.

class InputFrame(ctk.CTkFrame):
    def __init__(self, master, title, from_, to, ranges_and_increments, unit):
        # This is a custom frame containing a label, slider and value label.
        super().__init__(master)
        # Create and pack the label showing the title
        self.ranges_and_increments = self.process_ranges_and_increments(ranges_and_increments)
        self.label = ctk.CTkLabel(self, text=title)
        self.label.pack(side='left', padx=5)
        # Set up variable for holding the slider's value
        self.value_var = ctk.DoubleVar()  # Create a DoubleVar
        self.value_var.set(from_)  # Set its initial value
        # Create and pack the slider
        self.slider = ctk.CTkSlider(self, from_=from_, to=to, command=self.update_slider_value, variable=self.value_var)
        self.slider.pack(side='left', padx=5)
        # Label that shows the current value of the slider
        self.value_label = ctk.CTkLabel(self, textvariable=self.value_var)
        self.value_label.pack(side='left', padx=5)
        # Label that shows the unit of the value
        self.unit = unit
        self.value_label = ctk.CTkLabel(self, text=self.unit)
        self.value_label.pack(side='left', padx=5)

    def update_slider_value(self, value):
        # Adjust the slider's value to increments and format it
        corrected_value = self.variable_increment(value, self.ranges_and_increments)
        formatted_value = "{:.2f}".format(corrected_value)  # Format the value to two decimal places with unit
        self.value_var.set(formatted_value)

    def variable_increment(self, value, rangeAndInc):
        # Adjust the slider's value to the closest increment
        value = int(value)
        for (start, end, increment) in rangeAndInc:
            if start <= value <= end:
                return round((value - start) / increment) * increment + start
        return value

    def process_ranges_and_increments(self, ranges):
        # If a single value is provided, use it as the increment and set no limit
        # if ranges is just a single value, then create a list of one tuple
        if isinstance(ranges, (int, float)):
            return [(0, float('inf'), ranges)]
        return ranges

class MessageWindow(ctk.CTkToplevel):
    # This creates a simple message window with a given title and message.
    def __init__(self, title, msg):
        super().__init__()
        self.geometry("400x100")

        self.title(title)
        self.msg = ctk.CTkLabel(self, text=msg).pack(padx=20, pady=20)
      
class ParametersWindow(ctk.CTkToplevel):
    # This window allows users to adjust pacemaker parameters with sliders.
    DEFAULT_VALUES = [60, 120, 120, 150, 3500, 400, 750,  3500, 400, 250, 250 , 320 , 250 , 4, 30 , 8, 5]
    values = []

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.geometry("600x400")
        self.title("Parameters")
        self.focus() # Put the frame on top
        # Create a scrollable frame
        self.overall_frame = ctk.CTkScrollableFrame(self)
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
        # Populate the parameters window with sliders
        if not ParametersWindow.values:
           ParametersWindow.values = ParametersWindow.DEFAULT_VALUES

        self.frames = []
        for (title, value, (from_, to_, increment), unit) in zip(titles, self.values, slider_ranges, units):
            frame = InputFrame(self.overall_frame, title, from_, to_, increment, unit)
            frame.slider.set(value)  # Set the slider to the default value
            frame.pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)
        # Buttons to save changes or reset to default
        # Save Button
        self.save_button = ctk.CTkButton(self, text="Save Options", command=self.save_options, fg_color="#1d3557", hover_color="#457B9D")
        self.save_button.pack(side='left', padx=20, pady=20)

        # Reset to Default Button
        self.reset_button = ctk.CTkButton(self, text="Reset to Default", command=self.reset_to_default, fg_color="#1d3557", hover_color="#457B9D")
        self.reset_button.pack(side='right', padx=20, pady=20)

    def get_user_list(self):
        # Reads the file with users, returns a list of user lines
            # Check if the file exists, if not, return an empty list
            if not os.path.exists("user_accounts.txt"):
                return []

            try:
                with open("user_accounts.txt", "r") as file:
                    return [line.strip() for line in file.readlines()]
            except FileNotFoundError:
                return []

    def reset_to_default(self):
        # Reset the sliders to their default values
        ParametersWindow.values = ParametersWindow.DEFAULT_VALUES.copy()  # Reset to default values in memory
        self.update_values()
        self.save_options()  # Save the default values back to the file

    def update_values(self):
        for i, frame in enumerate(self.frames):
            frame.slider.set(ParametersWindow.values[i])

    def save_options(self):
        # Check if a user is logged in
        if not self.app.current_username:
            print("No user logged in.")
            return

        # Update self.values with current slider values
        self.values = [int(frame.slider.get()) for frame in self.frames]

        # Read the existing user list from the file
        user_list = self.get_user_list()

        # Find the user entry for the currently logged-in user
        for i, user_entry in enumerate(user_list):
            username, hashed_password, _ = user_entry.split(":")
            if self.app.current_username == username:
                # Update the encoded parameters directly
                user_list[i] = f"{username}:{hashed_password}:{','.join(map(str, self.values))}"
                break

        # Write the updated user list back to the file
        with open("user_accounts.txt", "w") as file:
            file.write(','.join(user_list) + "\n")

        print(f"Saved options for user {self.app.current_username}")


    def variable_increment(value, rangeAndInc):
        value = int(value)
        for (start, end, increment) in rangeAndInc:
            if start <= value <= end:
                return round((value - start) / increment) * increment + start
        return value

class App(ctk.CTk):
    def __init__(self): #initializes, for all tkinter code, you find replace app with self
        super().__init__()
        self.title('Pacemaker')
        self.geometry('800x400')
        # self.custom_font = ctk.CTkFont(family="Calibri", size=14, weight='bold')
        self.msg_window = None
        self.current_username = None  # Initialize the current_username variable
        self.create_welcome_screen()
        
    def create_welcome_screen(self):
        self.welcome_frame = ctk.CTkFrame(self)
        self.welcome_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.welcome_frame, text='Welcome!').pack(pady=20)
        ctk.CTkButton(self.welcome_frame, text='Login', command=self.show_login_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        ctk.CTkButton(self.welcome_frame, text='Create an Account', command=self.show_register_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        ctk.CTkButton(self.welcome_frame, text='Continue as Guest', command=self.show_main_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)

    def show_login_screen(self):
        self.welcome_frame.pack_forget()
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.login_frame, text='Login').pack(pady=20)

        # Entry for username
        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        # Entry for password
        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")  # Password entry
        self.password_entry.pack(pady=10)

        # Login Button
        ctk.CTkButton(self.login_frame, text='Login', command=self.login, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        ctk.CTkButton(self.login_frame, text='Back', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)

    def show_register_screen(self):
        self.welcome_frame.pack_forget()
        self.register_frame = ctk.CTkFrame(self)
        self.register_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.register_frame, text='Create Account').pack(pady=20)

        # Entry for username
        self.create_username_entry = ctk.CTkEntry(self.register_frame, placeholder_text="Username")
        self.create_username_entry.pack(pady=10)

        # Entry for password
        self.create_password_entry = ctk.CTkEntry(self.register_frame, placeholder_text="Password", show="*")  # Password entry
        self.create_password_entry.pack(pady=10)

        # Entry for password re-entry
        self.create_password_check = ctk.CTkEntry(self.register_frame, placeholder_text="Re-Type Password", show="*")  # Password check
        self.create_password_check.pack(pady=10)

        # Register Button
        ctk.CTkButton(self.register_frame, text='Register', command=self.register, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        ctk.CTkButton(self.register_frame, text='Back', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)

    def register(self):
        username = self.create_username_entry.get()
        password = self.create_password_entry.get()
        password_check = self.create_password_check.get()

        # Check if the number of accounts exceeds 10
        if len(self.get_user_list()) >= 10:
            error_message = "Maximum number of accounts reached."
            self.show_message("Accounts Error", error_message)
            return

        # Check if the username already exists
        if self.username_exists(username):
            error_message = f"Username '{username}' already exists. Choose a different username."
            self.show_message("Username Error", error_message)
            return

        # Check if the entered password matches the password check
        if password != password_check:
            error_message = "Passwords do not match. Please re-enter your password."
            self.show_message("Password Error", error_message)
            return

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Save the username and hashed password to the file
        with open("user_accounts.txt", "a") as file:
            file.write(f"{username}:{hashed_password}:{','.join(map(str, ParametersWindow.DEFAULT_VALUES))}\n")

        print(f"Registered: Username - {username}")

        # Set the current_username after registration
        self.current_username = username

        # Continue with the main screen display
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
        for user_entry in user_list:
            stored_username, stored_hashed_password, _ = user_entry.split(":")
            if username == stored_username and hashed_password == stored_hashed_password:
                print(f"Logged in: Username - {username}")

                # Set the current_username variable
                self.current_username = username

                # Continue with the rest of the login process
                self.show_main_screen()

                # Create an instance of ParametersWindow after showing the main screen
                self.toplevel_window = ParametersWindow(self, self)
                self.toplevel_window.values = list(map(int, _.split(',')))  # Replace _ with the appropriate variable
                self.toplevel_window.update_values()

                # Focus on the ParametersWindow after the main screen is displayed
                self.toplevel_window.focus()

                return

        error_message = "Login failed: Invalid username or password."
        self.show_message("Login Error", error_message)

    def show_message(self, title, msg):
        if self.msg_window is None or not self.msg_window.winfo_exists():
            self.msg_window = MessageWindow(title, msg)  # create window if its None or destroyed
        else:
            self.msg_window.focus()  # if window exists focus it
        print(msg)

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

        self.main_frame = ctk.CTkFrame(self)  
        self.main_frame.pack(fill='both', expand=True)

        self.nav_bar = ctk.CTkFrame(self.main_frame)
        self.nav_bar.pack(fill='x')
        ctk.CTkButton(self.nav_bar, text='Sign Out', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        ctk.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        self.optionmenu_var = ctk.StringVar(value="Select Pacing Mode")
        self.optionmenu = ctk.CTkOptionMenu(self.nav_bar, values=["AOO", "AAI","VOO","VVI"], command=self.optionmenu_callback, variable=self.optionmenu_var)
        self.optionmenu.pack(side="right")
        ctk.CTkButton(self.nav_bar, text='⏸ Stop', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        ctk.CTkButton(self.nav_bar, text='▶ Run', command=self.show_parameters_popup, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')

        self.toplevel_window = None

        self.switch_var = ctk.StringVar(value="on")
        self.switch = ctk.CTkSwitch(self.nav_bar, text="🌙", command=self.theme_event, variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.pack(side="left")
        
        self.body_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.body_frame.pack(fill='both', expand=True, pady=20)
        ctk.CTkLabel(self.body_frame, text='Main Body Content').pack()


        self.footer_frame = ctk.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill='x', side='bottom')
        
        ctk.CTkButton(self.footer_frame, text='Print Report', command=None, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        ctk.CTkLabel(self.footer_frame, text='Pacemaker Controller').pack(side='right', padx=(0,200))
        
        self.connection = ctk.CTkLabel(self.footer_frame, text="Finding Connection", text_color="#E63946", justify="right").pack(side = 'left', padx=5) #initial state is not connected
        #self.show_parameters_popup() # makes the paramater popup appear when the main screen is launched

    

    def theme_event(self):
        print("switch toggled, current value:", self.switch_var.get())
        if self.switch_var.get() == "on":
            ctk.set_appearance_mode("dark")
            self.switch.configure(text="🌙")
        else: 
            ctk.set_appearance_mode("light")
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
