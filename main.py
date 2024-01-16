# from waveGenerator import WaveGen
# import tkinter as tk
# import tkinter.font as font
# from tkinter import ttk, filedialog, messagebox

# class WaveGenGUI(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title("Audio Stagnography")
#         self.geometry("800x600")

#         self.notebook = ttk.Notebook(self)
#         self.notebook.pack(expand=True, fill="both")

#         button_font = font.Font(family='Helvitica', size=20)

#         # Set the common style for TButton
#         self.style = ttk.Style()
#         self.style.configure("TButton", foreground="#ffffff", background="#45b592", bd=0, font=button_font, height=2, width=10)

#         # Remove hover effect for the active state
#         self.style.map("TButton", background=[("active", "#45b592")])

#         # Create Encode Tab
#         self.encode_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.encode_tab, text="Encode")

#         self.setup_encode_tab()

#         # Create Decode Tab
#         self.decode_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.decode_tab, text="Decode")

#         self.setup_decode_tab()

#     def setup_encode_tab(self):
#         encode_message_var = tk.StringVar(self.encode_tab)
#         encode_filename_var = tk.StringVar(self.encode_tab)

#         tk.Label(self.encode_tab, text="Encode Message", font=('Helvetica', 16)).pack(pady=5)
#         tk.Label(self.encode_tab, text="Secret Message:", font=('Helvetica', 12)).pack(pady=5)
        
#         # Add a placeholder text
#         encode_entry = tk.Entry(self.encode_tab, textvariable=encode_message_var, font=('Helvetica', 10), width=50)
#         # encode_entry.insert(0, "Enter message to hide data")
#         encode_entry.pack(pady=5)

#         tk.Label(self.encode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
#         # Increase length and add placeholder
#         filename_entry = tk.Entry(self.encode_tab, textvariable=encode_filename_var, font=('Helvetica', 10), width=50)
#         # filename_entry.insert(0, "Enter your file name")
#         filename_entry.pack(pady=5)

#         encode_button = ttk.Button(self.encode_tab, text="Encode", command=lambda: self.encode(encode_message_var.get(), encode_filename_var.get()), style="TButton")
#         encode_button.pack(pady=5)

#         tk.Label(self.encode_tab, text="Status:", font=('Helvetica', 12)).pack()

#         self.encode_status_label = tk.Label(self.encode_tab, text="", font=('Helvetica', 10))
#         self.encode_status_label.pack(pady=5)

#     def encode(self, secret_message, filename):
#         wg = WaveGen()
#         success = wg.encode(secret_message, filename)

#         if success:
#             self.encode_status_label.config(text="Message encoded successfully!")
#             messagebox.showinfo("Encode Success", "Message encoded successfully!")
#         else:
#             self.encode_status_label.config(text="Encoding failed. Please check the message length.")
#             messagebox.showerror("Encode Failed", "Encoding failed. Please check the message length.")

#     def setup_decode_tab(self):
#         decode_filename_var = tk.StringVar(self.decode_tab)

#         tk.Label(self.decode_tab, text="Decode Message", font=('Helvetica', 16)).pack(pady=5)
#         tk.Label(self.decode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
#         # Increase length and add placeholder
#         filename_entry = tk.Entry(self.decode_tab, textvariable=decode_filename_var, font=('Helvetica', 10), width=50)
#         # filename_entry.insert(0, "Enter your file name")
#         filename_entry.pack(pady=5)

#         decode_button = ttk.Button(self.decode_tab, text="Decode", command=lambda: self.decode(decode_filename_var.get()), style="TButton")
#         decode_button.pack(pady=5)

#         tk.Label(self.decode_tab, text="Decoded Message:", font=('Helvetica', 12)).pack()

#         self.decode_decoded_label = tk.Label(self.decode_tab, text="", font=('Helvetica', 10))
#         self.decode_decoded_label.pack(pady=5)

