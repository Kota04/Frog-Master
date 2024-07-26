import customtkinter as ctk

class MySignup(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        
        # Create a container for widgets
        self.container = ctk.CTkFrame(self, width=450, height=600)
        self.container.place(relx=0.5, rely=0.5, anchor="center")  # Center the container in the parent frame

        # Initialize widgets
        self.title_label = ctk.CTkLabel(self.container, text="Sign Up For An Account", font=("Arial", 24))
        self.username_entry = ctk.CTkEntry(self.container, placeholder_text="Enter Username", width=200)
        self.password_entry = ctk.CTkEntry(self.container, placeholder_text="Enter Password", show="*", width=200)
        self.confirm_password_entry = ctk.CTkEntry(self.container, placeholder_text="Confirm Password", show="*", width=200)
        self.api_token_entry = ctk.CTkEntry(self.container, placeholder_text="Enter API Token", width=200)
        self.signup_button = ctk.CTkButton(self.container, text="Sign Up", command=self.signup)
        self.back_button = ctk.CTkButton(self.container, text="Back to Login", command=self.back_to_login)

        # Place widgets in the container
        self.title_label.place(relx=0.5, rely=0.18, anchor="center")
        self.username_entry.place(relx=0.5, rely=0.30, anchor="center")
        self.password_entry.place(relx=0.5, rely=0.40, anchor="center")
        self.confirm_password_entry.place(relx=0.5, rely=0.50, anchor="center")
        self.api_token_entry.place(relx=0.5, rely=0.60, anchor="center")
        self.signup_button.place(relx=0.5, rely=0.70, anchor="center")
        self.back_button.place(relx=0.5, rely=0.80, anchor="center")

    def signup(self):
        # TODO - Add the details into the database
        pass

    def back_to_login(self):
        self.controller.show_frame("MyLogin")
