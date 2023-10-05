import customtkinter

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x400")

        self.overall_frame = customtkinter.CTkScrollableFrame(self)
        self.overall_frame.pack(padx=20, pady=20, fill='both', expand=False)
        # there is probably a way to convert all of these into a for loop and have all of the titles as a string
        #       i will probably do that later since idk what we are gonna do to these values
        # Frame containing the Lower Rate Limit
        self.LRL_frame = InputFrame(self.overall_frame, "Lower Rate Limit           ")
        self.LRL_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Upper Rate Limit
        self.URL_frame = InputFrame(self.overall_frame, "Upper Rate Limit           ")
        self.URL_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Maximum Sensor Rate
        self.MSR_frame = InputFrame(self.overall_frame, "Maximum Sensor Rate")
        self.MSR_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Fixed AV Delay
        self.FAV_frame = InputFrame(self.overall_frame, "Fixed AV Delay             ")
        self.FAV_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Atrial Amplitude
        self.AAM_frame = InputFrame(self.overall_frame, "Atrial Amplitude           ")
        self.AAM_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Atrial Pulse Width
        self.APW_frame = InputFrame(self.overall_frame, "Atrial Pulse Width         ")
        self.APW_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Atrial Sensitivity
        self.AST_frame = InputFrame(self.overall_frame, "Atrial Sensitivity          ")
        self.AST_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.VTA_frame = InputFrame(self.overall_frame, "Ventricular Amplitude      ")
        self.VTA_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.VPW_frame = InputFrame(self.overall_frame, "Ventricular Pulse Width    ")
        self.VPW_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.VTS_frame = InputFrame(self.overall_frame, "Ventricular Sensitivity    ")
        self.VTS_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.ARP_frame = InputFrame(self.overall_frame, "Absolute Refractory Period ")
        self.ARP_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.VRP_frame = InputFrame(self.overall_frame, "Ventricular Refractory Period")
        self.VRP_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.PVARP_frame = InputFrame(self.overall_frame, "Post-Ventricular Atrial Refractory Period")
        self.PVARP_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.ACT_frame = InputFrame(self.overall_frame, "Activity Threshold         ")
        self.ACT_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.RT_frame = InputFrame(self.overall_frame, "Reaction Time              ")
        self.RT_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.RF_frame = InputFrame(self.overall_frame, "Response Factor           ")
        self.RF_frame.pack(padx=20, pady=20, anchor='w')

        # Frame containing the Ventricular Amplitude
        self.RCT_frame = InputFrame(self.overall_frame, "Recovery Time            ")
        self.RCT_frame.pack(padx=20, pady=20, anchor='w')

        # Save Button
        self.save_button = customtkinter.CTkButton(self, text="Save Options", command=self.save_options)
        self.save_button.pack(padx=20, pady=20)

    def save_options(self):
        # Retrieve the values from the entries in the frames and print them
        LRL_value = self.LRL_frame.entry.get()
        URL_value = self.URL_frame.entry.get()
        # print(f"Lower Rate Limit: {LRL_value}")
        # print(f"Upper Rate Limit: {URL_value}")


class App(customtkinter.CTk):
    def __init__(self): #initializes, for all tkinter code, you find replace app with self
        super().__init__()
        self.title('Pacemaker')
        self.geometry('800x400')
        # self.custom_font = customtkinter.CTkFont(family="Calibri", size=14, weight='bold')
        self.create_welcome_screen()
        

    def create_welcome_screen(self):
        self.welcome_frame = customtkinter.CTkFrame(self)
        self.welcome_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.welcome_frame, text='Welcome!').pack(pady=20)
        customtkinter.CTkButton(self.welcome_frame, text='Login', command=self.show_login_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        customtkinter.CTkButton(self.welcome_frame, text='Create an Account', command=self.show_create_account_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)
        customtkinter.CTkButton(self.welcome_frame, text='Continue as Guest', command=self.show_main_screen, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)


    def show_login_screen(self):
        self.welcome_frame.pack_forget()
        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.login_frame, text='Login Screen').pack(pady=20)
        customtkinter.CTkButton(self.login_frame, text='Back', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)

    def show_create_account_screen(self):
        self.welcome_frame.pack_forget()
        self.create_account_frame = customtkinter.CTkFrame(self)
        self.create_account_frame.pack(fill='both', expand=True)

        customtkinter.CTkLabel(self.create_account_frame, text='Create Account Screen').pack(pady=20)
        customtkinter.CTkButton(self.create_account_frame, text='Back', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(pady=10)


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
        customtkinter.CTkButton(self.nav_bar, text='Sign Out', command=self.back_to_welcome, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
        customtkinter.CTkButton(self.nav_bar, text='⚙ Options', command=self.show_parameters_popup, fg_color="#1d3557", hover_color="#457B9D").pack(side='right')
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

        self.connection = customtkinter.CTkLabel(self.footer_frame, text="Finding Connection", text_color="#E63946", justify="right").pack(side = 'right') #initial state is not connected
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



if __name__ == '__main__':
    app = App()
    app.mainloop()  