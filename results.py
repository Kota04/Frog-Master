import customtkinter as ctk

class Results(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Results")
        label.place(relx=0.5, rely=0.5, anchor="center")
