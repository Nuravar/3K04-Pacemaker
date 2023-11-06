import tkinter as tk
from tkinter.font import Font

def on_resize(event):
    # Calculate the new font size based on the window size
    new_font_size = max(min(event.width // 20, event.height // 20), 8)  # Adjust the divisors to get the desired scaling
    # Update the font size of the label
    responsive_font.configure(size=new_font_size)

root = tk.Tk()
root.geometry('400x200')  # Initial size of the window

# Create a responsive font
responsive_font = Font(family='Helvetica', size=12)  # Starting font size

# Create a label with the responsive font
label = tk.Label(root, text="Responsive Font Size", font=responsive_font)
label.pack(expand=True, fill='both')

# Bind the resize event
root.bind('<Configure>', on_resize)

root.mainloop()
