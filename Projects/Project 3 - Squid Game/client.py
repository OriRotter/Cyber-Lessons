from util import IP, PORT, PACKET
import socket

client_socket = socket.socket()
client_socket.connect((IP, PORT))
print(f"Connected to: {IP}:{PORT}.")

while True:
    try:
        data = client_socket.recv(PACKET).decode()
        message = input(f"{data}")
        client_socket.send(message.encode())
    except ConnectionAbortedError:
        print("Disconnected from the server.")
        break
