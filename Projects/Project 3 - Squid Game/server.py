import socket
from threading import Thread
from util import IP, PORT, BYE, PACKET
from BullsCode import BullsCode
import datetime


server_socket = socket.socket()
server_socket.bind((IP, PORT))
server_socket.listen()
print(f"Server is up and running! on: {IP}:{PORT}")
serverCode = BullsCode()
print(f"Server code is: {serverCode.get_code()}")

def eco(client_socket):
    data = None
    while data != BYE:
        data = client_socket.recv(PACKET).decode()
        print("Client sent: " + data)

        if data != BYE:
            client_socket.send(f"{data} to you too. I eco your message: ".encode())
    client_socket.send("BYE! press enter to close".encode())
    client_socket.close()



def client_thread(client,startTime):
    print(f"Client connected! ({client[1]})")
    client_socket = client[0]
    client_socket.send("Welcome to the Server. Enter your first guess: ".encode())
    counter = 2
    while counter <= 10 and (datetime.datetime.now()-startTime).total_seconds()/60 <= 6:
        timer = datetime.datetime.now()
        data = client_socket.recv(1024).decode()
        if (datetime.datetime.now()-timer).total_seconds() > 30.0:
            break
        if data == BYE:
            client_socket.send("BYE! press enter to close".encode())
            client_socket.close()
            return
        try:
            answer = serverCode.check(BullsCode(data))
            if answer == ['B','B','B','B']:
                client_socket.send(f"You won at your {counter} attempt! Now I am an eco server: ".encode())
                WON = True
                eco(client_socket)
                return
            else:
                client_socket.send(f"You got: {answer}. Enter your {counter} guess: ".encode())
                counter += 1
        except:
            client_socket.send(f"Invalid guss. Try again. Enter your {counter} guess:".encode())
    client_socket.send(f"No more guesses. BYE! press enter to close".encode())
    client_socket.close()


while True:
    startTime = datetime.datetime.now()
    Thread(target=client_thread, args=(server_socket.accept(),startTime,)).start()
