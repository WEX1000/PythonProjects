import tkinter as tk
import socket
import threading
from time import sleep

HOST = '51.83.132.29'
PORT = 2138
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))



class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("TCP chat 0.1")

        self.label = tk.Label(self.root, text="TCP Chat", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=10, font=('Arial', 18), state='disabled')
        self.textbox.pack(padx=10, pady=10)

        self.sendbox = tk.Text(self.root, height=1, font=('Arial', 18))
        self.sendbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Send Message", font=('Arial', 18), command=self.send_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def send_message(self):
        client.send(str(self.sendbox.get('1.0', tk.END)).encode('ascii'))
        self.sendbox.delete('1.0', tk.END)

    def display_message(self, message):
        self.textbox.config(state='normal')
        self.textbox.insert(tk.END, message + '\n')
        self.textbox.config(state='disabled')
        self.textbox.see(tk.END)

MyGUI()
