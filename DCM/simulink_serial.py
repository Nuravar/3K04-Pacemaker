import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import struct
import time
import threading
import customtkinter as ctk  # Replace tkinter with customtkinter
import serial.tools.list_ports
import re
import json

def check_and_update_boards(serial_id):
    try:
        # Try to open the boards.json file
        with open('boards.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file is not found, create an empty dictionary
        data = {'Boards': {}}

    # Check if the given serial_id already exists
    if serial_id in data['Boards']:
        # If it exists, return the corresponding board number
        return data['Boards'][serial_id]
    else:
        # If it doesn't exist, find the next available board number
        board_numbers = [int(board.split()[-1]) for board in data['Boards'].values()]
        next_board_number = max(board_numbers) + 1 if board_numbers else 1

        # Add the new serial_id and corresponding board number to the dictionary
        data['Boards'][serial_id] = f"Board {next_board_number}"

        # Save the updated data back to the boards.json file
        with open('boards.json', 'w') as file:
            json.dump(data, file, indent=2)

        # Return the new board name
        return data['Boards'][serial_id]


def list_available_ports():
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No COM ports found")
    else:
        for port, desc, hwid in sorted(ports):
            
            pattern = r'SER=(\d+)'
            match = re.search(pattern, hwid)
            if match:
                ser_number = match.group(1)
                return port, ser_number
        return None, None
            

# Call the function to list available COM ports
list_available_ports()


def receiveSerial(port):
    
    st = struct.Struct('<BBBBBBBBBBBBBBBBBB')


    print("in receive function")
    try:
        com = serial.Serial(port, baudrate=115200)
        received_data = com.read(st.size)
        unpacked_data = st.unpack(received_data)

        Mode = unpacked_data[0]
        LRL = unpacked_data[1]
        URL = unpacked_data[2]
        MSR = unpacked_data[3]
        AVDelay = unpacked_data[4]
        AAmp = (unpacked_data[5])/10
        VAmp = (unpacked_data[6])/10
        APulseWidth = (unpacked_data[7])
        VPulseWidth = (unpacked_data[8])
        ASensitivity = (unpacked_data[9])/10
        VSensitivity = (unpacked_data[10])/10
        ARP = (unpacked_data[11])*10
        VRP = (unpacked_data[12])*10
        ActivityThreshold = (unpacked_data[13])*10
        ReactionTime = unpacked_data[14]
        ResponseFactor = unpacked_data[15]
        RecoveryTime = unpacked_data[16]

        print(Mode,LRL,URL,MSR)

        

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        com.close()
        return [Mode, LRL, URL, MSR, AVDelay, AAmp, VAmp, APulseWidth, VPulseWidth, ASensitivity, VSensitivity, ARP, VRP, ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime]


def send(Sync, Function_call, Mode, LRL, URL, MSR, AVDelay, AAmp, VAmp, APulseWidth, VPulseWidth, ASensitivity, VSensitivity, ARP, VRP, PVARP, ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime, port):


    st = struct.Struct('<BBBBBBBBBBBBBBBBBBBB')

    Function_call = int(Function_call)
    Sync = int(Sync)
    Mode=int(Mode)
    LRL=int(LRL)
    URL=int(URL)
    MSR=int(MSR)
    AVDelay = int(AVDelay/10)
    AAmp = int(10*AAmp)
    VAmp = int(10*VAmp)
    APulseWidth = int(APulseWidth)
    VPulseWidth = int(VPulseWidth)
    ASensitivity = int(10*ASensitivity)
    VSensitivity = int(10*VSensitivity)
    ARP = int(ARP/10)
    VRP = int(VRP/10)
    PVARP = int(PVARP/10)
    ActivityThreshold = int(ActivityThreshold)
    ReactionTime = int(ReactionTime)
    ResponseFactor = int(ResponseFactor)
    RecoveryTime = int(RecoveryTime)


    serial_com = st.pack(Sync, Function_call, Mode, LRL, URL, MSR, AVDelay, AAmp, VAmp, APulseWidth, VPulseWidth, ASensitivity, VSensitivity, ARP, VRP, PVARP, ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime)
    
    com = serial.Serial(port, baudrate=115200)
    com.write(serial_com)
    unpacked = st.unpack(serial_com)
    print("sent")
    com.close()

    if Function_call == 34:
        receiveSerial(port)

    
def egramPull(port):
    #Send egram message
    stsend = struct.Struct('<BBBBBBBBBBBBBBBBBBBB')
    serial_com = stsend.pack(22, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    com = serial.Serial(port, baudrate=115200)
    com.write(serial_com)
    print("send egram message")

    #receive egram
    streceive = struct.Struct('<ffBBBBBBBBBB')
    received_data = com.read(streceive.size)
    unpacked_data = streceive.unpack(received_data)

    print(unpacked_data[0],unpacked_data[1],unpacked_data[2],unpacked_data[3],unpacked_data[4],unpacked_data[5],unpacked_data[6],unpacked_data[7],unpacked_data[8])
    
    com.close()
    return unpacked_data

class SerialApp(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # Removed self.title("Serial Data Plotting")

        with plt.style.context("DCM\\Themes\\pine.mplstyle"):
            # Create a figure for plotting
            self.fig, self.ax = plt.subplots()
            self.ax.set_title('Egram Data')
            self.ax.set_xlabel('Time (s)')
            self.ax.set_ylabel('Value')
            self.line1, = self.ax.plot([], [], lw=2, label='Data 1')
            self.line2, = self.ax.plot([], [], lw=2, label='Data 2')

        # Embed the plot in the Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        # Initialize data lists and a time counter
        self.xdata, self.ydata1, self.ydata2 = [], [], []
        self.start_time = None
        self.running = False
        self.max_length = 50  # Define the maximum length of the data arrays

        self.serial_port, self.serial_id = list_available_ports()

    def start(self):
        print("started graphs")
        if not self.running:
            self.running = True
            self.start_time = time.time()

            # Clear existing data on start
            self.xdata.clear()
            self.ydata1.clear()
            self.ydata2.clear()
            self.update_plot()

    def stop(self):
        print("stopped graphs")
        self.running = False

    def update_plot(self):
        if self.running:
            # Calculate elapsed time
            current_time = time.time() - self.start_time

            # Pull data from egram (replace with your data fetching logic)
            egram_data = egramPull('COM5')

            # Append new data for both lines
            self.xdata.append(current_time)
            self.ydata1.append(egram_data[0])  # First data point
            self.ydata2.append(egram_data[1])  # Second data point

            # Keep only the latest data points within the fixed time interval
            if len(self.xdata) > self.max_length:
                self.xdata.pop(0)
                self.ydata1.pop(0)
                self.ydata2.pop(0)

            # Update the line data
            self.line1.set_xdata(self.xdata)
            self.line1.set_ydata(self.ydata1)
            self.line2.set_xdata(self.xdata)
            self.line2.set_ydata(self.ydata2)

            # Adjust plot limits dynamically
            self.ax.relim()
            self.ax.autoscale_view()

            # Redraw the plot
            self.canvas.draw()

            # Schedule the next update
            self.after(100, self.update_plot)

# Run the application
# if __name__ == "__main__":
#     app = SerialApp()
#     app.mainloop()



