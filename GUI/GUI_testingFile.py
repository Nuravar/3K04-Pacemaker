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
    values = [] #class level variable

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x400")
        self.title("Parameters")

        self.overall_frame = customtkinter.CTkScrollableFrame(self)
        self.overall_frame.pack(padx=20, pady=20, fill='both', expand=False)

        titles = [
            "Lower Rate Limit", "Upper Rate Limit", "Maximum Sensor Rate", "Fixed AV Delay",
            "Atrial Amplitude", "Atrial Pulse Width", "Atrial Sensitivity", "Ventricular Amplitude",
            "Ventricular Pulse Width", "Ventricular Sensitivity", "Absolute Refractory Period",
            "Ventricular Refractory Period", "Post-Ventricular Atrial Refractory Period", "Activity Threshold",
            "Reaction Time", "Response Factor", "Recovery Time"
        ]

        if not ParametersWindow.values:
            ParametersWindow.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        
        self.frames = []
        for title, value in zip(titles, self.values):
            frame = InputFrame(self.overall_frame, title)
            frame.entry.insert(0, value)  # Insert the default value into the entry
            frame.pack(padx=20, pady=20, anchor='w')
            self.frames.append(frame)

        # Save Button
        self.save_button = customtkinter.CTkButton(self, text="Save Options", command=self.save_options, fg_color="#1d3557", hover_color="#457B9D")
        self.save_button.pack(padx=20, pady=20)

    def save_options(self):
        for i, frame in enumerate(self.frames):
            self.values[i] = frame.entry.get()  # Update the values list with the current entry value
            frame.entry.delete(0, 'end')  # Clear the entry
            frame.entry.insert(0, self.values[i])  # Insert the updated value back into the entry
        print(self.values)

    def update_values(self):
        for i, frame in enumerate(self.frames):
            frame.entry.delete(0, 'end')  # Clear the entry
            frame.entry.insert(0, self.values[i])  # Insert the updated value into the entry