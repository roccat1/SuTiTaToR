import socket, threading

import scripts.client.client as client
import scripts.log as log
import scripts.UI as UI
import scripts.client.write as write

def connect(host, port, nick):
    client.nickname = nick

    client.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.client.connect((host, port))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write.write)
    write_thread.start()

def receive():
    while True:
        try:
            # Receive message from server
            message = client.client.recv(1024).decode('ascii')
            if message == 'NICK':
                # Send nickname to server
                client.client.send(client.nickname.encode('ascii'))
            else:
                log.log("[INFO] " + message)
                try:
                    UI.execute_board_change(int(message.split(";")[1]), int(message.split(";")[2]), int(message.split(";")[3]), int(message.split(";")[4]))
                except:
                    log.log("[ERROR] operation failed")
        except Exception as e:
            # Close connection when error
            log.log("[ERROR] " + str(e))
            log.log("[ERROR] Server disconnected")
            client.client.close()
            break