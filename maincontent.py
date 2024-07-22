import customtkinter as ctk

class MainContent(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=0.85*master.winfo_screenwidth(), corner_radius=0, border_width=2, border_color="green")
        self.grid(row=0, column=1, sticky="nsew")
