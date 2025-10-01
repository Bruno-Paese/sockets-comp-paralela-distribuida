import socket
import time
import os

FILE_NAME = '/home/bruno/Vídeos/VIDEO/180123000/131429AB.MP4'
BUFFER_SIZE = 512
filesize = os.path.getsize(FILE_NAME)

def transferirArquivo(connection, buffer_size):
    print(f"Iniciando transferência de arquivo {time.time()}")
    connection.send(f"{os.path.basename(FILE_NAME)};{filesize}\n".encode())
    startTime = time.time();
    print (f"Tamanho do arquivo: {filesize}")
    with open(FILE_NAME, "rb") as f:
        size = 0
        while size < filesize:
            bytes_read = f.read(buffer_size)
            if not bytes_read:
                break
            connection.send(bytes_read)
            size += len(bytes_read)

        endTime =  time.time();
    connection.send(f'{endTime - startTime}'.encode())

def menu():
    print("--------MENU--------")
    print("1) Start UDP")
    print("2) Start TCP")
    print("3) Exit")
    mode = input("Selecione uma opção: ")

    if (mode.find("1") != -1):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('', 60000))
        server_socket.listen()

    if (mode.find("2") != -1):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', 60000))
        server_socket.listen()

    print('Aguardando conexão do cliente para iniciar transferência de arquivo')
    connection, client_address = server_socket.accept()
    print('Cliente conectado:', client_address)
    while True:
        try:
            buffer_size = connection.recv(100);
            transferirArquivo(connection, int(buffer_size.decode()))

        except:
            server_socket.close()


menu()
