import socket
import time
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 60000))
server_socket.listen()

FILE_NAME = '/home/bruno/Vídeos/VIDEO/180123000/131429AA.MP4'
BUFFER_SIZE = 4096
filesize = os.path.getsize(FILE_NAME)

def transferirArquivo(connection):
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

        endTime =  time.time();
        print(f"Arquivo {FILE_NAME} enviado com sucesso. Transferencia durou {endTime - startTime} segundos")
    # connection.send(b"\\endfile", b'{endTime - startTime}')

print('Aguardando conexão do cliente para iniciar transferência de arquivo')
connection, client_address = server_socket.accept()
print('Cliente conectado:', client_address)

while True: 
    try:
        # while True:
        data = connection.recv(1024)
        print('Mensagem recebida:', data.decode())
        # if data.decode() == 'sair':
        #     break
        if data.decode() == 'udp':
            print("Iniciando transferência UDP")
            transferirArquivo(connection)
        if data.decode() == 'tcp':
            print("Iniciando transferência TCP")
            transferirArquivo(connection)
        if data.decode() == 'exit':
            print("Encerrando conexão")
            server_socket.close()
        
    except:
        print("Ocorreu uma exceção!")
        server_socket.close()
        break