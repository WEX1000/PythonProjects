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
            msg = message = client.recv(1024)
            if msg.decode('ascii').startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_kick = msg.decode('ascii')[5:]
                    kick_user(name_to_kick)
                else:
                    client.send('Command was refused!'.encode('ascii'))
            elif msg.decode('ascii').startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_ban = msg.decode('ascii')[4:]
                    kick_user(name_to_ban)
                    with open('bans.txt', 'a') as f:
                        f.write(f'{name_to_ban}')
                    print(f'User {name_to_ban} was banned!')
                else:
                    client.send('Command was refused!'.encode('ascii'))
            else:
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

        with open('bans.txt', 'r') as f:
            bans = f.readline()

        if nickname+'\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        if nickname == 'admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')

            if password != 'pass':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue


        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the clinet is {nickname}')
        brodecast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send('You were kicked by the admin!'.encode('ascii'))
        client_to_kick.close()
        nicknames.remove(name)
        brodecast(f'{client_to_kick} was kicked!')


def ban_user(a):
    print(a)
if __name__ == '__main__':
    print("Server is listening")
    recive()
