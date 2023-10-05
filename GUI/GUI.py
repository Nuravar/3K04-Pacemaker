import customtkinter

class ParametersWindow(customtkinter.CTkToplevel):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("400x300")
            self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
            self.label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self): #initializes, for all tkinter code, you find replace app with self
        super().__init__()
        self.title('Pacemaker')
        self.geometry('800x600')
        # self.custom_font = customtkinter.CTkFont(family="Calibri", size=14, weight='bold')
        self.create_welcome_screen()
        

    def create_welcome_screen(self):
        self.welcome_frame = customtkinter.CTkFrame(self)
        self.welcome_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.welcome_frame, text='Welcome!').pack(pady=20)
        customtkinter.CTkButton(self.welcome_frame, text='Login', command=self.show_login_screen).pack(pady=10)
        customtkinter.CTkButton(self.welcome_frame, text='Create an Account', command=self.show_create_account_screen).pack(pady=10)
        customtkinter.CTkButton(self.welcome_frame, text='Continue as Guest', command=self.show_main_screen).pack(pady=10)


    def show_login_screen(self):
        self.welcome_frame.pack_forget()
        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.login_frame, text='Login Screen').pack(pady=20)
        customtkinter.CTkButton(self.login_frame, text='Back', command=self.back_to_welcome).pack(pady=10)

    def show_create_account_screen(self):
        self.welcome_frame.pack_forget()
        self.create_account_frame = customtkinter.CTkFrame(self)
        self.create_account_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.create_account_frame, text='Create Account Screen').pack(pady=20)
        customtkinter.CTkButton(self.create_account_frame, text='Back', command=self.back_to_welcome).pack(pady=10)


    def back_to_welcome(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.create_welcome_screen()

    def show_main_screen(self):
        for widget in self.winfo_children():
            widget.pack_forget()

        self.main_frame = customtkinter.CTkFrame(self)  
        self.main_frame.pack(fill='both', expand=True)

        self.nav_bar = customtkinter.CTkFrame(self.main_frame)
        self.nav_bar.pack(fill='x')
        customtkinter.CTkButton(self.nav_bar, text='Sign Out', command=self.back_to_welcome, fg_color="#1d3557").pack(side='right')
        customtkinter.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, fg_color="#1d3557").pack(side='right')
        self.toplevel_window = None

        self.switch_var = customtkinter.StringVar(value="on")
        self.switch = customtkinter.CTkSwitch(self.nav_bar, text="🌙", command=self.theme_event, variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.pack(side="left")
        
        self.body_frame = customtkinter.CTkScrollableFrame(self.main_frame)
        self.body_frame.pack(fill='both', expand=True, pady=20)
        customtkinter.CTkLabel(self.body_frame, text='Main Body Content').pack()

        self.footer_frame = customtkinter.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill='x', side='bottom')
        customtkinter.CTkLabel(self.footer_frame, text='Footer Content').pack()

        self.show_parameters_popup()


    def theme_event(self):
        print("switch toggled, current value:", self.switch_var.get())
        if self.switch_var.get() == "on":
            customtkinter.set_appearance_mode("dark")
            self.switch.configure(text="🌙")
        else: 
            customtkinter.set_appearance_mode("light")
            self.switch.configure(text="🌞")       

    def show_parameters_popup(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ParametersWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def save_parameters(self):
        self.frequency = self.frequency_entry.get()
        self.name = self.name_entry.get()
        print(f'Saved Parameters: Frequency - {self.frequency}, Name - {self.name}')
        self.parameters_popup.destroy()


if __name__ == '__main__':
    app = App()
    app.mainloop()  