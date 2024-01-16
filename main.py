# from waveGenerator import WaveGen
# import os

# # title = """\n\033[36m      .o.       ooooo     ooo  .oooooo..o ooooooooooooo oooooooooooo ooooo      ooo 
# # \033[36m     .888.      `888'     `8' d8P'    `Y8 8'   888   `8 `888'     `8 `888b.     `8' 
# # \033[36m    .8"888.      888       8  Y88bo.           888       888          8 `88b.    8  
# # \033[36m   .8' `888.     888       8   `"Y8888o.       888       888oooo8     8   `88b.  8  
# # \033[36m  .88ooo8888.    888       8       `"Y88b      888       888    "     8     `88b.8  
# # \033[36m .8'     `888.   `88.    .8'  oo     .d8P      888       888       o  8       `888  
# # \033[36mo88o     o8888o    `YbodP'    8""88888P'      o888o     o888ooooood8 o8o        `8"""
# # title2 = "\033[32m- Hide Your Secret Message in Audio Wave File -\033[37m"



# title = "IS Project"
# title2 = "\033[32m- Hide Your Secret Message in Audio Wave File -\033[37m"



# def choose(op):
#     if op not in ['1','2','3']:
#         return
    
#     if op == '3':
#         exit()
    
#     if op == '1':       # Encode
#         secretMessage = input("\033[33mWrite a message: \n\033[37m")
#         filename = input("\033[33mName the audio wave file: \033[37m")
#         wg.encode(secretMessage, filename)
#         input("\n[Press Enter]")

#     if op == '2':       # Decode
#         audioFileName = input("Name the audio wave file (only if is in the same folder): ")
#         wg.decode(audioFileName)
#         input("\n[Press Enter]")


# def main():
#     while True:
#         os.system('cls')
#         print(title)
#         print('\n' + title2)
#         operation = input("\n\nPress:\n1) Generate an audio wave file with a secret message\n2) Decode Secret Message from audio .wav file\n3) Quit\n\n>> ")
#         choose(operation)

# wg = WaveGen()
# main()

# GUI
# from waveGenerator import WaveGen
# import tkinter as tk
# from tkinter import filedialog, messagebox

# class WaveGenGUI(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title("WaveGen GUI")
#         self.geometry("400x300")

#         self.message_var = tk.StringVar(self)
#         self.filename_var = tk.StringVar(self)

#         tk.Label(self, text="Secret Message:").pack()
#         tk.Entry(self, textvariable=self.message_var).pack()

#         tk.Label(self, text="Filename:").pack()
#         tk.Entry(self, textvariable=self.filename_var).pack()

#         tk.Button(self, text="Encode", command=self.encode).pack()
#         tk.Button(self, text="Decode", command=self.decode).pack()

#         tk.Label(self, text="Decoded Message:", font=('Helvetica', 12)).pack()

#         self.decoded_label = tk.Label(self, text="", font=('Helvetica', 10))
#         self.decoded_label.pack(pady=5)

#     def encode(self):
#         secret_message = self.message_var.get()
#         filename = self.filename_var.get()

#         wg = WaveGen()
#         success = wg.encode(secret_message, filename)

#         if success:
#             messagebox.showinfo("Encode Success", "Message encoded successfully!")
#         else:
#             messagebox.showerror("Encode Failed", "Encoding failed. Please check the message length.")

#     def decode(self):
#         filename = filedialog.askopenfilename(title="Select a WAV file", filetypes=[("WAV files", "*.wav")])
#         if filename:
#             wg = WaveGen()
#             secret_message = wg.decode(filename)
#             if secret_message:
#                 self.decoded_label.config(text=secret_message)
#                 messagebox.showinfo("Decode Success", "Message decoded successfully!")
#             else:
#                 messagebox.showerror("Decode Failed", "Message not found or invalid WAV file.")

# if __name__ == "__main__":
#     app = WaveGenGUI()
#     app.mainloop()

# 3
from waveGenerator import WaveGen
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class WaveGenGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Audio Stagnography")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

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
        # encode_entry.insert(0, "Enter message to hide data")
        encode_entry.pack(pady=5)

        tk.Label(self.encode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
        # Increase length and add placeholder
        filename_entry = tk.Entry(self.encode_tab, textvariable=encode_filename_var, font=('Helvetica', 10), width=50)
        filename_entry.insert(0, "Enter your file name")
        filename_entry.pack(pady=5)

        encode_button = ttk.Button(self.encode_tab, text="Encode", command=lambda: self.encode(encode_message_var.get(), encode_filename_var.get()), style="TButton")
        encode_button.pack(pady=5)

        tk.Label(self.encode_tab, text="Status:", font=('Helvetica', 12)).pack()

        self.encode_status_label = tk.Label(self.encode_tab, text="", font=('Helvetica', 10))
        self.encode_status_label.pack(pady=5)

        self.style = ttk.Style()
        self.style.configure("TButton", foreground="white", background="#ADD8E6", padding=(5, 5), width=15)

    def encode(self, secret_message, filename):
        wg = WaveGen()
        success = wg.encode(secret_message, filename)

        if success:
            self.encode_status_label.config(text="Message encoded successfully!")
        else:
            self.encode_status_label.config(text="Encoding failed. Please check the message length.")

    def setup_decode_tab(self):
        decode_filename_var = tk.StringVar(self.decode_tab)

        tk.Label(self.encode_tab, text="Decode Message", font=('Helvetica', 16)).pack(pady=5)
        tk.Label(self.decode_tab, text="Filename:", font=('Helvetica', 12)).pack(pady=5)
        # Increase length and add placeholder
        filename_entry = tk.Entry(self.decode_tab, textvariable=decode_filename_var, font=('Helvetica', 10), width=50)
        filename_entry.insert(0, "Enter your file name")
        filename_entry.pack(pady=5)

        decode_button = ttk.Button(self.decode_tab, text="Decode", command=lambda: self.decode(decode_filename_var.get()), style="TButton")
        decode_button.pack(pady=5)

        tk.Label(self.decode_tab, text="Decoded Message:", font=('Helvetica', 12)).pack()

        self.decode_decoded_label = tk.Label(self.decode_tab, text="", font=('Helvetica', 10))
        self.decode_decoded_label.pack(pady=5)

    def decode(self, filename):
        wg = WaveGen()
        secret_message = wg.decode(filename)
        if secret_message:
            self.decode_decoded_label.config(text=secret_message)
        else:
            messagebox.showerror("Decode Failed", "Message not found or invalid WAV file.")

if __name__ == "__main__":
    app = WaveGenGUI()
    app.mainloop()



