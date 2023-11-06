import customtkinter as ctk

class MessageWindow(ctk.CTkToplevel):
    # This creates a simple message window with a given title and message.
    def __init__(self, title, msg):
        super().__init__()
        self.geometry("400x100")

        self.title(title)
        self.msg = ctk.CTkLabel(self, text=msg).pack(padx=20, pady=20)