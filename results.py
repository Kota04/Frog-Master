import os
import customtkinter as ctk
from virusTotal import scan_file_with_virustotal

class Results(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=300, height=200)
        self.scrollable_frame.pack(fill="both", expand=True)

        title_label = ctk.CTkLabel(self.scrollable_frame, text="Results", font=("Arial", 24)) 
        title_label.pack(pady=10)

    def display_results(self):
        directory = "./files"
        # Clear previous results (if any)
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        title_label = ctk.CTkLabel(self.scrollable_frame, text="Results", font=("Arial", 24))  # Recreate title label
        title_label.pack(pady=10)

        
        if not os.listdir(directory):  
            no_files_label = ctk.CTkLabel(self.scrollable_frame, text="Your Traffic is safe", font=("Arial", 16), anchor='center')
            no_files_label.pack(pady=20, anchor='w')
            return

        # Process files if there are any
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                results = scan_file_with_virustotal(file_path)

                for result in results:
                    result_label = ctk.CTkLabel(self.scrollable_frame, text=result, font=("Arial", 16), anchor='w')  # Increased font size and set anchor to left
                    result_label.pack(pady=5, anchor='w')  # Aligns the label to the left
