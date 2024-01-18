
# Import necessary modules
from audioGenerator import WaveGen
import tkinter as tk
import tkinter.font as font
from tkinter import ttk, messagebox

# Creating a class for the WaveGen GUI, inheriting from tk.Tk
class WaveGenGUI(tk.Tk):
    # Constructor method to initialize the main window
    def __init__(self):
        # Initialize the main window
        tk.Tk.__init__(self)
        # Set the title and initial geometry of the window
        self.title("Audio Stagnography IS Project")
        self.geometry("800x600")

        # Create a notebook for different tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Set the common style for TButton
        button_font = font.Font(family='Helvitica', size=20)
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="#45b592", background="#45b592", font=button_font, height=3, width=15)


        # Create Encode Tab
        self.encode_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.encode_tab, text="Encode")

        # Setup Encode Tab
        self.setup_encode_tab()

        # Create Decode Tab
        self.decode_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.decode_tab, text="Decode")

        # Setup Decode Tab
        self.setup_decode_tab()

    # Method to set up widgets and functionality for the Encode Tab
    def setup_encode_tab(self):
        # Initialize variables for entry widgets
        encode_message_var = tk.StringVar(self.encode_tab)
        encode_filename_var = tk.StringVar(self.encode_tab)

        # Labels and entry widgets for Encode Tab
        tk.Label(self.encode_tab, text="Embadding Process", font=('Helvetica', 16)).pack(pady=5)
        tk.Label(self.encode_tab, text="Secret Message:", font=('Helvetica', 12)).pack(pady=5)
        encode_entry = tk.Entry(self.encode_tab, textvariable=encode_message_var, font=('Helvetica', 10), width=50)
        encode_entry.pack(pady=5)

        tk.Label(self.encode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
        filename_entry = tk.Entry(self.encode_tab, textvariable=encode_filename_var, font=('Helvetica', 10), width=50)
        filename_entry.pack(pady=5)

        tk.Label(self.encode_tab, text="Password:", font=('Helvetica', 12)).pack(pady=5)
        password_entry = tk.Entry(self.encode_tab, show="*", font=('Helvetica', 10), width=50)
        password_entry.pack(pady=5)

        # Button to trigger encoding
        encode_button = ttk.Button(self.encode_tab, text="Encode", command=lambda: self.encode(
            encode_message_var.get(), encode_filename_var.get(), password_entry.get()), style="TButton")
        encode_button.pack(pady=5)

        tk.Label(self.encode_tab, text="Status:", font=('Helvetica', 12)).pack()
        self.encode_status_label = tk.Label(self.encode_tab, text="", font=('Helvetica', 10))
        self.encode_status_label.pack(pady=5)

    # Method to handle encoding process
    def encode(self, secret_message, filename, password):
        # Function to handle encoding process
        if not password:
            messagebox.showerror("Error", "Please enter a password.")
            return

        wg = WaveGen()
        success = wg.encode(secret_message, filename, password)

        if success:
            self.encode_status_label.config(text="Message encoded successfully!")
            messagebox.showinfo("Encode Success", "Message encoded successfully!")
        else:
            self.encode_status_label.config(text="Encoding failed. Please check the message length.")
            messagebox.showerror("Encode Failed", "Encoding failed. Please check the message length.")

    # Method to set up widgets and functionality for the Decode Tab
    def setup_decode_tab(self):
        # Initialize variable for entry widget
        decode_filename_var = tk.StringVar(self.decode_tab)

        # Labels and entry widgets for Decode Tab
        tk.Label(self.decode_tab, text="Extrating Process", font=('Helvetica', 16)).pack(pady=5)
        tk.Label(self.decode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
        filename_entry = tk.Entry(self.decode_tab, textvariable=decode_filename_var, font=('Helvetica', 10), width=50)
        filename_entry.pack(pady=5)

        tk.Label(self.decode_tab, text="Password:", font=('Helvetica', 12)).pack(pady=5)
        password_entry = tk.Entry(self.decode_tab, show="*", font=('Helvetica', 10), width=50)
        password_entry.pack(pady=5)

        # Button to trigger decoding
        decode_button = ttk.Button(self.decode_tab, text="Decode", command=lambda: self.decode(
            decode_filename_var.get(), password_entry.get()), style="TButton")
        decode_button.pack(pady=5)

        tk.Label(self.decode_tab, text="Decoded Message:", font=('Helvetica', 12)).pack()
        self.decode_decoded_label = tk.Label(self.decode_tab, text="", font=('Helvetica', 10))
        self.decode_decoded_label.pack(pady=5)

    # Method to handle decoding process
    def decode(self, filename, password):
        # Function to handle decoding process
        if not password:
            messagebox.showerror("Error", "Please enter a password.")
            return

        wg = WaveGen()
        secret_message = wg.decode(filename, password)
        if secret_message:
            self.decode_decoded_label.config(text=secret_message)
            messagebox.showinfo("Decode Success", "Message decoded successfully!")
        else:
            messagebox.showerror("Decode Failed", "Message not found or invalid WAV file.")

# Application entry point
if __name__ == "__main__":
    app = WaveGenGUI()
    app.mainloop()