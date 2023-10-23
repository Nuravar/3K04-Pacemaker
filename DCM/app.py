import customtkinter as ctk
import os
import hashlib

# ... (Copy the App class code from the original GUI.py)
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

        ctk.CTkLabel(self.welcome_frame, text='PACE++').pack(pady=20)
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
            stored_username, stored_hashed_password, saved_parameters = user_entry.split(":")
            if username == stored_username and hashed_password == stored_hashed_password:
                print(f"Logged in: Username - {username}")

                # Set the current_username variable
                self.current_username = username

                # Continue with the rest of the login process
                self.show_main_screen()

                # Create an instance of ParametersWindow after showing the main screen
                self.toplevel_window = ParametersWindow(self, self)
                self.toplevel_window.values = list(map(int, saved_parameters.split(',')))  
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
        ctk.CTkButton(self.nav_bar, text='⏸ Stop', fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        ctk.CTkButton(self.nav_bar, text='▶ Run', fg_color="#1d3557", hover_color="#457B9D").pack(side='right')

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