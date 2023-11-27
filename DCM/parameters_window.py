import os
import customtkinter as ctk
from input_frame import InputFrame
import json
from simulink_serial import send, SerialApp
import time


class ParametersWindow(ctk.CTkToplevel):
    def __init__(self, app, pacing_mode):
        super().__init__()
        self.app = app
        self.title("Parameters Window")
        self.geometry('850x750')
        self.minsize(750, 650)
        self.overall_frame = ctk.CTkScrollableFrame(self)
        self.overall_frame.pack(side="top", fill="both", expand=True)
        self.frames = []
        # Load the parameters from the selected pacing mode
        self.pacing_mode = pacing_mode
        print("self.pacing_mode:", pacing_mode)
        self.load_parameters(self.pacing_mode)
        self.serial_app = SerialApp()
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

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "pacing_modes.json")
        # Load parameters from the pacing_modes.json file
        with open(file_path, "r") as file:
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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "user_accounts.json")
        current_user = self.app.current_username
        if current_user:
            with open(file_path, "r") as file:
                user_data = json.load(file)
                for user in user_data["Users"]:
                    if user["Username"] == current_user:
                        saved_parameters = user["Saved Parameters"].get(pacing_mode_value, {})
                        return bool(saved_parameters)

        return False

    def get_saved_value(self, parameter_title, pacing_mode_value):
        # Get the saved value from user_accounts.json
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "user_accounts.json")
        current_user = self.app.current_username
        if current_user:
            with open(file_path, "r") as file:
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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "user_accounts.json")
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
            print(saved_parameters)
            # Update the saved parameters in user_accounts.json
            with open(file_path, "r") as file:
                user_data = json.load(file)

            for user in user_data["Users"]:
                if user["Username"] == current_user:
                    user["Saved Parameters"][pacing_mode_value] = saved_parameters

            with open(file_path, "w") as file:
                json.dump(user_data, file, indent=2)

            print("Options saved successfully.")

            #send packets to the pacemaker
            send_Data_checked("save", pacing_mode_value, saved_parameters)
            
        else:
            print("No user logged in.")

    def reset_to_default(self):
        # Check if a user is logged in
        script_dir = os.path.dirname(os.path.abspath(__file__))
        user_file_path = os.path.join(script_dir, "user_accounts.json")
        file_path = os.path.join(script_dir, "pacing_modes.json")
        current_user = self.app.current_username
        if current_user:
            # Get the selected pacing mode
            pacing_mode_value = self.pacing_mode.get()

            # Load default values for the selected pacing mode from pacing_modes.json
            with open(file_path, "r") as file:
                pacing_data = json.load(file)
                default_values = pacing_data.get(pacing_mode_value, {}).get("Default Values", {})

            # Update the saved parameters in user_accounts.json to the default values
            with open(user_file_path, "r") as file:
                user_data = json.load(file)

            for user in user_data["Users"]:
                if user["Username"] == current_user:
                    user["Saved Parameters"][pacing_mode_value] = default_values

            with open(user_file_path, "w") as file:
                json.dump(user_data, file, indent=2)

            # Reload parameters with updated default values
            self.load_parameters(self.pacing_mode)
            print("the defualt values are: ", default_values)
            send_Data_checked("default", pacing_mode_value, default_values)
            print("Reset to default values successfully.")
        else:
            print("No user logged in.")




