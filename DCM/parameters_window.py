import os
import customtkinter as ctk
from input_frame import InputFrame
import json

class ParametersWindow(ctk.CTkToplevel):
    def __init__(self, app, pacing_mode):
        super().__init__()
        self.app = app
        self.title("Parameters Window")

        self.overall_frame = ctk.CTkFrame(self)
        self.overall_frame.pack(side="top", fill="both", expand=True)
        self.frames = []

        # Load the parameters from the selected pacing mode
        self.pacing_mode = pacing_mode
        print("self.pacing_mode:", pacing_mode)
        self.load_parameters(self.pacing_mode)

    def load_parameters(self, pacing_mode):
        # Retrieve the value from the StringVar object
        pacing_mode_value = pacing_mode.get()
        print("pacing_mode_value", pacing_mode_value)

        # Load parameters from the pacing_modes.json file
        with open("pacing_modes.json", "r") as file:
            pacing_data = json.load(file)
            parameters = pacing_data.get(pacing_mode_value, {}).get("Parameters", [])

        # Clear existing frames
        for frame in self.frames:
            frame.destroy()

        self.frames = []

        # Create frames for each parameter
        for param in parameters:
            title = param["title"]
            units = param["units"]
            slider_range = param["slider_range"]
            default_value = param["default_value"]

            frame = InputFrame(self.overall_frame, title, ranges_and_increments=slider_range, unit=units)
            frame.slider.set(default_value)
            frame.pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)

    def update_parameters(self, pacing_mode):
        # Update pacing mode and load parameters
        self.load_parameters(pacing_mode)
