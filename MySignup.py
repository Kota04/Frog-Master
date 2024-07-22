import customtkinter as ctk

class MySignup(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Sign Up For An Account", font=("Arial", 24))
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Enter Username", width=200)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter Password", show="*", width=200)
        self.confirm_password_entry = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=200)
        self.api_token_entry = ctk.CTkEntry(self, placeholder_text="Enter Api Token", width=200)
        self.signup_button = ctk.CTkButton(self, text="Sign Up", command=self.signup)
        self.back_button = ctk.CTkButton(self, text="Back to Login", command=self.back_to_login)

        self.title_label.grid(row=0, column=0, pady=30, padx=80)
        self.username_entry.grid(row=1, column=0, padx=20, pady=2)
        self.password_entry.grid(row=2, column=0, padx=20, pady=2)
        self.confirm_password_entry.grid(row=3, column=0, padx=20, pady=2)
        self.api_token_entry.grid(row=4, column=0, padx=20, pady=2)
        self.signup_button.grid(row=5, column=0, pady=10)
        self.back_button.grid(row=6, column=0, pady=(10, 100))

    def signup(self):
        #! TODO - Add the details into database
        pass

    def back_to_login(self):
        self.controller.show_frame("MyLogin")
