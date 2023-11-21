import os
import customtkinter as ctk
from input_frame import InputFrame
import json

class ParametersWindow(ctk.CTkToplevel):
    def __init__(self, app, pacing_mode):
        super().__init__()
        self.app = app
        self.title("Parameters Window")
        self.geometry('650x550')
        self.overall_frame = ctk.CTkScrollableFrame(self)
        self.overall_frame.pack(side="top", fill="both", expand=True)
        self.frames = []
        # Load the parameters from the selected pacing mode
        self.pacing_mode = pacing_mode
        print("self.pacing_mode:", pacing_mode)
        self.load_parameters(self.pacing_mode)
        # Buttons to save changes or reset to default
        # Save Button
        self.save_button = ctk.CTkButton(self, text="Save Options", command=self.save_options, width=150, height=40, font=("Arial", 20))
        self.save_button.pack(side='left', padx=20, pady=20)

        # Reset to Default Button
        self.reset_button = ctk.CTkButton(self, text="Reset to Default", command=self.reset_to_default, width=150, height=40, font=("Arial", 20))
        self.reset_button.pack(side='right', padx=20, pady=20)

    def load_parameters(self, pacing_mode):
        # Retrieve the value from the StringVar object
        pacing_mode_value = pacing_mode.get()
        print("pacing_mode_value", pacing_mode_value)

        # Load parameters from the pacing_modes.json file
        with open("pacing_modes.json", "r") as file:
            pacing_data = json.load(file)
            parameters_info = pacing_data.get(pacing_mode_value, {})
            parameters = parameters_info.get("Parameters", [])
            default_values = {param["title"]: param.get("default_value") for param in parameters}

        # Clear existing frames
        for frame in self.frames:
            frame.destroy()

        self.frames = []

        # Check if there are saved values for the current pacing mode
        saved_values_available = self.are_saved_values_available(pacing_mode_value)

        # Create frames for each parameter
        for param in parameters:
            title = param.get("title")
            units = param.get("units")
            slider_range = param.get("slider_range")

            # Check if the slider_range is empty
            if not slider_range:
                slider_range = [0, 0, 0]

            # Extract 'from_' and 'to' from slider_range
            from_, to, increments = slider_range

            # Use the saved value if available, otherwise use the default value
            saved_value = self.get_saved_value(title, pacing_mode_value)
            default_value = saved_value if saved_values_available and saved_value is not None else default_values.get(title, from_)

            frame = InputFrame(self.overall_frame, title, from_, to, ranges_and_increments=increments, unit=units)
            frame.slider.set(default_value)
            frame.pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)

    def are_saved_values_available(self, pacing_mode_value):
        # Check if there are saved values for the current pacing mode
        current_user = self.app.current_username
        if current_user:
            with open("user_accounts.json", "r") as file:
                user_data = json.load(file)
                for user in user_data["Users"]:
                    if user["Username"] == current_user:
                        saved_parameters = user["Saved Parameters"].get(pacing_mode_value, {})
                        return bool(saved_parameters)

        return False

    def get_saved_value(self, parameter_title, pacing_mode_value):
        # Get the saved value from user_accounts.json
        current_user = self.app.current_username
        if current_user:
            with open("user_accounts.json", "r") as file:
                user_data = json.load(file)
                for user in user_data["Users"]:
                    if user["Username"] == current_user:
                        saved_parameters = user["Saved Parameters"].get(pacing_mode_value, {})
                        return saved_parameters.get(parameter_title)

        return None

    def update_parameters(self, pacing_mode):
        # Update pacing mode and load parameters
        self.load_parameters(pacing_mode)


    def save_options(self):
        # Check if a user is logged in
        current_user = self.app.current_username
        if current_user:
            # Get the selected pacing mode
            pacing_mode_value = self.pacing_mode.get()

            # Get the parameters for the current pacing mode
            saved_parameters = {}
            for frame in self.frames:
                title = frame.label.cget("text")  # Use label to access the title
                value = frame.slider.get()
                saved_parameters[title] = value

            # Update the saved parameters in user_accounts.json
            with open("user_accounts.json", "r") as file:
                user_data = json.load(file)

            for user in user_data["Users"]:
                if user["Username"] == current_user:
                    user["Saved Parameters"][pacing_mode_value] = saved_parameters

            with open("user_accounts.json", "w") as file:
                json.dump(user_data, file, indent=2)

            print("Options saved successfully.")
        else:
            print("No user logged in.")

    def reset_to_default(self):
        # Check if a user is logged in
        current_user = self.app.current_username
        if current_user:
            # Get the selected pacing mode
            pacing_mode_value = self.pacing_mode.get()

            # Load default values for the selected pacing mode from pacing_modes.json
            with open("pacing_modes.json", "r") as file:
                pacing_data = json.load(file)
                default_values = pacing_data.get(pacing_mode_value, {}).get("Default Values", {})

            # Update the saved parameters in user_accounts.json to the default values
            with open("user_accounts.json", "r") as file:
                user_data = json.load(file)

            for user in user_data["Users"]:
                if user["Username"] == current_user:
                    user["Saved Parameters"][pacing_mode_value] = default_values

            with open("user_accounts.json", "w") as file:
                json.dump(user_data, file, indent=2)

            # Reload parameters with updated default values
            self.load_parameters(self.pacing_mode)
            print("Reset to default values successfully.")
        else:
            print("No user logged in.")