def send_Pacemaker( type, pacing_mode_value, saved_parameters):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    user_file_path = os.path.join(script_dir, "user_accounts.json")
    file_path = os.path.join(script_dir, "pacing_modes.json")
    send_list = [22, 85, 0, 60, 120, 120, 150, 5, 5, 1, 1, 4, 4, 250, 320, 320, 4, 30, 8, 5]
    serial_app = SerialApp()
    port = serial_app.serial_port
     #send(Sync, Function_call, Mode, LRL, URL, MSR, AVDelay, AAmp, VAmp, APulseWidth, VPulseWidth, ASensitivity, VSensitivity, ARP, VRP, PVARP, ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime, port):
    if pacing_mode_value == "AOO" and type == "save":
        send_list[2] = 0  # !!!!!!!!!!!!change depending on mode, I do not know which number is which mode
        send_list[3] = saved_parameters['Lower Rate Limit']
        send_list[4] = saved_parameters['Upper Rate Limit']
        send_list[7] = saved_parameters['Atrial Amplitude']/1000
        send_list[9] = saved_parameters['Atrial Pulse Width']
        send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
    elif pacing_mode_value == "AAI" and type == "save":
        send_list[2] = 2
        send_list[3] = saved_parameters['Lower Rate Limit']
        send_list[4] = saved_parameters['Upper Rate Limit']
        send_list[7] = saved_parameters['Atrial Amplitude']/1000
        send_list[9] = saved_parameters['Atrial Pulse Width']
        send_list[11] = saved_parameters['Atrial Sensitivity']/1000
        send_list[13] = saved_parameters['Absolute Refractory Period']
        send_list[15] = saved_parameters['Post-Ventricular Atrial Refractory Period']
        send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
    elif pacing_mode_value == "VOO" and type == "save":
        send_list[2] = 1
        send_list[3] = saved_parameters['Lower Rate Limit']
        send_list[4] = saved_parameters['Upper Rate Limit']
        send_list[8] = saved_parameters['Ventricular Amplitude']/1000
        send_list[10] = saved_parameters['Ventricular Pulse Width']
        send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
    elif pacing_mode_value == "VVI" and type == "save":
        send_list[2] = 3
        send_list[3] = saved_parameters['Lower Rate Limit']
        send_list[4] = saved_parameters['Upper Rate Limit']
        send_list[8] = saved_parameters['Ventricular Amplitude']/1000
        send_list[10] = saved_parameters['Ventricular Pulse Width']
        send_list[12] = saved_parameters['Ventricular Sensitivity']/1000
        send_list[14] = saved_parameters['Ventricular Refractory Period']
        send(send_list[0], send_list[1], send_list[2], send_list[3], send_list[4], send_list[5], send_list[6], send_list[7], send_list[8], send_list[9], send_list[10], send_list[11], send_list[12], send_list[13], send_list[14], send_list[15], send_list[16], send_list[17], send_list[18], send_list[19], port)
    elif pacing_mode_value == "AOOR" and type == "save":
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
    elif pacing_mode_value == "AAIR" and type == "save":
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
    elif pacing_mode_value == "VOOR" and type == "save":
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
    elif pacing_mode_value == "VVIR" and type == "save":
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
    send_list.pop()
    return send_list

def convert_to_int(array):
    for i in range(len(array)):
        array[i] = int(array[i])



def recieve_Pacemaker():
    serial_app = SerialApp()
    port = serial_app.serial_port
    values = [0, 60, 120, 120, 150, 5, 5, 1, 1, 4, 4, 250, 320, 320, 4, 30, 8, 5]
    array = send(22, 34, values[0], values[1], values[2], values[3],values[4], values[5],values[6], values[7],values[8], values[9],values[10], values[11],values[12], values[13],values[14], values[15], values[16], values[17], port)
    print("second print", array)
    return array

def send_Data_checked( type, pacing_mode_value, saved_parameters): 
    sent_values = send_Pacemaker(type, pacing_mode_value, saved_parameters)
    time.sleep(1)
    sent_values.pop(0)
    sent_values.pop(0)
    sent_values = sent_values[:4] + sent_values[5:]
    checker = recieve_Pacemaker()
    checker = checker[:4] + checker[5:]
    convert_to_int(sent_values)
    convert_to_int(checker)
    print("values", sent_values)
    print("check", checker)

    if (sent_values == checker): #need to change simulink serial
        print("sent packets verified")
    else:
        send_Pacemaker("default", pacing_mode_value, saved_parameters)
        print("Invalid bytes sent")

