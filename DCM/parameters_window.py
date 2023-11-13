import os
import customtkinter as ctk
from input_frame import InputFrame

class ParametersWindow(ctk.CTkToplevel):
    # This window allows users to adjust pacemaker parameters with sliders
    DEFAULT_VALUES = [60, 120, 120, 150, 3500, 400, 750,  3500, 400, 250, 250 , 320 , 250 , 4, 30 , 8, 5]
    values = []

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.geometry("1200x600")
        self.title("Parameters")
        self.focus() # Put the frame on top
        # Create a scrollable frame
        self.overall_frame = ctk.CTkScrollableFrame(self, height=400)
        self.overall_frame.pack(padx=20, pady=20, fill='both', expand=False)
        
        self.values = []  # Initialize the values list

        loaded_values = self.load_user_values()  # Load the saved values for the current user
        if loaded_values:
            self.values = loaded_values

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
        if self.values == []:
           self.values = ParametersWindow.DEFAULT_VALUES

        self.frames = []
        for (title, value, (from_, to_, increment), unit) in zip(titles, self.values, slider_ranges, units):
            frame = InputFrame(self.overall_frame, title, from_, to_, increment, unit)
            frame.slider.set(value)  # Set the slider to the default value
            frame.pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)
        # Buttons to save changes or reset to default
        # Save Button
        self.save_button = ctk.CTkButton(self, text="Save Options", command=self.save_options, width=150, height=40, font=("Arial", 20))
        self.save_button.pack(side='left', padx=20, pady=20)

        # Reset to Default Button
        self.reset_button = ctk.CTkButton(self, text="Reset to Default", command=self.reset_to_default, width=150, height=40, font=("Arial", 20))
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
        self.values = ParametersWindow.DEFAULT_VALUES.copy()  # Reset to default values in memory
        self.update_values()
        self.save_options()  # Save the default values back to the file

    def update_values(self):
        for i, frame in enumerate(self.frames):
            frame.slider.set(self.values[i])

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
            username, hashed_password, saved_parameters = user_entry.split(":")
            if self.app.current_username == username:
                # Update the encoded parameters directly
                user_list[i] = f"{username}:{hashed_password}:{','.join(map(str, self.values))}"
                break

        # Write the updated user list back to the file
        with open("user_accounts.txt", "w") as file:
            file.write('\n'.join(user_list) + '\n' if user_list else '')

        print(f"Saved options for user {self.app.current_username}")

    def load_user_values(self):
        # Check if a user is logged in
        if not self.app.current_username:
            print("No user logged in.")
            return

        # Read the existing user list from the file
        user_list = self.get_user_list()

        # Find the user entry for the currently logged-in user
        for user_entry in user_list:
            username, hashed_password, saved_parameters = user_entry.split(":")
            if self.app.current_username == username:
                # Update self.values with the saved parameters
                self.values = list(map(int, saved_parameters.split(',')))
                break

    def variable_increment(value, rangeAndInc):
        value = int(value)
        for (start, end, increment) in rangeAndInc:
            if start <= value <= end:
                return round((value - start) / increment) * increment + start
        return value