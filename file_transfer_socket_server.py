import socket
import time
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 60001))
server_socket.listen()

FILE_NAME = './file_tranfer_client.py'
BUFFER_SIZE = 16

print('Aguardando conexão do cliente para iniciar transferência de arquivo')
connection, client_address = server_socket.accept()
filesize = os.path.getsize(FILE_NAME)

def transferirArquivo(connection):
    print(f"Iniciando transferência de arquivo {time.time()}")
    connection.send(f"{os.path.basename(FILE_NAME)};{filesize}\n".encode())
    print (filesize)
    with open(FILE_NAME, "rb") as f:
        size = 0
        while size < filesize:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            connection.send(bytes_read)
            size += len(bytes_read)

        print(f"[+] File {FILE_NAME} sent successfully")


try:
    # while True:
    print('Cliente conectado:', client_address)
    data = connection.recv(1024)
    print('Mensagem recebida:', data.decode())
    # if data.decode() == 'sair':
    #     break
    # if data.decode() == 'baixar':
    transferirArquivo(connection)
    connection.close()

    print("Cliente solicitou desconexão")
    
except:
    print("Ocorreu uma exceção!")
    server_socket.close()
finally:
    print("Saindo...")
    server_socket.close()