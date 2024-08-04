import customtkinter as ctk
# from PIL import Image, ImageTk
import subprocess

class AnalyzeRealTimePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Create a frame to contain all widgets
        self.container = ctk.CTkFrame(self, width=600, height=600)
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        # Initialize widgets
        self.label = ctk.CTkLabel(self.container, text="Analyze Real Time Page", font=("Arial", 26))
        self.label.place(relx=0.5, rely=0.1, anchor="center")
        
        self.SourceIP = ctk.CTkEntry(self.container, placeholder_text="Source IP", width=250)
        self.SourceIP.place(relx=0.5, rely=0.2, anchor="center")
        
        self.DestinationIP = ctk.CTkEntry(self.container, placeholder_text="Destination IP", width=250)
        self.DestinationIP.place(relx=0.5, rely=0.30, anchor="center")
        
        self.protocols = ["TCP", "UDP", "ICMP", "HTTPS", "SMTP", "FTP", "SSH"]
        self.protocol_vars = {protocol: ctk.BooleanVar() for protocol in self.protocols}

        # Create a frame for protocol checkboxes
        self.protocol_frame = ctk.CTkFrame(self.container)
        self.protocol_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Display checkboxes in a grid layout with 3 options per line
        for idx, protocol in enumerate(self.protocols):
            row = idx // 3
            col = idx % 3
            cb = ctk.CTkCheckBox(self.protocol_frame, text=protocol, variable=self.protocol_vars[protocol])
            cb.grid(row=row, column=col, padx=10, pady=5, sticky="w")

        # Run the interfaces.sh script to get the result and set the combo box values
        interface_values = self.get_interfaces()
        
        self.Interfaces = ctk.CTkComboBox(self.container, values=interface_values)
        self.Interfaces.place(relx=0.5, rely=0.7, anchor="center")

        self.Submit = ctk.CTkButton(self.container, text="Submit", command=self.submit)
        self.Submit.place(relx=0.5, rely=0.8, anchor="center")

    def get_interfaces(self):
        shell_script_path = './Interfaces.sh'
        try:
            result = subprocess.run(['bash', shell_script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            interfaces = result.stdout.splitlines()
            return interfaces
        except subprocess.CalledProcessError as e:
            print(f"Shell script failed with exit code {e.returncode}")
            print(f"Error output:\n{e.stderr}")
            return []

    def submit(self):
        source_ip = self.SourceIP.get()
        destination_ip = self.DestinationIP.get()
        selected_protocols = [protocol for protocol, var in self.protocol_vars.items() if var.get()]
        interface = self.Interfaces.get()
    
        # Print the details for debugging
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocols: {selected_protocols}")
        print(f"Interface: {interface}")
    
        # Build filter string
        filters = []
        if source_ip:
            filters.append(f"ip src {source_ip}")
        if destination_ip:
            filters.append(f"ip dst {destination_ip}")
        if selected_protocols:
            protocol_filters = ' or '.join([f'proto {protocol.lower()}' for protocol in selected_protocols])
            filters.append(f"({protocol_filters})")
    
        if filters:
            filter_str = ' and '.join(filters)
            filter_str = f"-f {filter_str}"  # Prefix the filter string with "-f"
        else:
            filter_str = ''  # No filters if nothing is specified
    
        # Print the constructed filter string for debugging
        print(f"Filter string: {filter_str}")
    
        # Construct the command with the filter string and interface
        shell_script_path = './CaptureTraffic.sh'
        try:
            # Note: Ensure that the CaptureTraffic.sh script can handle the filter string argument
            result = subprocess.run(['sudo', 'bash', shell_script_path, interface, filter_str],
                                    check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print('Success')
            print(f"Output:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Shell script failed with exit code {e.returncode}")
            print(f"Error output:\n{e.stderr}")
