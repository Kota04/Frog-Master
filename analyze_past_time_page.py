import customtkinter as ctk
from tkinter import filedialog
import os
import subprocess
import requests 

class AnalyzePastTimePage(ctk.CTkFrame):
    def __init__(self, parent, controller, results_frame):
        super().__init__(parent)
        self.controller = controller
        self.results_frame = results_frame  # Reference to the Results frame
        
        self.container = ctk.CTkFrame(self, width=400, height=300)
        self.container.place(relx=0.5, rely=0.5, anchor="center")
        
        self.label = ctk.CTkLabel(self.container, text="Analyze Past Time Page", font=("Arial", 26))
        self.label.place(relx=0.5, rely=0.2, anchor="center")
        
        self.upload_button = ctk.CTkButton(self.container, text="Upload File", command=self.upload_file)
        self.upload_button.place(relx=0.5, rely=0.4, anchor="center")
        
        self.status_label = ctk.CTkLabel(self.container, text="")
        self.status_label.place(relx=0.5, rely=0.6, anchor="center")

        self.submit_button = ctk.CTkButton(self.container, text="Submit", command=self.submit)
        self.submit_button.place(relx=0.5, rely=0.8, anchor="center")
        
        self.file_path = None  

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("PCAP Files", "*.pcap")],
            title="Select a PCAP file"
        )
        
        if self.file_path:
            file_size = os.path.getsize(self.file_path) / (1024 * 1024)  # File size in MB
            
            if file_size > 5:
                self.status_label.configure(text="File size exceeds 5MB.")
            else:
                self.status_label.configure(text=f"File '{os.path.basename(self.file_path)}' uploaded successfully.")

    def submit(self):
        if self.file_path:
            script_path = "./PastTraffic.sh"
            try:
                result = subprocess.run(['sudo', 'bash', script_path, self.file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    self.status_label.configure(text="File processed successfully.")
                    self.results_frame.display_results()  # Call the display_results method
                    self.controller.show_frame("Results")  # Switch to the Results frame
                else:
                    self.status_label.configure(text="Failed to process file.")
                    print(result.stderr)
                    
            except Exception as e:
                print(e)
                self.status_label.configure(text=f"An error occurred: {str(e)}")
        else:
            self.status_label.configure(text="Please upload a file first.")

# Ensure that when you create AnalyzePastTimePage, you pass in the Results frame:
# analyze_page = AnalyzePastTimePage(parent, controller, results_frame)
