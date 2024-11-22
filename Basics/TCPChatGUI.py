import tkinter as tk
import socket
import threading


HOST = '127.0.0.1'
PORT = 2140
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

stop_thread = False
nickname = ""
password = ""


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



def receive():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print("Connection was refuse! Wrond password!")
                        stop_thread = True
                elif next_message == 'BAN':
                    print('Connection refused because of ban!')
                    client.close()
                    stop_thread = True
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    global stop_thread
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input("")}'
        if message == f'{nickname}: exit':
            stop_thread = True
        if message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin':
                if message[len(nickname)+2:].startswith('/kick'):
                    client.send(f'KICK {message[len(nickname) + 2 + 6:]}'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/ban'):
                    client.send(f'BAN {message[len(nickname) + 2 + 5:]}'.encode('ascii'))
            else:
                print("Commands can only be executed by admin!")
        else:
            client.send(message.encode('ascii'))

def send_data():
    global nickname, password
    nickname = myentryLogin.get()
    password = myentryPass.get()
    login.destroy()

login = tk.Tk()
login.geometry("350x350")
login.title("Zaloguj się!")

labelLogin = tk.Label(login, text="Login", font=('Arial', 18)) # Etykieta
labelLogin.pack(padx=20, pady=20)

myentryLogin = tk.Entry(login)
myentryLogin.pack(padx=10, pady=10)

labelPass = tk.Label(login, text="Password", font=('Arial', 18)) # Etykieta
labelPass.pack(padx=20, pady=20)

myentryPass = tk.Entry(login)
myentryPass.pack(padx=10, pady=10)

buttonSend = tk.Button(login, text="Send Message", font=('Arial', 18), command=send_data)
buttonSend.pack(padx=10, pady=10)

login.mainloop()



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

MyGUI()
