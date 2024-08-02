import customtkinter as ctk
#from PIL import Image, ImageTk
from MyLogin import MyLogin
from MySignup import MySignup
from MainContent import MainContent

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Frog Master")
        self._max_width = 1200  # Set your max width here
        self._max_height = 800  # Set your max height here
        self.geometry(f"{self._max_width}x{self._max_height}")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # self.canvas = ctk.CTkCanvas(self)
        # self.canvas.grid(row=0, column=0, sticky="nsew")
        # self.bg_image = Image.open("./assets/pattern.png")
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        # self.canvas.create_image(0, 0, anchor='nw', image=self.bg_photo)

        self.container = ctk.CTkFrame(self, width=450, height=450)  # Fixed size for the container
        self.container.grid(row=0, column=0)
        self.container.grid_propagate(False)

        self.frames = {}
        for F in (MyLogin, MySignup, MainContent):
            page_name = F.__name__
            frame = F(self.container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MyLogin")

        # Center the container in the main window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "MainContent":
            # Make MainContent full-size
            self.container.configure(width=self.winfo_screenwidth(), height=self.winfo_screenheight())
            self.container.grid(row=0, column=0, sticky="nsew")
            frame.grid(row=0, column=0, sticky="nsew")
        else:
            # Reset the container size and re-center it
            self.container.configure(width=450, height=450)
            self.container.grid(row=0, column=0)
            frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
