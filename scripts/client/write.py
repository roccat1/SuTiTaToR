import scripts.client.client as client

import socket

def write():
    while True:
        if client.msg:
            client.client.send(client.msg.encode('ascii'))
            client.msg = None
        else:
            pass