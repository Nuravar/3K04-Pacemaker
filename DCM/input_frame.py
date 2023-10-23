import customtkinter as ctk
import tkinter as tk

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
        self.value_var.set(corrected_value)  # Set the internal value
        # Update displayed value
        formatted_value = "{:.2f}".format(corrected_value)
        self.value_label['text'] = formatted_value + " " + self.unit

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
