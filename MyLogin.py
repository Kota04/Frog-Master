import customtkinter as ctk

class MyLogin(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        
        self.container = ctk.CTkFrame(self, width=450, height=450)
        self.container.place(relx=0.5, rely=0.5, anchor="center")  # Center the container in the parent frame

        self.title_label = ctk.CTkLabel(self.container, text="Login To Your Account", font=("Arial", 24))
        self.username_entry = ctk.CTkEntry(self.container, placeholder_text="Enter Username", width=200)
        self.password_entry = ctk.CTkEntry(self.container, placeholder_text="Enter Password", show="*", width=200)
        self.login_button = ctk.CTkButton(self.container, text="Login", command=self.login)
        self.signup_button = ctk.CTkButton(self.container, text="Sign Up", command=self.go_to_signup)

        # Place widgets in the container
        self.title_label.place(relx=0.5, rely=0.2, anchor="center")
        self.username_entry.place(relx=0.5, rely=0.35, anchor="center")
        self.password_entry.place(relx=0.5, rely=0.45, anchor="center")
        self.login_button.place(relx=0.5, rely=0.55, anchor="center")
        self.signup_button.place(relx=0.5, rely=0.7, anchor="center")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.show_frame("MainContent")
        # Todo: Verify the username and password
       
    def go_to_signup(self):
        self.controller.show_frame("MySignup")

   