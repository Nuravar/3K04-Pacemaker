import os
import customtkinter as ctk
from input_frame import InputFrame

class ParametersWindow(ctk.CTkToplevel):
    # This window allows users to adjust pacemaker parameters with sliders
    DEFAULT_VALUES = {
        "AOO": [60, 120, 120, 150, 3500, 400, 750, 3500, 400, 250, 250, 320, 250, 4, 30, 8, 5],
        "AAI": [60, 120, 120, 150, 3500, 400, 750, 3500, 400, 250, 250, 320, 250, 4, 30, 8, 5],
        "VOO": [60, 120, 120, 150, 3500, 400, 750, 3500, 400, 250, 250, 320, 250, 4, 30, 8, 5],
        "VVI": [60, 120, 120, 150, 3500, 400, 750, 3500, 400, 250, 250, 320, 250, 4, 30, 8, 5]
    }

    SLIDER_RANGES = {
        "AOO": [...],  # Define slider ranges for AOO pacing mode
        "AAI": [...],  # Define slider ranges for AAI pacing mode
        "VOO": [...],  # Define slider ranges for VOO pacing mode
        "VVI": [...],  # Define slider ranges for VVI pacing mode
        # Add more pacing modes as needed
    }

    # slider_ranges = [
    #     (30, 175, [(30, 50, 5), (50, 90, 1), (90, 175, 5)]),  #lower rate limit x x 
    #     (50, 175, 5), # Upper Rate Limit x x 
    #     (50, 175, 5), # Maximum Sensor Rate x 
    #     (70, 300, 10), # Fixed AV Delay x
    #     (500, 7000, [(500, 3200, 100), (3200, 3500, 300), (3500, 7000, 500)]), # Atrial Amplitude   x x 
    #     (50, 1900, [(50,100,50),(100,1900,100)]),  # Atrial Pulse Width x x 
    #     (250, 10000, [(250,500,250), (500,750,250), (1000,10000,500)]),  # Atrial Sensitivity x 
    #     (500, 7000, [(500, 3200, 100), (3200, 3500, 300), (3500, 7000, 500)]),  # Ventricular Amplitude xx
    #     (50, 1900, [(50,100,50),(100,1900,100)]), # Ventricular Pulse Width x 
    #     (25000, 1000000, [(250,500,250), (500,750,250), (0,75000,1000,250), (1000,10000,500)]), # Ventricular Sensitivity x 
    #     (150, 500, 10), # Absolute Refractory Period x  
    #     (150, 500, 10), # Ventricular Refractory Period x 
    #     (150, 500, 10), # Post-Ventricular Atrial Refractory Period x 
    #     (0, 7, 1), # Activity Threshold x 
    #     (10, 50, 10), # Reaction Time x 
    #     (1, 16, 1), # Response Factor x
    #     (2, 16, 1) # Recovery Time x 
    # ]

    UNIT_LABELS = ["ppm", "ppm", "ppm", "ms", "µV", "µs", "µV", "µV", "µs", "µV", "ms", "ms", "ms", "", "sec", "", "min"]

    def __init__(self, app, pacing_mode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.geometry("600x400")
        self.title("Parameters")
        self.focus()  # Put the frame on top

        # Create a scrollable frame
        self.overall_frame = ctk.CTkScrollableFrame(self)
        self.overall_frame.pack(padx=20, pady=20, fill='both', expand=False)

        self.values = []  # Initialize the values list

        # Load the saved values for the current user and pacing mode
        loaded_values = self.load_user_values(pacing_mode)
        if loaded_values:
            self.values = loaded_values

        # Define unique slider ranges for each pacing mode
        slider_ranges = ParametersWindow.SLIDER_RANGES.get(pacing_mode, ParametersWindow.SLIDER_RANGES["AOO"])

        titles = [
            "Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Fixed AV Delay",
            "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "Ventricular Amplitude",
            "Ventricular Pulse Width", "Ventricular Sensitivity", "Absolute Refractory Period",
            "Ventricular Refractory Period", "Post-Ventricular Atrial Refractory Period", "Activity Threshold",
            "Reaction Time", "Response Factor", "Recovery Time"
        ]

        self.frames = []
        for (title, value, (from_, to_, increment), unit) in zip(titles, self.values, slider_ranges, ParametersWindow.UNIT_LABELS):
            frame = InputFrame(self.overall_frame, title, from_, to_, increment, unit)
            frame.slider.set(value)  # Set the slider to the default value
            frame.pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)

        # Buttons to save changes or reset to default
        # Save Button
        self.save_button = ctk.CTkButton(self, text="Save Options", command=lambda: self.save_options(pacing_mode))
        self.save_button.pack(side='left', padx=20, pady=20)

        # Reset to Default Button
        self.reset_button = ctk.CTkButton(self, text="Reset to Default", command=lambda: self.reset_to_default(pacing_mode))
        self.reset_button.pack(side='right', padx=20, pady=20)

    def reset_to_default(self, pacing_mode):
        # Reset the sliders to their default values for the given pacing mode
        default_values = ParametersWindow.DEFAULT_VALUES.get(pacing_mode, ParametersWindow.DEFAULT_VALUES["AOO"]).copy()
        self.update_values(default_values)
        self.save_options(pacing_mode)  # Save the default values back to the file

    def update_values(self, values):
        for i, frame in enumerate(self.frames):
            frame.slider.set(values[i])

    def save_options(self, pacing_mode):
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
                saved_parameters_dict = dict(zip(titles, map(str, self.values)))
                user_list[i] = f"{username}:{hashed_password}:{','.join(saved_parameters_dict[p] for p in titles)}"
                break

        # Write the updated user list back to the file
        with open("user_accounts.txt", "w") as file:
            file.write('\n'.join(user_list) + '\n' if user_list else '')

        print(f"Saved options for user {self.app.current_username} and pacing mode {pacing_mode}")

    def load_user_values(self, pacing_mode):
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
                # Update self.values with the saved parameters for the given pacing mode
                saved_parameters_dict = dict(zip(titles, map(int, saved_parameters.split(','))))
                return saved_parameters_dict.get(pacing_mode, ParametersWindow.DEFAULT_VALUES.get(pacing_mode, ParametersWindow.DEFAULT_VALUES["AOO"]))

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
