import socket
from threading import Thread
from datetime import datetime

HOST = "127.0.0.1"
PORT = 1234
SEPARATOR = "<SEP>"

clients = {}

def handle_client(client_socket):
    name = client_socket.recv(1024).decode()
    target = client_socket.recv(1024).decode()

    clients[name] = client_socket
    print(f"[+] {name} connected, wants to talk to {target}")

    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break

            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            full_msg = f"[{time_now}] {name}: {msg}"

            if target in clients:
                clients[target].send(full_msg.encode())

        except:
            break

    client_socket.close()
    clients.pop(name, None)
    print(f"[-] {name} disconnected")

def main():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[*] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] Connection from {addr}")
        Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
