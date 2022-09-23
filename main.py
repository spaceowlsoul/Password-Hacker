import sys
import socket
import itertools


def establish_connection():
    args = sys.argv
    ip_address, port = args[1], args[2]
    client_socket.connect((ip_address, int(port)))


def generate_password():
    with open('passwords.txt', 'r') as file:
        for line in file:
            if not line.isdigit():
                for p in itertools.product(*([letter.lower(), letter.upper()] for letter in line.rstrip('\n'))):
                    yield ''.join(p)
            else:
                yield line


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
