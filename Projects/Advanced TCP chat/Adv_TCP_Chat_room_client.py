import socket
import threading

HOST = input("IP Adress: \n")
PORT = int(input("Podaj port: \n"))

nickname = input("Choose a nickname: \n")
if nickname == 'admin':
    password = input("Enter password for admin: \n")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

stop_thread = False

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
    while True:
        global stop_thread
        if stop_thread:
            break
        text = input("")
        if text == "exit":
            stop_thread = True
        message = f'{nickname}: {text}'
        if message[len(nickname)+2].startswith('/'):
            if nickname == 'admin':
                if message[len(nickname)+2].startswith('/kick'):
                    client.send(f'KICK {message[len(nickname) + 2 + 6:]}'.encode('ascii'))
                elif message[len(nickname)+2].startswith('/ban'):
                    client.send(f'BAN {message[len(nickname) + 2 + 5:]}'.encode('ascii'))
            else:
                print("Commands can only be executed by admin!")
        else:
            client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write())
write_thread.start()