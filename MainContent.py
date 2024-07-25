import customtkinter as ctk
from PIL import Image, ImageTk

class MainContent(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # Navbar
        self.navbar = ctk.CTkFrame(self, height=50, fg_color="black", corner_radius=0)
        self.navbar.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        self.title_label = ctk.CTkLabel(self.navbar, text="Frog Master", font=("Arial", 26))
        self.title_label.place(relx=0.01, rely=0.5, anchor="w")

        self.logout_button = ctk.CTkButton(self.navbar, text="Logout", command=self.logout,height=50,font=("Arial", 18))
        self.logout_button.place(relx=0.98, rely=0.5, anchor="e")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=100, fg_color="black", corner_radius=0)
        self.sidebar.place(relx=0, rely=0.08, relwidth=0.111, relheight=0.92)
        
        self.home = ctk.CTkButton(self.sidebar, text="Home", command=self.button1_action,corner_radius=0)
        self.home.place(relx=0.5, rely=0.03, anchor="center", relwidth=1, relheight=0.05)

        self.Runtime = ctk.CTkButton(self.sidebar, text="Analyze Real Time", command=self.button2_action,corner_radius=0)
        self.Runtime.place(relx=0.5, rely=0.08, anchor="center", relwidth=1, relheight=0.05)

        self.Offline = ctk.CTkButton(self.sidebar, text="Analyze Past Time", command=self.button3_action,corner_radius=0)
        self.Offline.place(relx=0.5, rely=0.13, anchor="center", relwidth=1, relheight=0.05)

        self.Analyze_pdf = ctk.CTkButton(self.sidebar, text="Analyze PDF", command=self.button3_action,corner_radius=0)
        self.Analyze_pdf.place(relx=0.5, rely=0.18, anchor="center", relwidth=1, relheight=0.05)

        # Main content area
        self.main_content = ctk.CTkFrame(self)
        self.main_content.place(relx=0.111, rely=0.08, relwidth=0.889, relheight=0.92)
        
    def button1_action(self):
        print("Button 1 clicked")

    def button2_action(self):
        print("Button 2 clicked")

    def button3_action(self):
        print("Button 3 clicked")

    def logout(self):
        self.controller.show_frame("MyLogin")

# You can now create an instance of your MainContent class and add it to your application
