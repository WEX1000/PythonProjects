import tkinter as tk
import socket
import threading

HOST = ""
PORT = 0
stop_thread = False
nickname = ""
password = ""
#----------------------------------------Import, Variable, Server Start------------------------------#
#----------------------------------------------------------------------------------------------------#
#----------------------------------------Main GUI----------------------------------------------------#

class MyGUI:

    def __init__(self):

        self.message = None
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("TCP chat 0.2")

        self.label = tk.Label(self.root, text=f'Logged as: {nickname}', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=10, font=('Arial', 18), state='disabled')
        self.textbox.pack(padx=10, pady=10)

        self.sendbox = tk.Text(self.root, height=1, font=('Arial', 18))
        self.sendbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Send Message", font=('Arial', 18), command=self.send_message)
        self.button.pack(padx=10, pady=10)

        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()
        self.root.mainloop()

    def send_message(self):
        client.send(str(f'{nickname}: ' + self.sendbox.get('1.0', tk.END)).encode('ascii'))
        self.sendbox.delete('1.0', tk.END)

    def display_message(self, message):
        self.textbox.config(state='normal')
        self.textbox.insert(tk.END, message)
        self.textbox.config(state='disabled')
        self.textbox.see(tk.END)
    def receive(self):
        while True:
            if stop_thread:
                break
            try:
                self.message = client.recv(1024).decode('ascii')
                self.display_message(self.message)
            except:
                print("An error occurred!")
                client.close()
                break


#----------------------------------------Main GUI----------------------------------------------------#
#----------------------------------------------------------------------------------------------------#
#----------------------------------------Login Panel-------------------------------------------------#

def send_data():
    global nickname, password, HOST, PORT
    nickname = myentryLogin.get()
    password = myentryPass.get()
    HOST = myentryIP.get()
    PORT = myentryPort.get()
    login.destroy()

login = tk.Tk()
login.geometry("400x550")
login.title("Zaloguj się!")

labelLogin = tk.Label(login, text="Login", font=('Arial', 18)) # Etykieta
labelLogin.pack(padx=20, pady=20)

myentryLogin = tk.Entry(login)
myentryLogin.pack(padx=10, pady=10)

labelPass = tk.Label(login, text="Password", font=('Arial', 18)) # Etykieta
labelPass.pack(padx=20, pady=20)

myentryPass = tk.Entry(login)
myentryPass.pack(padx=10, pady=10)

labelIP = tk.Label(login, text="IP", font=('Arial', 18)) # Etykieta
labelIP.pack(padx=20, pady=20)

myentryIP = tk.Entry(login)
myentryIP.pack(padx=10, pady=10)

labelPort = tk.Label(login, text="PORT", font=('Arial', 18)) # Etykieta
labelPort.pack(padx=20, pady=20)

myentryPort = tk.Entry(login)
myentryPort.pack(padx=10, pady=10)

buttonSend = tk.Button(login, text="Send Message", font=('Arial', 18), command=send_data)
buttonSend.pack(padx=10, pady=10)

login.mainloop()

#----------------------------------------Login Panel-------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, int(PORT)))

MyGUI()
