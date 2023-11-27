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
    
    

def receiveSerial(port):
    # Initialize variables with default values
    Mode = LRL = URL = MSR = AVDelay = 0
    AAmp = VAmp = APulseWidth = VPulseWidth = 0
    ASensitivity = VSensitivity = ARP = VRP = 0
    ActivityThreshold = ReactionTime = ResponseFactor = RecoveryTime = 0

    st = struct.Struct('<BBBBBBBBBBBBBBBBBB')

    print("in receive function")
    try:
        com = serial.Serial(port, baudrate=115200)
        received_data = com.read(st.size)
        unpacked_data = st.unpack(received_data)

        # Assign values from unpacked_data
        Mode, LRL, URL, MSR, AVDelay = unpacked_data[:5]
        AAmp, VAmp = unpacked_data[5]/10, unpacked_data[6]/10
        APulseWidth, VPulseWidth = unpacked_data[7], unpacked_data[8]
        ASensitivity, VSensitivity = unpacked_data[9]/10, unpacked_data[10]/10
        ARP, VRP = unpacked_data[11]*10, unpacked_data[12]*10
        ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime = unpacked_data[13]*10, unpacked_data[14], unpacked_data[15], unpacked_data[16]

        print("inside receive", Mode, LRL, URL, MSR, AVDelay, AAmp, VAmp, APulseWidth, VPulseWidth, ASensitivity, VSensitivity, ARP, VRP, ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime)

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        if com:
            com.close()

    # Return array outside of finally block
    array = [Mode, LRL, URL, MSR, AVDelay, AAmp, VAmp, APulseWidth, VPulseWidth, ASensitivity, VSensitivity, ARP, VRP, ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime]
    return array


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
        return receiveSerial(port)

    
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
        self.serial_port, self.serial_id = list_available_ports()
        self.update_available_ports()
        with plt.style.context("DCM\\Themes\\pine.mplstyle"):
            self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(1, 3, figsize=(50, 6))  # 3 subplots in a row

            # Atrial graph
            self.ax1.set_title('Atrial Output')
            self.line1, = self.ax1.plot([], [], lw=2, label='Atrial Data')

            # Ventricle graph
            self.ax2.set_title('Ventricle Output')
            self.line2, = self.ax2.plot([], [], lw=2, label='Ventricle Data')

            # Combined graph
            self.ax3.set_title('Egram Data')
            self.line1_combined, = self.ax3.plot([], [], lw=2, label='Atrial Data')
            self.line2_combined, = self.ax3.plot([], [], lw=2, label='Ventricle Data')
            # Set labels and legend for each axis
            for ax in [self.ax1, self.ax2, self.ax3]:
                ax.set_xlabel('Time (t)')
                ax.set_ylabel('Voltage (V)')
                ax.legend(loc='upper right')
        ax.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        # Initialize data lists and a time counter
        self.xdata, self.ydata1, self.ydata2 = [], [], []
        self.start_time = None
        self.running = False
        self.max_length = 50  # Define the maximum length of the data arrays

        

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
            current_time = time.time() - self.start_time
            egram_data = egramPull(self.serial_port)

            self.xdata.append(current_time)
            self.ydata1.append(egram_data[0])  # Atrial data
            self.ydata2.append(egram_data[1])  # Ventricle data

            # Update atrial graph
            self.line1.set_xdata(self.xdata)
            self.line1.set_ydata(self.ydata1)
            self.ax1.relim()
            self.ax1.autoscale_view()

            # Update ventricle graph
            self.line2.set_xdata(self.xdata)
            self.line2.set_ydata(self.ydata2)
            self.ax2.relim()
            self.ax2.autoscale_view()

            # Update combined graph
            self.line1_combined.set_xdata(self.xdata)
            self.line1_combined.set_ydata(self.ydata1)
            self.line2_combined.set_xdata(self.xdata)
            self.line2_combined.set_ydata(self.ydata2)
            self.ax3.relim()
            self.ax3.autoscale_view()

            # Keep only the latest data points
            if len(self.xdata) > self.max_length:
                self.xdata.pop(0)
                self.ydata1.pop(0)
                self.ydata2.pop(0)

            self.canvas.draw()
            self.after(100, self.update_plot)


    def update_available_ports(self):
        self.serial_port, self.serial_id = list_available_ports()
        self.after(105, self.update_available_ports)

    def save_graphs(self):
        # Ensure the data is current on the graphs
        self.update_plot()
        
        # Save Atrial Graph
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax1.plot(self.xdata, self.ydata1, lw=2, label='Atrial Data')
        ax1.set_title('Atrial Output')
        ax1.set_xlabel('Time (t)')
        ax1.set_ylabel('Voltage (V)')
        ax1.legend(loc='upper right')
        fig1.savefig('Atrial_Graph.png')
        plt.close(fig1)

        # Save Ventricle Graph
        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot(self.xdata, self.ydata2, lw=2, label='Ventricle Data')
        ax2.set_title('Ventricle Output')
        ax2.set_xlabel('Time (t)')
        ax2.set_ylabel('Voltage (V)')
        ax2.legend(loc='upper right')
        fig2.savefig('Ventricle_Graph.png')
        plt.close(fig2)

        # Save Combined Graph
        fig3 = plt.figure()
        ax3 = fig3.add_subplot(111)
        ax3.plot(self.xdata, self.ydata1, lw=2, label='Atrial Data')
        ax3.plot(self.xdata, self.ydata2, lw=2, label='Ventricle Data')
        ax3.set_title('Egram Data')
        ax3.set_xlabel('Time (t)')
        ax3.set_ylabel('Voltage (V)')
        ax3.legend(loc='upper right')
        fig3.savefig('Combined_Graph.png')
        plt.close(fig3)

        print("Graphs saved as PNG files.")


    def plot_surface_electrogram(self):
        # Sum the data from ydata1 and ydata2
        ydata3 = [self.ydata1[i] + self.ydata2[i] for i in range(len(self.ydata1))]

        # Create a new figure for the surface electrogram
        fig, ax = plt.subplots(figsize=(25, 12))

        # Plot the summed data
        ax.plot(self.xdata, ydata3, lw=2, label='Surface Electrogram')

        # Set title and labels
        ax.set_title('Surface Electrogram')
        ax.set_xlabel('Time (t)')
        ax.set_ylabel('Voltage (V)')
        ax.legend(loc='upper right')

        # Save the figure
        fig.savefig('Surface_Electrogram.png')
        plt.close(fig)

