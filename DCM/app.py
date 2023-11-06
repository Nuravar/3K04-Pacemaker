import customtkinter as ctk
import os
import hashlib
from PIL import Image
from message_window import MessageWindow
from parameters_window import ParametersWindow
from datetime import datetime

ctk.set_default_color_theme("DCM/Themes/cNord_theme.json")
ctk.set_appearance_mode("system")


class App(ctk.CTk):
    def __init__(self): # initializes, for all tkinter code, you find replace app with self
        super().__init__()
        self.title('Pacemaker')
        self.geometry('1200x800')
        self.HEIGHT = App.winfo_screenheight(self)
        self.WIDTH = App.winfo_screenwidth(self)
        # self.custom_font = ctk.CTkFont(family="Calibri", size=14, weight='bold')
        self.msg_window = None
        self.current_username = None  # Initialize the current_username variable
        self.pacing_mode_selected = None  # Flag to track if pacing mode has been selected
        self.create_welcome_screen()
        self.minsize(1200,800)

    def get_current_size(self):
        self.HEIGHT = App.winfo_screenheight(self)
        self.WIDTH = App.winfo_screenwidth(self)
        print(self.WIDTH,"x", self.HEIGHT)
        return self.WIDTH, self.HEIGHT


    def get_current_time(self):
        # Returns the current system time as a formatted string
        return datetime.now().strftime('%H:%M')

    def update_time(self, label):
        current_time = self.get_current_time()
        label.configure(text=current_time)

        # Schedule the method to run again after 1000ms (1 second)
        self.after(1000, lambda: self.update_time(label))  # Pass the label argument here

 
    def update_theme(self):
        if (ctk.get_appearance_mode() == "Dark"):
            return "☾"
        else:
            return "☀"
    
    def create_welcome_screen(self):
        width, height = self.get_current_size() #utilize this to scale each element as a percentage of size DOES NOT WORK
        self.update_theme()
        self.welcome_frame = ctk.CTkFrame(self)
        self.welcome_frame.pack(fill='both', expand=True)

        self.top_frame = ctk.CTkFrame(self.welcome_frame)
        self.top_frame.pack(fill='x', pady=20, padx=20)

        battery = ctk.CTkImage(light_image=Image.open("DCM/Themes/Battery_light.png"),
                                dark_image=Image.open("DCM/Themes/Battery_dark.png"),
                                size=(30, 30))

        self.battery_label = ctk.CTkLabel(self.top_frame, image=battery, text="")  # display image with a CTkLabel
        self.battery_label.pack(side="left", padx=(65, 10), pady=5)

        self.time_label = ctk.CTkLabel(self.top_frame, text=self.get_current_time())
        self.time_label.pack(side="left", padx=10, pady=10)
        self.update_time(self.time_label)

        self.switch_var = ctk.StringVar(value=ctk.get_appearance_mode())
        self.switch = ctk.CTkButton(self.top_frame, text=self.update_theme(), command=self.theme_event, width=30, height=30)  # 40x40 is just an example size, adjust accordingly
        self.switch.pack(side="right", pady=10, padx=10)

        logo_title = ctk.CTkImage(light_image=Image.open("DCM/Themes/logo.png"),
                                  dark_image=Image.open("DCM/Themes/dark_logo.png"),
                                  size=(70 * 5, 30 * 5))

        self.logo_label = ctk.CTkLabel(self.welcome_frame, image=logo_title, text="")
        self.logo_label.pack(pady=(50, 20))

        ctk.CTkButton(self.welcome_frame, text='Login', command=self.show_login_screen).pack(pady=10, padx=(10, 0))
        ctk.CTkButton(self.welcome_frame, text='Create an Account', command=self.show_register_screen).pack(pady=10, padx=(10, 0))
        ctk.CTkButton(self.welcome_frame, text='Continue as Admin', command=self.create_admin_screen, text_color="#047bda", fg_color="transparent", border_width=0).pack(pady=10, padx=(10, 0))

        waves_title = ctk.CTkImage(light_image=Image.open("DCM/Themes/Wave_light.png"),
                                   dark_image=Image.open("DCM/Themes/Wave.png"),
                                   size=(70 * 27, 33 * 17))

        self.waves_label = ctk.CTkLabel(self.welcome_frame, image=waves_title, text="")
        self.waves_label.pack(pady=(40, 0))

    def show_login_screen(self):
        self.welcome_frame.pack_forget()
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.login_frame, text='Login', font=("Arial", 55, "bold")).pack(pady=(80,20))

        # Entry for username
        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username", height=35, width=160)
        self.username_entry.pack(pady=10)

        # Entry for password
        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", height=35, width=160)  # Password entry
        self.password_entry.pack(pady=10)

        # Login Button
        ctk.CTkButton(self.login_frame, text='Login', command=lambda:self.login("users")).pack(pady=10)
        ctk.CTkButton(self.login_frame, text='Back', command=self.back_to_welcome).pack(pady=10)

        bg_image = ctk.CTkImage(light_image=Image.open("DCM/Themes/wave2_light.png"),
                                  dark_image=Image.open("DCM/Themes/wave2_dark.png"),
                                  size=(70 * 27, 33 * 17))
        self.logo_label = ctk.CTkLabel(self.login_frame, image=bg_image, text="")
        self.logo_label.pack(pady=(70, 0))

    def show_register_screen(self):
        self.welcome_frame.pack_forget()
        self.register_frame = ctk.CTkFrame(self)
        self.register_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.register_frame, text='Register', font=("Arial", 55, "bold")).pack(pady=(80,20))

        # Entry for username
        self.create_username_entry = ctk.CTkEntry(self.register_frame, placeholder_text="Username", height=35, width=160)
        self.create_username_entry.pack(pady=10)

        # Entry for password
        self.create_password_entry = ctk.CTkEntry(self.register_frame, placeholder_text="Password", show="*", height=35, width=160)  # Password entry
        self.create_password_entry.pack(pady=10)

        # Entry for password re-entry
        self.create_password_check = ctk.CTkEntry(self.register_frame, placeholder_text="Re-Type Password", show="*", height=35, width=160)  # Password check
        self.create_password_check.pack(pady=10)

        # Register Button
        ctk.CTkButton(self.register_frame, text='Register', command=self.register).pack(pady=10)
        ctk.CTkButton(self.register_frame, text='Back', command=self.back_to_welcome).pack(pady=10)

        bg_image = ctk.CTkImage(light_image=Image.open("DCM/Themes/wave2_light.png"),
                                  dark_image=Image.open("DCM/Themes/wave2_dark.png"),
                                  size=(70 * 27, 33 * 17))
        self.logo_label = ctk.CTkLabel(self.register_frame, image=bg_image, text="")
        self.logo_label.pack(pady=(70, 0))

    def register(self):
        username = self.create_username_entry.get()
        password = self.create_password_entry.get()
        password_check = self.create_password_check.get()

        print(not password and not password_check)

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
        if password != password_check or not password and not password_check:
            error_message = "Passwords do not match or are empty.\nPlease re-enter your password."
            self.show_message("Password Error", error_message)
            return

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Save the username and hashed password to the file
        with open("user_accounts.txt", "a") as file:
            file.write(f"{username}:{hashed_password}:{','.join(map(str, [str(value) for value in ParametersWindow.DEFAULT_VALUES]))}\n")

        print(f"Registered: Username - {username}")

        # Set the current_username after registration
        self.current_username = username

        # Continue with the main screen display
        self.show_main_screen()

    def login(self, type):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hash the entered password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if (type == "admin"):
            print("in admin")
            filename = "admin_accounts.txt"
        else:
            filename = "user_accounts.txt"

        # Check if the file exists, if not, create it
        if not os.path.exists(filename):
            open(filename, "w").close()

        # Check if the provided username and hashed password match any record in the file
        user_list = self.get_user_list(type)
        for user_entry in user_list:
            stored_username, stored_hashed_password, saved_parameters = user_entry.split(":")
            if username == stored_username and hashed_password == stored_hashed_password:
                print(f"Logged in: Username - {username}")

                # Set the current_username variable
                self.current_username = username

                # Continue with the rest of the login process
                if (type == "admin"):
                    self.show_deletion_screen()
                else: 
                    self.show_main_screen()
                return

        error_message = "Login failed: Invalid username or password."
        self.show_message("Login Error", error_message)

    def show_message(self, title, msg):
        if self.msg_window is None or not self.msg_window.winfo_exists():
            self.msg_window = MessageWindow(title, msg)  # create window if its None or destroyed
        else:
            self.msg_window.focus()  # if window exists focus it
        print(msg)

    def get_user_list(self, type):
        # Check if the file exists, if not, return an empty list
        if (type == "admin"):
            filename = "admin_accounts.txt"
        else: 
            filename = "user_accounts.txt"

        if not os.path.exists(filename):
            return []

        try:
            with open(filename, "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    def username_exists(self, username):
        user_list = self.get_user_list()
        return any(user.split(":")[0] == username for user in user_list)

    def back_to_welcome(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.pacing_mode_selected = None  # Reset the flag
        self.create_welcome_screen()

    def create_admin_screen(self):
        self.welcome_frame.pack_forget()
        self.admin_frame = ctk.CTkFrame(self)
        self.admin_frame.pack(fill='both', expand=True)  
        ctk.CTkLabel(self.admin_frame, text='Admin Login', font=("Arial", 55, "bold")).pack(pady=(80,20))

        self.username_entry = ctk.CTkEntry(self.admin_frame, placeholder_text="Admin Username")
        self.username_entry.pack(pady=10)

        # Entry for password
        self.password_entry = ctk.CTkEntry(self.admin_frame, placeholder_text="Password", show="*")  # Password entry
        self.password_entry.pack(pady=10)
        ctk.CTkButton(self.admin_frame, text='Login', command=lambda:self.login("admin")).pack(pady=10)
        ctk.CTkButton(self.admin_frame, text='Back', command=self.back_to_welcome).pack(pady=10)

        bg_image = ctk.CTkImage(light_image=Image.open("DCM/Themes/wave2_light.png"),
                                  dark_image=Image.open("DCM/Themes/wave2_dark.png"),
                                  size=(70 * 27, 33 * 17))
        self.logo_label = ctk.CTkLabel(self.admin_frame, image=bg_image, text="")
        self.logo_label.pack(pady=(70, 0))

    def back_to_admin(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.pacing_mode_selected = None  # Reset the flag
        self.create_admin_screen()

    def show_deletion_screen(self):
        self.admin_frame.pack_forget()
        self.deletion_frame = ctk.CTkFrame(self)
        self.deletion_frame.pack(fill='both', expand=True)  

        userList = self.get_user_list("user")
        ctk.CTkButton(self.deletion_frame, text='Back', command=self.back_to_admin).pack(pady=10)

    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get())

    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)
        self.pacing_mode_selected = choice != "Select Pacing Mode"

        # Update the "⚙ Options" button state based on the pacing mode selection
        if self.pacing_mode_selected:
            self.options_button.configure(state='normal')
        else:
            self.options_button.configure(state='disabled')


    def show_main_screen(self):
        for widget in self.winfo_children():
            widget.pack_forget()

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        self.nav_bar = ctk.CTkFrame(self.main_frame)
        self.nav_bar.pack(fill='x', padx=10, pady=10)

        self.switch_var = ctk.StringVar(value=ctk.get_appearance_mode())
        self.switch = ctk.CTkButton(self.nav_bar, text=self.update_theme(), command=self.theme_event, width=30, height=30)
        self.switch.pack(side="right", pady=10, padx=10)

        ctk.CTkButton(self.nav_bar, text='Sign Out', command=self.back_to_welcome).pack(side='right', padx=10)
        

        # Create the "⚙ Options" button initially disabled
        print(self.pacing_mode_selected)
        if self.pacing_mode_selected is not None:
            print("HERE")
            self.options_button = ctk.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, state='normal')
            self.options_button.pack(side='right', padx=10)
        else:
            print("THERE")
            self.options_button = ctk.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, state='disabled')
            self.options_button.pack(side='right', padx=10)

        self.optionmenu_var = ctk.StringVar(value="Select Pacing Mode")
        self.optionmenu = ctk.CTkOptionMenu(self.nav_bar, values=["AOO", "AAI", "VOO", "VVI"], command=self.optionmenu_callback, variable=self.optionmenu_var)
        self.optionmenu.pack(side="right", padx=10)
        ctk.CTkButton(self.nav_bar, text='⏸ Stop').pack(side='right', padx=10)
        ctk.CTkButton(self.nav_bar, text='▶ Run').pack(side='right', padx=10)

        my_image = ctk.CTkImage(light_image=Image.open("DCM/Themes/logo.png"),
                                dark_image=Image.open("DCM/Themes/dark_logo.png"),
                                size=(70, 30))

        self.image_label = ctk.CTkLabel(self.nav_bar, image=my_image, text="")
        self.image_label.pack(side="left", padx=(10, 10), pady=5)

        self.toplevel_window = None

        self.body_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.body_frame.pack(fill='both', expand=True, pady=20)
        ctk.CTkLabel(self.body_frame, text='Main Body Content').pack()

        self.footer_frame = ctk.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill='x', side='bottom', pady=10, padx=10)

        ctk.CTkButton(self.footer_frame, text='Print Report', command=None).pack(side='right', pady=10, padx=10)
        ctk.CTkLabel(self.footer_frame, text='Pacemaker Controller').pack(side='right', padx=(0, 200))

        self.connection = ctk.CTkLabel(self.footer_frame, text="Finding Connection", text_color="#BF616A").pack(side='left', padx=10)

    def theme_event(self):
        print("Button clicked, current value:", ctk.get_appearance_mode())
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("dark")
            self.switch.configure(text="☾")
            self.switch_var.set("dark")
        else:
            ctk.set_appearance_mode("light")
            self.switch.configure(text="☀")
            self.switch_var.set("light")

    def show_parameters_popup(self):
        if not self.pacing_mode_selected:
            return  # Do not show the Parameters Window if pacing mode hasn't been selected

        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ParametersWindow(self)
        else:
            self.toplevel_window.update_values()
            self.toplevel_window.focus()

if __name__ == '__main__':
    app = App()
    app.mainloop()