#     def decode(self, filename):
#         wg = WaveGen()
#         secret_message = wg.decode(filename)
#         if secret_message:
#             self.decode_decoded_label.config(text=secret_message)
#             messagebox.showinfo("Decode Success", "Message decoded successfully!")
#         else:
#             messagebox.showerror("Decode Failed", "Message not found or invalid WAV file.")

# if __name__ == "__main__":
#     app = WaveGenGUI()
#     app.mainloop()





from audioGenerator import WaveGen
import tkinter as tk
import tkinter.font as font
from tkinter import ttk, filedialog, messagebox, simpledialog

class WaveGenGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Audio Stagnography")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        button_font = font.Font(family='Helvitica', size=20)

        # Set the common style for TButton
        self.style = ttk.Style()
        self.style.configure("TButton", foreground="#ffffff", background="#45b592", bd=0, font=button_font, height=2, width=10)

        # Remove hover effect for the active state
        self.style.map("TButton", background=[("active", "#45b592")])

        # Create Encode Tab
        self.encode_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.encode_tab, text="Encode")

        self.setup_encode_tab()

        # Create Decode Tab
        self.decode_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.decode_tab, text="Decode")

        self.setup_decode_tab()

    def setup_encode_tab(self):
        encode_message_var = tk.StringVar(self.encode_tab)
        encode_filename_var = tk.StringVar(self.encode_tab)

        tk.Label(self.encode_tab, text="Encode Message", font=('Helvetica', 16)).pack(pady=5)
        tk.Label(self.encode_tab, text="Secret Message:", font=('Helvetica', 12)).pack(pady=5)
        
        # Add a placeholder text
        encode_entry = tk.Entry(self.encode_tab, textvariable=encode_message_var, font=('Helvetica', 10), width=50)
        encode_entry.pack(pady=5)

        tk.Label(self.encode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
        filename_entry = tk.Entry(self.encode_tab, textvariable=encode_filename_var, font=('Helvetica', 10), width=50)
        filename_entry.pack(pady=5)

        # Add a password field
        tk.Label(self.encode_tab, text="Password:", font=('Helvetica', 12)).pack(pady=5)
        password_entry = tk.Entry(self.encode_tab, show="*", font=('Helvetica', 10), width=20)
        password_entry.pack(pady=5)

        encode_button = ttk.Button(self.encode_tab, text="Encode", command=lambda: self.encode(
            encode_message_var.get(), encode_filename_var.get(), password_entry.get()), style="TButton")
        encode_button.pack(pady=5)

        tk.Label(self.encode_tab, text="Status:", font=('Helvetica', 12)).pack()
        self.encode_status_label = tk.Label(self.encode_tab, text="", font=('Helvetica', 10))
        self.encode_status_label.pack(pady=5)

    def encode(self, secret_message, filename, password):
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

    def setup_decode_tab(self):
        decode_filename_var = tk.StringVar(self.decode_tab)

        tk.Label(self.decode_tab, text="Decode Message", font=('Helvetica', 16)).pack(pady=5)
        tk.Label(self.decode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
        filename_entry = tk.Entry(self.decode_tab, textvariable=decode_filename_var, font=('Helvetica', 10), width=50)
        filename_entry.pack(pady=5)

        # Add a password field
        tk.Label(self.decode_tab, text="Password:", font=('Helvetica', 12)).pack(pady=5)
        password_entry = tk.Entry(self.decode_tab, show="*", font=('Helvetica', 10), width=20)
        password_entry.pack(pady=5)

        decode_button = ttk.Button(self.decode_tab, text="Decode", command=lambda: self.decode(
            decode_filename_var.get(), password_entry.get()), style="TButton")
        decode_button.pack(pady=5)

        tk.Label(self.decode_tab, text="Decoded Message:", font=('Helvetica', 12)).pack()
        self.decode_decoded_label = tk.Label(self.decode_tab, text="", font=('Helvetica', 10))
        self.decode_decoded_label.pack(pady=5)

    def decode(self, filename, password):
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

if __name__ == "__main__":
    app = WaveGenGUI()
    app.mainloop()