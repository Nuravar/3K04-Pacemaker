import customtkinter as ctk
import os
import hashlib
from PIL import Image
from message_window import MessageWindow
from parameters_window import ParametersWindow
from datetime import datetime
from encryption import generate_encryption_key, encrypt_data, decrypt_data
from base64 import urlsafe_b64encode
import json
import platform
from simulink_serial import *
if platform.system() == "Darwin": # if user is MacOS
    FILE_PATH_PREFIX = "../DCM"
else: # if user is Windows
    FILE_PATH_PREFIX = "DCM"
cNord_theme_path = os.path.join(FILE_PATH_PREFIX,"Themes", "cNord_theme.json")
ctk.set_default_color_theme(cNord_theme_path)
ctk.set_appearance_mode("system")
from simulink_serial import SerialApp

class App(ctk.CTk):
    def __init__(self): # initializes, for all tkinter code, you find replace app with self
        super().__init__()
        self.title('Pacemaker')
        self.geometry('1200x800')
        self.HEIGHT = App.winfo_screenheight(self)
        self.WIDTH = App.winfo_screenwidth(self)
        self.serial_app = SerialApp()
        # Retrieve or generate the encryption key
        key_from_env = os.environ.get("ENCRYPTION_KEY")
        if key_from_env:
            self.encryption_key = key_from_env.encode()
        else:
            self.encryption_key = generate_encryption_key()

        # self.custom_font = ctk.CTkFont(family="Calibri", size=14, weight='bold')
        self.msg_window = None
        self.current_username = None  # Initialize the current_username variable
        self.is_pacing_mode_selected = None  # Flag to track if pacing mode has been selected
        self.toplevel_window = None
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
        self.update_theme()
        self.welcome_frame = ctk.CTkFrame(self)
        self.welcome_frame.pack(fill='both', expand=True)

        self.top_frame = ctk.CTkFrame(self.welcome_frame)
        self.top_frame.pack(fill='x', pady=20, padx=20)

        battery_light_path = os.path.join(FILE_PATH_PREFIX,"Themes", "Battery_light.png")
        battery_dark_path = os.path.join(FILE_PATH_PREFIX,"Themes", "Battery_dark.png")

        battery = ctk.CTkImage(light_image=Image.open(battery_light_path),
                                dark_image=Image.open(battery_dark_path),
                                size=(30, 30))

        self.battery_label = ctk.CTkLabel(self.top_frame, image=battery, text="")  # display image with a CTkLabel
        self.battery_label.pack(side="left", padx=(65, 10), pady=5)

        self.time_label = ctk.CTkLabel(self.top_frame, text=self.get_current_time())
        self.time_label.pack(side="left", padx=10, pady=10)
        self.update_time(self.time_label)

        self.switch_var = ctk.StringVar(value=ctk.get_appearance_mode())
        self.switch = ctk.CTkButton(self.top_frame, text=self.update_theme(), command=self.theme_event, width=30, height=30)  # 40x40 is just an example size, adjust accordingly
        self.switch.pack(side="right", pady=10, padx=10)

        logo_light_path = os.path.join(FILE_PATH_PREFIX,"Themes", "logo.png")
        logo_dark_path = os.path.join(FILE_PATH_PREFIX,"Themes", "dark_logo.png")

        logo_title = ctk.CTkImage(light_image=Image.open(logo_light_path),
                                  dark_image=Image.open(logo_dark_path),
                                  size=(70 * 5, 30 * 5))

        self.logo_label = ctk.CTkLabel(self.welcome_frame, image=logo_title, text="")
        self.logo_label.pack(pady=(50, 20))

        ctk.CTkButton(self.welcome_frame, text='Login', command=self.show_login_screen).pack(pady=10, padx=(10, 0))
        ctk.CTkButton(self.welcome_frame, text='Create an Account', command=self.show_register_screen).pack(pady=10, padx=(10, 0))
        ctk.CTkButton(self.welcome_frame, text='Continue as Admin', command=self.create_admin_screen, text_color="#047bda", fg_color="transparent", border_width=0).pack(pady=10, padx=(10, 0))

        wave_light_path = os.path.join(FILE_PATH_PREFIX,"Themes", "Wave_light.png")
        wave_dark_path = os.path.join(FILE_PATH_PREFIX,"Themes", "Wave.png")
        waves_title = ctk.CTkImage(light_image=Image.open(wave_light_path),
                                   dark_image=Image.open(wave_dark_path),
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
        
        bg_light_path = os.path.join(FILE_PATH_PREFIX,"Themes", "wave2_light.png")
        bg_dark_path = os.path.join(FILE_PATH_PREFIX,"Themes", "wave2_dark.png")
        bg_image = ctk.CTkImage(light_image=Image.open(bg_light_path),
                                  dark_image=Image.open(bg_dark_path),
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

        bg_light_path = os.path.join(FILE_PATH_PREFIX,"Themes", "wave2_light.png")
        bg_dark_path = os.path.join(FILE_PATH_PREFIX,"Themes", "wave2_dark.png")
        bg_image = ctk.CTkImage(light_image=Image.open(bg_light_path),
                                  dark_image=Image.open(bg_dark_path),
                                  size=(70 * 27, 33 * 17))
        self.logo_label = ctk.CTkLabel(self.register_frame, image=bg_image, text="")
        self.logo_label.pack(pady=(70, 0))

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
        if password != password_check or not password and not password_check:
            error_message = "Passwords do not match or are empty.\nPlease re-enter your password."
            self.show_message("Password Error", error_message)
            return

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "pacing_modes.json")

        # Load pacing modes from the pacing_modes.json file
        with open(file_path, "r") as file:
            pacing_data = json.load(file)

        # Extract pacing modes from the loaded data
        pacing_modes = list(pacing_data.keys())

        # Initialize the "Saved Parameters" dictionary with empty lists for each pacing mode
        saved_parameters = {mode: {} for mode in pacing_modes}

        # Create the user entry in the desired JSON format
        user_entry = {
            "Username": username,
            "Password": hashed_password,
            "Saved Parameters": saved_parameters
        }

        script_dir = os.path.dirname(os.path.abspath(__file__))
        user_file_path = os.path.join(script_dir, "user_accounts.json")
        # Load existing data or create an empty dictionary
        try:
            with open(user_file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"Users": []}

        # Add the new user entry to the Users list
        data["Users"].append(user_entry)

        # Save the updated data to the file
        with open(user_file_path, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Registered: Username - {username}")

        # Set the current_username after registration
        self.current_username = username

        # Continue with the main screen display
        self.show_main_screen()

    def login(self, account_type):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hash the entered password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Set the correct file path for user_accounts.json
        script_dir = os.path.dirname(os.path.abspath(__file__))
        user_file_path = os.path.join(script_dir, "user_accounts.json")

        # Check if the file exists
        if not os.path.exists(user_file_path):
            error_message = f"Login failed: {account_type.capitalize()} account file not found."
            self.show_message("Login Error", error_message)
            return

        # Read user accounts from the file
        try:
            with open(user_file_path, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            error_message = f"Login failed: Error decoding {account_type.capitalize()} account file."
            self.show_message("Login Error", error_message)
            return
        except FileNotFoundError:
            error_message = "Login failed: User accounts file not found."
            self.show_message("Login Error", error_message)
            return

        # Set user type
        usertype = "Admin" if account_type == "admin" else "Users"

        # Check if the provided username and password match any record in the file
        for user_entry in data.get(usertype, []):
            if username == user_entry.get("Username") and hashed_password == user_entry.get("Password"):
                self.current_username = username
                # Continue with the rest of the login process
                if account_type == "admin":
                    self.show_deletion_screen()
                else:
                    self.show_main_screen()
                return

        error_message = "Login failed: Invalid username or password."
        self.show_message("Login Error", error_message)

    def show_message(self, title, msg):
        if self.msg_window is None or not self.msg_window.winfo_exists():
            self.msg_window = MessageWindow(title, msg)  # create window    if its None or destroyed
        else:
            self.msg_window.focus()  # if window exists focus it
        print(msg)

    def get_user_list(self):
        # Check if the file exists, if not, return an empty list
        filename = "user_accounts.json"

        if not os.path.exists(filename):
            return []
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        user_file_path = os.path.join(script_dir, "user_accounts.json")
        
        try:
            with open(user_file_path, "r") as file:
                data = json.load(file)
                return data.get("Users", [])
        except FileNotFoundError:
            return []

    def username_exists(self, username):
        user_list = self.get_user_list()

        for user_data in user_list:
            stored_username = user_data.get("Username")
            print(stored_username, username)
            if stored_username and stored_username == username:
                return True

        return False

    def back_to_welcome(self):
        # Check if the toplevel_window is a ParametersWindow
        if isinstance(self.toplevel_window, ParametersWindow):
            # Call the destroy method to close the ParametersWindow
            self.toplevel_window.destroy()
        
        for widget in self.winfo_children():
            widget.pack_forget()

        self.is_pacing_mode_selected = None  # Reset the flag

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
        bg_light_path = os.path.join(FILE_PATH_PREFIX,"Themes", "wave2_light.png")
        bg_dark_path = os.path.join(FILE_PATH_PREFIX,"Themes", "wave2_dark.png")
        bg_image = ctk.CTkImage(light_image=Image.open(bg_light_path),
                                  dark_image=Image.open(bg_dark_path),
                                  size=(70 * 27, 33 * 17))
        self.logo_label = ctk.CTkLabel(self.admin_frame, image=bg_image, text="")
        self.logo_label.pack(pady=(70, 0))

    def back_to_admin(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.is_pacing_mode_selected = None  # Reset the flag
        self.create_admin_screen()


    def deletion_checkbox_event(self, username, check_var):
        print(f"{username} checkbox toggled, current value: {check_var.get()}")

    def show_deletion_screen(self):
        self.admin_frame.pack_forget()
        self.deletion_frame = ctk.CTkFrame(self, width=200, height=200)
        self.deletion_frame.pack(fill='both', expand=True)

        userList = self.get_user_list()
        username = [user['Username'] for user in userList]
        self.checkboxList = []
        self.check_vars = []  # List to store the StringVars for each checkbox

        for i, item in enumerate(userList):
            check_var = ctk.StringVar(value="off")  # Individual check variable for each checkbox
            self.check_vars.append(check_var)

            checkbox = ctk.CTkCheckBox(self.deletion_frame, text=username[i],
                                       command=lambda i=i, check_var=check_var: self.deletion_checkbox_event(username[i], check_var),
                                       variable=check_var, onvalue="on", offvalue="off")
            checkbox.pack(pady=10)
            self.checkboxList.append(checkbox)

        ctk.CTkButton(self.deletion_frame, text='Delete', command=self.delete_users, width=150, height=40, font=("Arial", 20)).pack(pady=10)
        ctk.CTkButton(self.deletion_frame, text='Back', command=self.back_to_admin, width=150, height=40, font=("Arial", 20)).pack(pady=10)

    def delete_users(self):
        indices_to_delete = [i for i, check_var in enumerate(self.check_vars) if check_var.get() == "on"] # Determine the indices to be deleted

        if not indices_to_delete: # if there are no users
            print("No users selected for deletion.")
            return
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        user_file_path = os.path.join(script_dir, "user_accounts.json")

        with open(user_file_path, "r") as file:  # Read the contents of the file
            data = json.load(file)

        updated_users = [user for i, user in enumerate(data["Users"]) if i not in indices_to_delete] # Remove the selected lines
        data["Users"] = updated_users # update the json for not having the selected users
       
        with open(user_file_path, "w") as file:
            json.dump(data, file, indent=4)

        # Update the checkbox list and UI
        for index in sorted(indices_to_delete, reverse=True):
            self.checkboxList[index].destroy()  # Remove the checkbox widget
            del self.checkboxList[index]  # Remove the reference from the list
            del self.check_vars[index]  # Remove the associated StringVar

        print("Selected users have been deleted.")

    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get())

    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)
        
        # Check if the toplevel_window is a ParametersWindow
        if isinstance(self.toplevel_window, ParametersWindow):
            # Destroy the ParametersWindow
            self.toplevel_window.destroy()
        
        self.is_pacing_mode_selected = choice != "Select Pacing Mode"

        # Update the "⚙ Options" button state based on the pacing mode selection
        if self.is_pacing_mode_selected:
            self.options_button.configure(state='normal')
            self.run_pacing.configure(state='normal')
            self.stop_pacing.configure(state='normal')
            saved_parameters = {}

            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "user_accounts.json")
            with open(file_path, "r") as file:
                user_data = json.load(file)

            for user in user_data["Users"]:
                if user["Username"] == self.current_username:
                    user["Saved Parameters"][choice] = saved_parameters
            
            send_list = [22, 85, 0, 60, 120, 120, 150, 5, 5, 1, 1, 4, 4, 250, 320, 320, 4, 30, 8, 5]
            if choice == "AOO":
                send_list[2] = 0  # !!!!!!!!!!!!change depending on mode, I do not know which number is which mode
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[7] = saved_parameters['Atrial Amplitude']/1000
                send_list[9] = saved_parameters['Atrial Pulse Width']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            elif choice == "AAI":
                send_list[2] = 2
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[7] = saved_parameters['Atrial Amplitude']/1000
                send_list[9] = saved_parameters['Atrial Pulse Width']
                send_list[11] = saved_parameters['Atrial Sensitivity']/1000
                send_list[13] = saved_parameters['Absolute Refractory Period']
                send_list[15] = saved_parameters['Post-Ventricular Atrial Refractory Period']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            elif choice == "VOO":
                send_list[2] = 1
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[8] = saved_parameters['Ventricular Amplitude']/1000
                send_list[10] = saved_parameters['Ventricular Pulse Width']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            elif choice == "VVI":
                send_list[2] = 3
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[8] = saved_parameters['Ventricular Amplitude']/1000
                send_list[10] = saved_parameters['Ventricular Pulse Width']
                send_list[12] = saved_parameters['Ventricular Sensitivity']/1000
                send_list[14] = saved_parameters['Ventricular Refractory Period']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            elif choice == "AOOR":
                send_list[2] = 4
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[5] = saved_parameters['Maximum Sensor Rate']
                send_list[7] = saved_parameters['Atrial Amplitude']/1000
                send_list[9] = saved_parameters['Atrial Pulse Width']
                send_list[16] = saved_parameters['Activity Threshold']
                send_list[17] = saved_parameters['Reaction Time']
                send_list[18] = saved_parameters['Response Factor']
                send_list[19] = saved_parameters['Recovery Time']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            elif choice == "AAIR":
                send_list[2] = 6
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[5] = saved_parameters['Maximum Sensor Rate']
                send_list[7] = saved_parameters['Atrial Amplitude']/1000
                send_list[9] = saved_parameters['Atrial Pulse Width']
                send_list[11] = saved_parameters['Atrial Sensitivity']/1000
                send_list[13] = saved_parameters['Absolute Refractory Period']
                send_list[15] = saved_parameters['Post-Ventricular Atrial Refractory Period']
                send_list[16] = saved_parameters['Activity Threshold']
                send_list[17] = saved_parameters['Reaction Time']
                send_list[18] = saved_parameters['Response Factor']
                send_list[19] = saved_parameters['Recovery Time']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            elif choice == "VOOR":
                send_list[2] = 5
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[5] = saved_parameters['Maximum Sensor Rate']
                send_list[8] = saved_parameters['Ventricular Amplitude']/1000
                send_list[10] = saved_parameters['Ventricular Pulse Width']
                send_list[16] = saved_parameters['Activity Threshold']
                send_list[17] = saved_parameters['Reaction Time']
                send_list[18] = saved_parameters['Response Factor']
                send_list[19] = saved_parameters['Recovery Time']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            elif choice == "VVIR":
                send_list[2] = 7
                send_list[3] = saved_parameters['Lower Rate Limit']
                send_list[4] = saved_parameters['Upper Rate Limit']
                send_list[5] = saved_parameters['Maximum Sensor Rate']
                send_list[8] = saved_parameters['Ventricular Amplitude']/1000
                send_list[10] = saved_parameters['Ventricular Pulse Width']
                send_list[12] = saved_parameters['Ventricular Sensitivity']/1000
                send_list[14] = saved_parameters['Ventricular Refractory Period']
                send_list[16] = saved_parameters['Activity Threshold']
                send_list[17] = saved_parameters['Reaction Time']
                send_list[18] = saved_parameters['Response Factor']
                send_list[19] = saved_parameters['Recovery Time']
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
            else:
                send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
        else:
            self.options_button.configure(state='disabled')
            self.run_pacing.configure(state='disabled')
            self.stop_pacing.configure(state='disabled')
 
    def pacing_mode_callback(self, *args):
        pacing_mode = self.pacing_mode.get()
        self.is_pacing_mode_selected = pacing_mode != "Select Pacing Mode"

        if self.toplevel_window is not None and self.toplevel_window.winfo_exists():
            self.toplevel_window.destroy()

        if self.is_pacing_mode_selected:
            self.toplevel_window = ParametersWindow(self, self.optionmenu_var)

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
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "pacing_modes.json")

        # Read values from pacing_modes.json
        with open(file_path, "r") as file:
            pacing_modes = json.load(file)

        self.pacing_mode = ctk.StringVar()
        self.pacing_mode.trace("w", self.pacing_mode_callback)
        self.pacing_mode.set("Select Pacing Mode")

        self.optionmenu_var = ctk.StringVar(value="Select Pacing Mode")
        self.optionmenu = ctk.CTkOptionMenu(self.nav_bar, values=list(pacing_modes.keys()), command=self.optionmenu_callback, variable=self.optionmenu_var)
        self.optionmenu.pack(side="right", padx=1)


        self.toplevel_window = None


        # MAIN BODY CONTENT
        self.body_frame = ctk.CTkFrame(self.main_frame)
        self.body_frame.pack(fill='both', expand=True, pady=20)

        self.graph_state = 'atrial'

       

        # GRAPH CONTENT
        ctk.CTkLabel(self.body_frame, text='ECG Output', font=("Calibri", 25, "bold")).pack(pady=10, padx=10, anchor='n')

        self.serial_app_frame = SerialApp(self.body_frame)
        self.serial_app_frame.pack(fill = 'x', pady = (10,2))
        

        # MAIN BODY CONTENT END

        
        # Create the "⚙ Options" button initially disabled
        if self.is_pacing_mode_selected:
            self.options_button = ctk.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, state='normal')
            self.options_button.pack(side='right', padx=10)

            self.stop_pacing = ctk.CTkButton(self.nav_bar, text='⏸ Stop', state='normal', command = self.serial_app_frame.stop)
            self.stop_pacing.pack(side='right', padx=10)

            self.run_pacing = ctk.CTkButton(self.nav_bar, text='▶ Run', state='normal', command = self.serial_app_frame.start)
            self.run_pacing.pack(side='right', padx=10)
        else:
            self.options_button = ctk.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, state='disabled')
            self.options_button.pack(side='right', padx=10)

            self.stop_pacing = ctk.CTkButton(self.nav_bar, text='⏸ Stop', state='disabled', command = self.serial_app_frame.stop)
            self.stop_pacing.pack(side='right', padx=10)

            self.run_pacing = ctk.CTkButton(self.nav_bar, text='▶ Run', state='disabled', command = self.serial_app_frame.start)
            self.run_pacing.pack(side='right', padx=10)

        self.footer_frame = ctk.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill='x', side='bottom', pady=10, padx=10)

        ctk.CTkButton(self.footer_frame, text='Print Report', command=self.printReport).pack(side='right', pady=10, padx=10)

        self.board_label = ctk.CTkLabel(self.footer_frame, text = (f"PACE++ V2.16.3 | {self.serial_app.serial_id} | Connected to {check_and_update_boards(self.serial_app.serial_id)} | McMaster University"))
        self.board_label.pack(side='right', padx=(0, 320))
        self.update_footer()
        self.connection = ctk.CTkLabel(self.footer_frame, text="Finding Connection", text_color="#BF616A")
        self.connection.pack(side='left', padx=10)
        print(self.serial_app.serial_port)
        self.verify_connection()

    def update_footer(self):
        self.board_label.configure(text = (f"PACE++ V2.16.3 | Serial ID: {self.serial_app.serial_id} | Connected to {check_and_update_boards(self.serial_app.serial_id)} | McMaster University"))
        self.after(105, self.update_footer)

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
        if not self.is_pacing_mode_selected:
            return  # Do not show the Parameters Window if pacing mode hasn't been selected

        selected_pacing_mode = self.optionmenu_var.get()

        # Check if the toplevel_window is a ParametersWindow for the selected pacing mode
        if isinstance(self.toplevel_window, ParametersWindow) and self.toplevel_window.pacing_mode == selected_pacing_mode:
            # Focus on the existing ParametersWindow
            self.toplevel_window.focus()
        else:
            # Destroy the existing ParametersWindow if it exists
            if isinstance(self.toplevel_window, ParametersWindow):
                self.toplevel_window.destroy()

            # Create a new ParametersWindow for the selected pacing mode
            self.toplevel_window = ParametersWindow(self, self.optionmenu_var)

    def verify_connection(self):
        self.connection.configure(text=f"Connected To Port {self.serial_app.serial_port}", text_color="#1cac78")
        self.after(110, self.verify_connection)




    def printReport(self):
        # Prepare data
        report_date = datetime.now().strftime('%H:%M:%Y')
        serial_id = self.serial_app.serial_id  # Ensure this is defined in your class
        self.serial_app_frame.save_graphs()  
        self.serial_app_frame.plot_surface_electrogram()
        values = [0, 60, 120, 120, 150, 5, 5, 1, 1, 4, 4, 250, 320, 320, 4, 30, 8, 5]
        port = self.serial_app.serial_port
        array = send(22, 34, values[0], values[1], values[2], values[3],values[4], values[5],values[6], values[7],values[8], values[9],values[10], values[11],values[12], values[13],values[14], values[15], values[16], values[17], port)
        current_mode = self.optionmenu_var.get()
        
        # HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>PACE++ Printed Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                h1, h2 {{
                    color: navy;
                }}
                .report-header {{
                    color: darkred;
                    font-size: 1.2em;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                .figure-label {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <h1>PACE++ Printed Report</h1>
            <p class="report-header">Institution Name: McMaster University</p>
            <p class="report-header">Date and Time: {report_date}</p>
            <p class="report-header">Version: PACE++ V2.16.3</p>
            <p class="report-header">Serial Number: {serial_id}</p>

            
            <h2>Table of Contents</h2>
            <ul>
                <li>Bradycardia Parameters.........................................................1 </li>
                <li>Resulted Figures..................................................................2</li>
                <li>Threshold Test Results</li>
                <li>Measured Data</li>
                <li>Trending Results</li>
                <li>Rate Histogram</li>
                <li>Implant Data</li>
                <li>Net Change</li>
                <li>Marker Legend Report</li>
                <li>Session Net Change Report</li>
            </ul>


            <h2>Bradycardia Parameters</h2>
            <table class="tg" style="undefined;table-layout: fixed; width: 582px">
            <colgroup>
            <col style="width: 250.2px">
            <col style="width: 180.2px">
            <col style="width: 151.2px">
            </colgroup>
            <thead>
            <tr>
                <th class="tg-ev0v">Parameter Name</th>
                <th class="tg-zci2">Value</th>
                <th class="tg-zci2">Unit</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td class="tg-0lax">Mode</td>
                <td class="tg-0lax">{current_mode}</td>
                <td class="tg-0lax"></td>
            </tr>
            <tr>
                <td class="tg-0lax">Lower Rate Limit</td>
                <td class="tg-0lax">{array[1]}</td>
                <td class="tg-0lax">ppm</td>
            </tr>
            <tr>
                <td class="tg-0lax">Upper Rate Limit</td>
                <td class="tg-0lax">{array[2]}</td>
                <td class="tg-0lax">ppm</td>
            </tr>
            <tr>
                <td class="tg-0lax">Maximum Sensor Rate</td>
                <td class="tg-0lax">{array[3]}</td>
                <td class="tg-0lax">ppm</td>
            </tr>
            <tr>
                <td class="tg-0lax">AV Delay</td>
                <td class="tg-0lax">{array[4]}</td>
                <td class="tg-0lax"></td>
            </tr>
            <tr>
                <td class="tg-0lax">Atrial Amplitude</td>
                <td class="tg-0lax">{array[5]}</td>
                <td class="tg-0lax">V</td>
            </tr>
            <tr>
                <td class="tg-0lax">Ventricular Amplitude</td>
                <td class="tg-0lax">{array[6]}</td>
                <td class="tg-0lax">V</td>
            </tr>
            <tr>
                <td class="tg-0lax">Atrial Pulse Width</td>
                <td class="tg-0lax">{array[7]}</td>
                <td class="tg-0lax">ms</td>
            </tr>
            <tr>
                <td class="tg-0lax">Ventricular Pulse Width</td>
                <td class="tg-0lax">{array[8]}</td>
                <td class="tg-0lax">ms</td>
            </tr>
            <tr>
                <td class="tg-0lax">Atrial Sensitivity</td>
                <td class="tg-0lax">{array[9]}</td>
                <td class="tg-0lax">mV</td>
            </tr>
            <tr>
                <td class="tg-0lax">Ventricular Sensitivity</td>
                <td class="tg-0lax">{array[10]}</td>
                <td class="tg-0lax">mV</td>
            </tr>
            <tr>
                <td class="tg-0lax">Absolute Refractory Period</td>
                <td class="tg-0lax">{array[11]}</td>
                <td class="tg-0lax">ms</td>
            </tr>
            <tr>
                <td class="tg-0lax">Ventricular Refractory Period</td>
                <td class="tg-0lax">{array[12]}</td>
                <td class="tg-0lax">ms</td>
            </tr>
            <tr>
                <td class="tg-0lax">Post Ventricular Absolute Refractory Period</td>
                <td class="tg-0lax">{array[13]}</td>
                <td class="tg-0lax">ms</td>
            </tr>
            <tr>
                <td class="tg-0lax">Activity Threshold</td>
                <td class="tg-0lax">{array[14]}</td>
                <td class="tg-0lax"></td>
            </tr>
            <tr>
                <td class="tg-0lax">Reaction Time</td>
                <td class="tg-0lax">{array[15]}</td>
                <td class="tg-0lax">sec</td>
            </tr>
            <tr>
                <td class="tg-0lax">Response Factor</td>
                <td class="tg-0lax">{array[16]}</td>
                <td class="tg-0lax"></td>
            </tr>
            </tbody>
            </table>

            <h2>Resulted Figures</h2>
            <p>The following three figures below are the resultant graphs taken at the time interval chosen when the "print report" button was pressed. Figure 1 depicts the egram data \n
                for the electrical acitivity found inside the atrium of the heart paced by the ATR_SIGNAL pin located at A0 on the board. Figure 2 depicts the egram daata for the \n
                electrical activatiy related to ventricular pacing done by the VENT_SIGNAL pin located at A1 on the board. From these two graphs, we can look at the resultant graph \n
                where we can combine the two to examine the relationship between atrial and ventricular pacing the pacemaker. </p>
            <img src="Atrial_Graph.png" alt="Atrial Graph" style="width:100%;max-width:600px;"/>
            <p><span class="figure-label">Figure 1:</span> Atrial Output Graph</p>
            
            <img src="Ventricle_Graph.png" alt="Ventricle Graph" style="width:100%;max-width:600px;"/>
            <p><span class="figure-label">Figure 2:</span> Ventricle Output Graph</p>
            
            <img src="Combined_Graph.png" alt="Combined Graph" style="width:100%;max-width:600px;"/>
            <p><span class="figure-label">Figure 3:</span> Combined Egram Data Graph</p>

            <img src="Surface_Electrogram.png" alt="Surface Electrogram Graph" style="width:100%;max-width:800px;"/>
            <p><span class="figure-label">Figure 4:</span> Surface Egram Graph</p>

       
            <!-- Add your content for each section here -->

        </body>
        </html>
        """

        # Write HTML content to a file
        with open("PACE++_Printed_Report.html", "w") as file:
            file.write(html_content)

        print("Report generated successfully.")


if __name__ == '__main__':
    app = App()
    app.mainloop()

