import socket, threading

HOST = '127.0.0.1'
PORT = 55555
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

clients = []
nicknames = []
users = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            # Broadcast message
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove and close the client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        if len(clients) <= 1:
            # Accept connection
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            # Request and store nickname
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)
            users.append(clients.index(client)+1)

            # Print and broadcast nickname
            print(f"Nickname is {nickname}")
            print(f"User is {users[clients.index(client)]}")
            broadcast(f"{nickname} joined the chat!".encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            # Start handling thread for client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        else:
            pass

print("Server is listening...")
receive()