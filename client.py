import socket
from threading import Thread

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 1234

client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    name = input("Enter your name: ").strip()
    if name:
        break
client_socket.send(name.encode())

while True:
    target = input("Who are you going to talk to: ").strip()
    if target:
        break
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
    if msg.lower() == "/exit":
        client_socket.close()
        print("Disconnected from server")
        break
    client_socket.send(msg.encode())
