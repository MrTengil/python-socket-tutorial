import socket
import time
HEADER = 64
PORT = 5050
FORMAT ='utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = "192.168.99.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    t = time.time()
    client.send(send_length)
    client.send(message)
    print(client.recv(1).decode(FORMAT))
    elapsed = (time.time() - t)*1000
    print(f"Latency: {elapsed} ms")

send('A')
input()

send(DISCONNECT_MESSAGE)