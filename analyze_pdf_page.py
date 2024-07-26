import customtkinter as ctk
from tkinter import filedialog
import os
import requests

class AnalyzePDFPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Create and place the container frame to hold all widgets
        self.container = ctk.CTkFrame(self, width=400, height=300)
        self.container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Create and place the label within the container frame
        self.label = ctk.CTkLabel(self.container, text="Analyze PDF Page", font=("Arial", 26))
        self.label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Create and place the upload button within the container frame
        self.upload_button = ctk.CTkButton(self.container, text="Upload PDF", command=self.upload_file)
        self.upload_button.place(relx=0.5, rely=0.4, anchor="center")
        
        # Create and place a label to show file upload status within the container frame
        self.status_label = ctk.CTkLabel(self.container, text="")
        self.status_label.place(relx=0.5, rely=0.6, anchor="center")

        # Create and place the submit button within the container frame
        self.submit_button = ctk.CTkButton(self.container, text="Submit", command=self.submit)
        self.submit_button.place(relx=0.5, rely=0.8, anchor="center")

        self.file_path = None  # Variable to store the selected file path

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")],
            title="Select a PDF file"
        )
        
        if self.file_path:
            file_size = os.path.getsize(self.file_path) / (1024 * 1024)  
            
            if file_size > 5:
                self.status_label.configure(text="File size exceeds 5MB.")
            else:
                self.status_label.configure(text=f"File '{os.path.basename(self.file_path)}' uploaded successfully.")

    def submit(self):
        #! TODO: Implement the logic to send the PDF file to VirusTotal and get the results
        if self.file_path:
            url = "YOUR_API_ENDPOINT"  
            api_key = "YOUR_API_KEY"  

            headers = {
                "Authorization": f"Bearer {api_key}"
            }
            
            files = {
                "file": open(self.file_path, "rb")  
            }
            
            try:
                response = requests.post(url, headers=headers, files=files)
                response.raise_for_status()  
                result = response.json()  
                self.status_label.configure(text=f"Submission successful. Result: {result}")
            except requests.RequestException as e:
                self.status_label.configure(text=f"Error submitting file: {e}")
        else:
            self.status_label.configure(text="No file selected.")
