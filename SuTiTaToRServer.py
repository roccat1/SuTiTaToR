import socket, threading

# find ip of the user without socket
HOST = socket.gethostbyname(socket.gethostname())

PORT = 5050

#if exists file names "ip.txt" read ip from it
try:
    with open("ip.txt", "r") as f:
        HOST = f.read()
except:
    pass

#if exists file names "port.txt" read port from it
try:
    with open("port.txt", "r") as f:
        PORT = int(f.read())
except:
    pass

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

            #send player number
            client.send(f"PLAYER{clients.index(client)+1}".encode('ascii'))

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

if __name__ == "__main__":
    print("Server is listening...")
    print(f"to connect, IP: {HOST} PORT: {PORT}")
    receive()

