import sys
import socket
import string
import itertools


def establish_connection():
    args = sys.argv
    ip_address, port = args[1], args[2]
    client_socket.connect((ip_address, int(port)))


def generate_password():
    letters = string.ascii_lowercase
    digits = string.digits
    symbols = letters + digits
    for count in range(1, len(symbols) + 1):
        for p in itertools.product(symbols, repeat=count):
            yield ''.join(map(lambda x: str(x), p))


def guessing():
    buff_size = 1024
    for guess_pass in generate_password():
        client_socket.send(guess_pass.encode())
        response = client_socket.recv(buff_size)
        response = response.decode()
        if response == 'Connection success!':
            print(guess_pass)
            break


def main():
    establish_connection()
    guessing()
    client_socket.close()


with socket.socket() as client_socket:
    if __name__ == "__main__":
        main()
