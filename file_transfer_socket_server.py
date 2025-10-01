import socket
import time
import os

FILE_NAME = './video.mp4'
BUFFER_SIZE = 4096
filesize = os.path.getsize(FILE_NAME)

def transferirArquivoPorTcp(connection):
    print(f"Iniciando transferência de arquivo {time.time()}")
    connection.send(f"{os.path.basename(FILE_NAME)};{filesize}\n".encode())
    startTime = time.time();
    print (f"Tamanho do arquivo: {filesize}")
    with open(FILE_NAME, "rb") as f:
        size = 0
        while size < filesize:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            connection.send(bytes_read)
            size += len(bytes_read)
            print(f"Enviado: {int(size/filesize * 100)}%", end='\r')
        print(f"Enviado: {int(size/filesize * 100)}%")
        endTime =  time.time();
    print (f"Arquivo transferido")
    connection.send(f'{endTime - startTime}'.encode())

def transferirArquivoPorUdp(sock, client_address):
    print(f"Iniciando transferência de arquivo {time.time()}")
    sock.sendto(f"{os.path.basename(FILE_NAME)};{filesize}\n".encode(), client_address)
    startTime = time.time();
    print (f"Tamanho do arquivo: {filesize}")
    with open(FILE_NAME, "rb") as f:
        size = 0
        while size < filesize:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                print("break")
                break
            sock.sendto(bytes_read, client_address)
            size += len(bytes_read)
            print(f"Enviado: {int(size/filesize * 100)}%", end='\r')
           
        print(f"Enviado: {int(size/filesize * 100)}%")
        endTime =  time.time();
    print (f"Arquivo transferido")
    # sock.sendto(f'{endTime - startTime}'.encode(), client_address)

def menu():
    print("--------MENU--------")
    print("1) Start UDP")
    print("2) Start TCP")
    mode = input("Selecione uma opção: ")

    if (mode.find("1") != -1):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('', 60000))

    if (mode.find("2") != -1):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', 60000))
        server_socket.listen()

    print('Aguardando conexão do cliente para iniciar transferência de arquivo')

    while True:
        try:
            if (mode.find("1") != -1):
                data, client_address = server_socket.recvfrom(100)
                transferirArquivoPorUdp(server_socket, client_address)

            
            if (mode.find("2") != -1):
                connection, client_address = server_socket.accept()
                print('Cliente conectado:', client_address)
                transferirArquivoPorTcp(connection)
                server_socket.close()

        except:
            server_socket.close()


menu()
