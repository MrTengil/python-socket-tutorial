import socket
import threading

HEADER = 64
PORT = 5151
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "213.89.156.227"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"

server = socket.socket(socket.AF_INET)
server.bind(ADDR)

def handle_client(conn, addr):  # Will run for each client
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg recieved".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is lsitening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[Starting] server is starting...")
start()