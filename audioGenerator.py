
import sys
import struct
import numpy as np
from tkinter import messagebox  # Import messagebox for displaying dialogs

class WaveGen:
    def __init__(self, frequency=440, channels=2):
        # Initialize default values for audio parameters
        self.SAMPLE_RATE = 44100
        self.BIT_FOR_SAMPLE = 16
        self.FREQUENCY = frequency
        self.CHANNELS = channels
        self.TIME = 5
        self.bitArray = b''

    def bitMessage(self, line):
        # Convert a string message to a binary string
        bitLine = ''
        for c in line:
            bitLine += bin(ord(c))[2:].zfill(8)
        return bitLine

    def intToByte(self, n, length=4):
        # Convert integer to bytes and append to bitArray
        l, f = '<', ''
        if length == 2:
            f = 'h'
        else:
            f = 'i'
        bitValue = struct.pack(l + f, n)
        self.bitArray += bitValue

    def ChunkID(self):
        # Append RIFF chunk identifier to bitArray
        self.bitArray += b'RIFF'

    def ChunkSize(self):
        # Calculate and append chunk size to bitArray
        size = 36 + ((self.SAMPLE_RATE * self.TIME) * self.CHANNELS * self.BIT_FOR_SAMPLE // 8)
        self.intToByte(size)

    def Format(self):
        # Append WAVE format identifier to bitArray
        self.bitArray += b'WAVE'

    def SubChunk1ID(self):
        # Append fmt subchunk identifier to bitArray
        self.bitArray += b'fmt '

    def SubChunk1Size(self):
        # Append size of fmt subchunk to bitArray
        self.intToByte(16)

    def AudioFormat(self):
        # Set audio format to 1 (PCM)
        self.intToByte(1, length=2)

    def NumChannels(self):
        # Set number of channels and append to bitArray
        self.intToByte(self.CHANNELS, length=2)

    def SampleRate(self):
        # Set sample rate and append to bitArray
        self.intToByte(self.SAMPLE_RATE)

    def ByteRate(self):
        # Calculate byte rate and append to bitArray
        byteRate = self.SAMPLE_RATE * self.CHANNELS * self.BIT_FOR_SAMPLE // 8
        self.intToByte(byteRate)

    def BlockAlign(self):
        # Calculate block align and append to bitArray
        blockAlign = self.CHANNELS * self.BIT_FOR_SAMPLE // 8
        self.intToByte(blockAlign, length=2)

    def BitPerSample(self):
        # Set bits per sample and append to bitArray
        self.intToByte(self.BIT_FOR_SAMPLE, length=2)

    def Subchunk2ID(self):
        # Append data subchunk identifier to bitArray
        self.bitArray += b'data'

    def Subchunk2Size(self):
        # Calculate size of data subchunk and append to bitArray
        size = (self.SAMPLE_RATE * self.TIME) * self.CHANNELS * self.BIT_FOR_SAMPLE // 8
        self.intToByte(size)

    def AppendAudioData(self, secretMessage):
        # Append audio data to bitArray with secretMessage encoding
        secret = self.bitMessage(secretMessage + '#1991#')
        if len(secret) > (self.SAMPLE_RATE):
            print("\033[31mMessage too long.")
            return False

        # Generate sine wave signal
        self.data = np.linspace(0, self.TIME, (self.SAMPLE_RATE * self.TIME), endpoint=True)
        signal = np.sin(2 * np.pi * self.FREQUENCY * self.data)
        signal *= 32767
        signal = np.int16(signal)

        # Embed secret message into the audio signal
        for i in range(len(secret)):
            if secret[i] == '1':
                signal[i] = signal[i] | 1
            elif secret[i] == '0':
                signal[i] = signal[i] & ~1

        # Append the modified signal to bitArray
        for s in signal:
            self.intToByte(s)

        return True

    def WriteItDown(self, filename):
        # Write the bitArray to a WAV file
        with open(filename + '.wav', 'wb') as f:
            f.write(self.bitArray)

    def encode(self, secretMessage, filename, password):
        # Encode the secretMessage into an audio file
        print("\033[33mEncoding message...")
        self.bitArray = b''
        self.ChunkID()
        self.ChunkSize()
        self.Format()
        self.SubChunk1ID()
        self.SubChunk1Size()
        self.AudioFormat()
        self.NumChannels()
        self.SampleRate()
        self.ByteRate()
        self.BlockAlign()
        self.BitPerSample()
        self.Subchunk2ID()
        self.Subchunk2Size()

        # Encrypt the secret message with the provided password
        encrypted_message = self.encrypt_message(secretMessage, password)

        if self.AppendAudioData(encrypted_message):
            self.WriteItDown(filename)
            print("\033[32mDone.\033[37m")
            return True
        else:
            print("\033[31mEncoding Failed\033[37m")
            return False

    def encrypt_message(self, message, password):
        # Perform encryption here (you can use a simple encryption algorithm)
        # For demonstration purposes, a basic XOR encryption is used
        encrypted_message = ''.join(chr(ord(char) ^ ord(password[i % len(password)])) for i, char in enumerate(message))
        return encrypted_message

    def decode(self, filename, password):
        # Decode the secretMessage from an audio file
        if filename[-4:] != '.wav':
            filename = filename + '.wav'

        index = 44
        bitsLine, description = '', ''

        try:
            # Read the audio file
            data = open(filename, "rb").read()
            sampleRate = int.from_bytes(data[24:28], byteorder=sys.byteorder)

            for _ in range(sampleRate):
                value = int.from_bytes(data[index:index + 4], byteorder=sys.byteorder, signed=True)
                lsb = bin(value).lstrip('-0b').rjust(8, '0')[-1]
                bitsLine += lsb
                index += 4

                if len(bitsLine) == 8:
                    description += chr(int(bitsLine, 2))
                    bitsLine = ''
                    if description[-6:] == '#1991#':
                        break

            # Decrypt the message using the provided password
            decrypted_message = self.decrypt_message(description[:-6], password)
            if len(decrypted_message) == 0 or description[-6:] != '#1991#':
                messagebox.showerror("Decode Failed", "Message not found or incorrect password.")
                print("\033[31mMessage not found or incorrect password.\033[37m")
                return None
            else:
                print(f"\n\033[32mMessage found:\033[37m\n\n'{decrypted_message}'\n\n\033[33m*** End of Message ***\033[37m")
                return decrypted_message

        except FileNotFoundError as e:
            messagebox.showerror("Decode Failed", f"{e}")
            print(f"\033[31m{e}\033[37]")
            return None

    def decrypt_message(self, encrypted_message, password):
        # Perform decryption here (you can use the same encryption algorithm)
        decrypted_message = ''.join(chr(ord(char) ^ ord(password[i % len(password)])) for i, char in enumerate(encrypted_message))
        return decrypted_message



