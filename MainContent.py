import customtkinter as ctk
from home_page import HomePage
from analyze_realtime_page import AnalyzeRealTimePage
from analyze_past_time_page import AnalyzePastTimePage
from analyze_pdf_page import AnalyzePDFPage

class MainContent(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # Navbar
        self.navbar = ctk.CTkFrame(self, height=50, fg_color="black", corner_radius=0)
        self.navbar.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        self.title_label = ctk.CTkLabel(self.navbar, text="Frog Master", font=("Arial", 26))
        self.title_label.place(relx=0.01, rely=0.5, anchor="w")

        self.logout_button = ctk.CTkButton(self.navbar, text="Logout", command=self.logout, height=50, font=("Arial", 18))
        self.logout_button.place(relx=0.98, rely=0.5, anchor="e")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=100, fg_color="black", corner_radius=0)
        self.sidebar.place(relx=0, rely=0.08, relwidth=0.111, relheight=0.92)

        self.home_button = ctk.CTkButton(self.sidebar, text="Home", command=self.show_home, corner_radius=0)
        self.home_button.place(relx=0.5, rely=0.03, anchor="center", relwidth=1, relheight=0.05)

        self.runtime_button = ctk.CTkButton(self.sidebar, text="Analyze Real Time", command=self.show_runtime, corner_radius=0)
        self.runtime_button.place(relx=0.5, rely=0.08, anchor="center", relwidth=1, relheight=0.05)

        self.offline_button = ctk.CTkButton(self.sidebar, text="Analyze Past Time", command=self.show_offline, corner_radius=0)
        self.offline_button.place(relx=0.5, rely=0.13, anchor="center", relwidth=1, relheight=0.05)

        self.analyze_pdf_button = ctk.CTkButton(self.sidebar, text="Analyze PDF", command=self.show_analyze_pdf, corner_radius=0)
        self.analyze_pdf_button.place(relx=0.5, rely=0.18, anchor="center", relwidth=1, relheight=0.05)

        # Main content area
        self.main_content = ctk.CTkFrame(self)
        self.main_content.place(relx=0.111, rely=0.08, relwidth=0.889, relheight=0.92)

        self.frames = {}
        for F in (HomePage, AnalyzeRealTimePage, AnalyzePastTimePage, AnalyzePDFPage):
            page_name = F.__name__
            frame = F(parent=self.main_content, controller=self)
            self.frames[page_name] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_home(self):
        self.show_frame("HomePage")

    def show_runtime(self):
        self.show_frame("AnalyzeRealTimePage")

    def show_offline(self):
        self.show_frame("AnalyzePastTimePage")

    def show_analyze_pdf(self):
        self.show_frame("AnalyzePDFPage")

    def logout(self):
        self.controller.show_frame("MyLogin")

# You can now create an instance of your MainContent class and add it to your application
