import socket
import argparse


class Hacker:

    def __init__(self):
        self.socket = socket.socket()

    def connect(self, ip_address, sock, message):
        hostname = (ip_address, sock)
        self.socket.connect(hostname)
        encoded_message = message.encode()
        self.socket.send(encoded_message)

    def receive_response(self):
        response = self.socket.recv(1024)
        response = response.decode()
        print(response)

    def close_connection(self):
        self.socket.close()

    def __del__(self):
        self.socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let's hack them... Enter victim's IP_address, socket and message")
    parser.add_argument("ip_address")
    parser.add_argument("socket")
    parser.add_argument("message")

    args = parser.parse_args()

    if args.ip_address == "localhost":
        args.ip_address = "127.0.0.1"

    try:
        args.socket = int(args.socket)
    except ValueError:
        print("Socket must be integer value!")
        exit()

    hacky = Hacker()
    hacky.connect(args.ip_address, int(args.socket), args.message)
    hacky.receive_response()
