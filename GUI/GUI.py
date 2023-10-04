# GUI
import customtkinter as ctk
import tkinter as tk


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Pacemaker')
        self.root.geometry('800x600')

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = ctk.CTkFrame(self.root)
        self.welcome_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.welcome_frame, text='Welcome!').pack(pady=20)
        ctk.CTkButton(self.welcome_frame, text='Login', command=self.show_login_screen).pack(pady=10)
        ctk.CTkButton(self.welcome_frame, text='Create an Account', command=self.show_create_account_screen).pack(pady=10)
        ctk.CTkButton(self.welcome_frame, text='Continue as Guest', command=self.show_main_screen).pack(pady=10)

    def show_login_screen(self):
        self.welcome_frame.pack_forget()
        self.login_frame = ctk.CTkFrame(self.root)
        self.login_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.login_frame, text='Login Screen').pack(pady=20)
        ctk.CTkButton(self.login_frame, text='Back', command=self.back_to_welcome).pack(pady=10)

    def show_create_account_screen(self):
        self.welcome_frame.pack_forget()
        self.create_account_frame = ctk.CTkFrame(self.root)
        self.create_account_frame.pack(fill='both', expand=True)

        ctk.CTkLabel(self.create_account_frame, text='Create Account Screen').pack(pady=20)
        ctk.CTkButton(self.create_account_frame, text='Back', command=self.back_to_welcome).pack(pady=10)

    def back_to_welcome(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.create_welcome_screen()

    def show_main_screen(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        self.nav_bar = ctk.CTkFrame(self.main_frame)
        self.nav_bar.pack(fill='x')
        ctk.CTkButton(self.nav_bar, text='Sign Out', command=self.back_to_welcome).pack(side='right')
        ctk.CTkButton(self.nav_bar, text='Parameters', command=self.show_parameters_popup).pack(side='right')

        self.body_frame = ctk.CTkFrame(self.main_frame)
        self.body_frame.pack(fill='both', expand=True, pady=20)
        ctk.CTkLabel(self.body_frame, text='Main Body Content').pack()

        self.footer_frame = ctk.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill='x', side='bottom')
        ctk.CTkLabel(self.footer_frame, text='Footer Content').pack()

        self.show_parameters_popup()

    def show_parameters_popup(self):
        self.parameters_popup = tk.Toplevel(self.root)
        self.parameters_popup.title('Parameters')
        ctk.CTkLabel(self.parameters_popup, text='Enter Frequency:').pack(pady=10)
        self.frequency_entry = ctk.CTkEntry(self.parameters_popup)
        self.frequency_entry.pack(pady=10)

        ctk.CTkLabel(self.parameters_popup, text='Enter Name:').pack(pady=10)
        self.name_entry = ctk.CTkEntry(self.parameters_popup)
        self.name_entry.pack(pady=10)

        ctk.CTkButton(self.parameters_popup, text='Save', command=self.save_parameters).pack(pady=10)
        ctk.CTkButton(self.parameters_popup, text='Close', command=self.parameters_popup.destroy).pack(pady=10)

    def save_parameters(self):
        self.frequency = self.frequency_entry.get()
        self.name = self.name_entry.get()
        print(f'Saved Parameters: Frequency - {self.frequency}, Name - {self.name}')
        self.parameters_popup.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()