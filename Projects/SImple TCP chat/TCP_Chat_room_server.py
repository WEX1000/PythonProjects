import threading
import socket

HOST = "51.83.132.29"
PORT = 6969

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []


def brodecast(message):  # Wysyła wiadomość do wszystkich połączonych użytkowników
    for client in clients:
        client.send(message)


def handle(client):  # Obsługuje połączonego klienta
    while True:
        try:
            message = client.recv(1024)
            brodecast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            client.close()
            brodecast(f'{nickname} left the chat'.encode('ascii'))
            break


def recive():  # Nasłuchuje i łączy klientów z serwerem
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the clinet is {nickname}')
        brodecast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == '__main__':
    print("Server is listening")
    recive()
