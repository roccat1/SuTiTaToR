import scripts.client.client as client

import time

def write():
    while True:
        if client.msg:
            client.client.send(client.msg.encode('ascii'))
            client.msg = None
        else:
            pass
        time.sleep(0.1)