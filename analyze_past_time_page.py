import customtkinter as ctk
from tkinter import filedialog
import os
import subprocess
import requests  # You might use this if you need to make additional HTTP requests

class AnalyzePastTimePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
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
            # Run the shell script with the file path as an argument
            script_path = "./PastTraffic.sh"
            try:
                # Call the shell script with the file path
                result = subprocess.run(['sudo','bash', script_path, self.file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                # Handle script output
                if result.returncode == 0:
                    self.status_label.configure(text="File processed successfully.")
                    # Optionally, you can display the script output
                    print(result.stdout)
                else:
                    self.status_label.configure(text="Failed to process file.")
                    print(result.stderr)
                    
            except Exception as e:
                print(e)
                self.status_label.configure(text=f"An error occurred: {str(e)}")
        else:
            self.status_label.configure(text="Please upload a file first.")
        
