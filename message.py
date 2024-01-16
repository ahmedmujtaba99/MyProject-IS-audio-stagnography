# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# #ENCRYPT
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"original message : {plain_text}")
# print(f"encrypted message: {cipher_text}")

# #DECRYPT
# cipher_text = input("Enter a message to encrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f"encrypted message: {cipher_text}")
# print(f"original message : {plain_text}")




import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import random
import string

def encrypt():
    plain_text = entry_encrypt.get()
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    label_encrypted_message.config(text=f"Encrypted message: {cipher_text}")

def decrypt():
    cipher_text = entry_decrypt.get()
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    label_decrypted_message.config(text=f"Decrypted message: {plain_text}")

# Set up the Tkinter window
window = tk.Tk()
window.title("Encryption and Decryption GUI")

# Define the character sets and create a copy for the key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# Create Tkinter variables for Entry widgets
var_encrypt = StringVar()
var_decrypt = StringVar()

# Create and place widgets
label_instruction_encrypt = Label(window, text="Enter a message to encrypt:")
entry_encrypt = Entry(window, textvariable=var_encrypt)
button_encrypt = Button(window, text="Encrypt", command=encrypt)
label_encrypted_message = Label(window, text="Encrypted message: ")

label_instruction_decrypt = Label(window, text="Enter a message to decrypt:")
entry_decrypt = Entry(window, textvariable=var_decrypt)
button_decrypt = Button(window, text="Decrypt", command=decrypt)
label_decrypted_message = Label(window, text="Decrypted message: ")

label_instruction_encrypt.pack()
entry_encrypt.pack()
button_encrypt.pack()
label_encrypted_message.pack()

label_instruction_decrypt.pack()
entry_decrypt.pack()
button_decrypt.pack()
label_decrypted_message.pack()

# Start the Tkinter event loop
window.mainloop()
