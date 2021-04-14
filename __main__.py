import socket
import _thread
IP = "192.168.194.10"
PORT = 8080
BUFFERSIZE = 8192
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((IP, PORT))

def listenMessages(conn):
    print(conn.recv(BUFFERSIZE).decode())
_thread.start_new_thread(listenMessages, (c,))
while True:
    inp = str(input(""))
    c.sendall(inp.encode())
    print(c.recv(BUFFERSIZE).decode())