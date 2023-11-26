import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import struct
import time
import threading


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
    
    #print(serial_com)
    #print("len of serial com: ",len(serial_com))
    com = serial.Serial(port, baudrate=115200)
    com.write(serial_com)
    unpacked = st.unpack(serial_com)
    #print(unpacked)
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

      





#def main():
    #send(Sync, Function_call, Mode, LRL, URL, MSR, AVDelay, AAmp, VAmp, APulseWidth, VPulseWidth, ASensitivity, VSensitivity, ARP, VRP, PVARP, ActivityThreshold, ReactionTime, ResponseFactor, RecoveryTime, port):
    # Send: 85      Receive: 34      egramPull: 56
    #send(22, 34, 0, 60, 120, 120, 150, 3.5, 3.5, 0.4, 0.4, 0.75, 2.5, 250, 320, 320, 10, 30, 8, 1, 'COM4')
    #send(22, 85, 4, 60, 60, 120, 150, 5, 5, 1, 1, 4, 4, 250, 320, 320, 10, 30, 8, 1, 'COM4')

    #while 1:
    #    egramPull('COM4')
    #    time.sleep(0.01)



# def main():
#     # Set up the figure for plotting
#     plt.ion()
#     fig, ax = plt.subplots()
#     ax.set_title('Egram Data')
#     ax.set_xlabel('Time (s)')
#     ax.set_ylabel('Value')
    
#     # Initialize two lines, one for each data set
#     line1, = ax.plot([], [], lw=2, label='Data 1')
#     line2, = ax.plot([], [], lw=2, label='Data 2')

#     # Initialize data lists and a time counter
#     xdata, ydata1, ydata2 = [], [], []
#     start_time = time.time()

#     while True:
#         # Calculate elapsed time
#         current_time = time.time() - start_time

#         # Pull data from egram
#         egram_data = egramPull('COM3')
        
#         # Append new data for both lines
#         xdata.append(current_time)
#         ydata1.append(egram_data[0])  # First data point
#         ydata2.append(egram_data[1])  # Second data point

#         # Update the line data
#         line1.set_xdata(xdata)
#         line1.set_ydata(ydata1)
#         line2.set_xdata(xdata)
#         line2.set_ydata(ydata2)

#         # Adjust plot limits dynamically
#         ax.relim()
#         ax.autoscale_view()

#         # Redraw the plot
#         fig.canvas.draw()
#         fig.canvas.flush_events()

#         # Wait for 0.1 seconds
#         time.sleep(0.1)

#     # Add a legend
#     ax.legend()



# main()

class SerialApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Serial Data Plotting")

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

        # Add buttons
        self.start_button = ttk.Button(self, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = ttk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.RIGHT, padx=20)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()

            # Clear existing data on start
            self.xdata.clear()
            self.ydata1.clear()
            self.ydata2.clear()
            self.update_plot()

    def stop(self):
        self.running = False

    def update_plot(self):
        if self.running:
            # Calculate elapsed time
            current_time = time.time() - self.start_time

            # Pull data from egram (replace with your data fetching logic)
            egram_data = egramPull('COM3')

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
if __name__ == "__main__":
    app = SerialApp()
    app.mainloop()


