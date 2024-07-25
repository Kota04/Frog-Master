import customtkinter as ctk

class MyLogin(ctk.CTkFrame):
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

        self.title_label = ctk.CTkLabel(self, text="Login To Your Account", font=("Arial", 24))
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Enter Username", width=200)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Enter Password", show="*", width=200)
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.signup_button = ctk.CTkButton(self, text="Sign Up", command=self.go_to_signup)

        self.title_label.grid(row=0, column=0, pady=30, padx=10)
        self.username_entry.grid(row=1, column=0, padx=20, pady=2)
        self.password_entry.grid(row=2, column=0, padx=20, pady=2)
        self.login_button.grid(row=3, column=0, pady=2)
        self.signup_button.grid(row=4, column=0, pady=(10, 100))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.show_frame("MainContent")
        #! Todo: Verify the username and password

    def go_to_signup(self):
        self.controller.show_frame("MySignup")
