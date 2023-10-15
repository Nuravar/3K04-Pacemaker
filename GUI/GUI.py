import os
import customtkinter
import hashlib

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        # Label
        self.label = customtkinter.CTkLabel(self, text=title)
        self.label.pack(side='left', padx=5)

        # Entry
        self.entry = customtkinter.CTkEntry(self)
        self.entry.pack(side='left', padx=5)


class ParametersWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x400")

        self.overall_frame = customtkinter.CTkScrollableFrame(self)
        self.overall_frame.pack(padx=20, pady=20, fill='both', expand=False)

        titles = [
            "Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Fixed AV Delay",
            "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "Ventricular Amplitude",
            "Ventricular Pulse Width", "Ventricular Sensitivity", "Absolute Refractory Period",
            "Ventricular Refractory Period", "Post-Ventricular Atrial Refractory Period", "Activity Threshold",
            "Reaction Time", "Response Factor", "Recovery Time"
        ]

        max_length = max(map(len, titles))
        self.frames = []
        for title in titles:
            frame = InputFrame(self.overall_frame, title.ljust(max_length)).pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)

        # Save Button
        self.save_button = customtkinter.CTkButton(self, text="Save Options", command=self.save_options, fg_color="#1d3557", hover_color="#457B9D")
        self.save_button.pack(padx=20, pady=20)

    def save_options(self):
        values = [frame.entry.get() for frame in self.frames]
        print(values)

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
        self.username_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        # Entry for password
        self.password_entry = customtkinter.CTkEntry(self.login_frame, placeholder_text="Password", show="*")  # Password entry
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
        self.create_username_entry = customtkinter.CTkEntry(self.register_frame, placeholder_text="Username")
        self.create_username_entry.pack(pady=10)

        # Entry for password
        self.create_password_entry = customtkinter.CTkEntry(self.register_frame, placeholder_text="Password", show="*")  # Password entry
        self.create_password_entry.pack(pady=10)

        # Entry for password re-entry
        self.create_password_check = customtkinter.CTkEntry(self.register_frame, placeholder_text="Re-Type Password", show="*")  # Password check
        self.create_password_check.pack(pady=10)

        # Register Button
        customtkinter.CTkButton(self.register_frame, text='Register', command=self.register, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        customtkinter.CTkButton(self.register_frame, text='Back', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)


    def back_to_welcome(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.create_welcome_screen()

    def show_main_screen(self):
        for widget in self.winfo_children():
            widget.pack_forget()

        self.main_frame = customtkinter.CTkFrame(self)  
        self.main_frame.pack(fill='both', expand=True)

        self.nav_bar = customtkinter.CTkFrame(self.main_frame)
        self.nav_bar.pack(fill='x')
        customtkinter.CTkButton(self.nav_bar, text='Sign Out', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        customtkinter.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        self.toplevel_window = None

        self.switch_var = customtkinter.StringVar(value="on")
        self.switch = customtkinter.CTkSwitch(self.nav_bar, text="🌙", command=self.theme_event, variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.pack(side="left")
        
        self.body_frame = customtkinter.CTkScrollableFrame(self.main_frame)
        self.body_frame.pack(fill='both', expand=True, pady=20)
        customtkinter.CTkLabel(self.body_frame, text='Main Body Content').pack()

        self.footer_frame = customtkinter.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill='x', side='bottom')
        customtkinter.CTkLabel(self.footer_frame, text='Footer Content').pack()

        self.connection = customtkinter.CTkLabel(self.footer_frame, text="Finding Connection", text_color="#E63946", justify="right").pack(side = 'right') #initial state is not connected
        self.show_parameters_popup()


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
            self.toplevel_window.focus()  # if window exists focus it

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

if __name__ == '__main__':
    app = App()
    app.mainloop()  