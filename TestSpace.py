import tkinter as tk
import socket
import threading

HOST = ""
PORT = 0
stop_thread = False
nickname = ""
password = ""

def send_data():
    global nickname, password, HOST, PORT
    nickname = myentryLogin.get()
    password = myentryPass.get()
    HOST = myentryIP.get()
    PORT = myentryPort.get()
    login.destroy()

login = tk.Tk()
login.geometry("400x200")
login.title("Zaloguj się!")

frame = tk.Frame(login)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

labelLogin = tk.Label(frame, text="Login", font=('Arial', 18)) # Etykieta
labelLogin.grid(row=0, column=0, sticky=tk.W+tk.E)

myentryLogin = tk.Entry(frame)
myentryLogin.grid(row=1, column=0, sticky=tk.W+tk.E)

labelPass = tk.Label(frame, text="Password", font=('Arial', 18)) # Etykieta
labelPass.grid(row=2, column=0, sticky=tk.W+tk.E)

myentryPass = tk.Entry(frame)
myentryPass.grid(row=3, column=0, sticky=tk.W+tk.E)

labelIP = tk.Label(frame, text="IP", font=('Arial', 18)) # Etykieta
labelIP.grid(row=0, column=1, sticky=tk.W+tk.E)

myentryIP = tk.Entry(frame)
myentryIP.grid(row=1, column=1, sticky=tk.W+tk.E)

labelPort = tk.Label(frame, text="PORT", font=('Arial', 18)) # Etykieta
labelPort.grid(row=2, column=1, sticky=tk.W+tk.E)

myentryPort = tk.Entry(frame)
myentryPort.grid(row=3, column=1, sticky=tk.W+tk.E)

buttonSend = tk.Button(login, text="Confirm", font=('Arial', 18), command=send_data)
buttonSend.pack(padx=10, pady=10)

frame.pack(fill='x')
login.mainloop()