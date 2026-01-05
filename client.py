import socket
from threading import Thread

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 1234

client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))

name = input("Enter your name: ")
client_socket.send(name.encode())

target = input("Who are you going to talk to: ")
client_socket.send(target.encode())

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

Thread(target=receive, daemon=True).start()

while True:
    msg = input()
    client_socket.send(msg.encode())
