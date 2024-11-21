import tkinter as tk
import socket
import threading



HOST = '51.83.132.29'
PORT = 2141

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="TCP Chat 0.1", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 18))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        client.send(str(self.textbox.get('1.0', tk.END)).encode('ascii'))

MyGUI()
