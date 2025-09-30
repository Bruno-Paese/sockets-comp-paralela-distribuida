import socket
import os

BUFFER_SIZE = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 60000))
print("Conectado ao servidor", client_socket.getpeername())


def downloadArquivo(sock):
    header = b''
    while b'\n' not in header:
        chunk = sock.recv(BUFFER_SIZE)
        if not chunk:
            raise RuntimeError("Conexão fechada antes de receber o header")
        header += chunk

    nl_index = header.index(b'\n')
    header_bytes = header[:nl_index]        # "nome;filesize"
    rest = header[nl_index+1:]             # possíveis primeiros bytes do arquivo

    try:
        filename_bytes, filesize_bytes = header_bytes.split(b';', 1)
    except ValueError:
        raise RuntimeError("Header mal formatado: " + repr(header_bytes))

    original_name = filename_bytes.decode(errors='replace')
    filesize = int(filesize_bytes.decode())

    out_name = "./downloaded_" + os.path.basename(original_name)

    print(f"[*] Recebendo {out_name} ({filesize} bytes)")

    with open(out_name, "wb") as f:
        received = 0
        # escreve bytes que já chegaram junto com o header
        if rest:
            f.write(rest)
            received += len(rest)

        while received < filesize:
            to_read = min(BUFFER_SIZE, filesize - received)
            chunk = sock.recv(to_read)
            if not chunk:
                raise RuntimeError("Conexão fechada antes do fim do arquivo")
            f.write(chunk)
            received += len(chunk)
            
            print(f"Recebido: {int(received/filesize * 100)}%", end='\r')

while True and client_socket:
    print("--------MENU--------")
    print("1) Download UDP")
    print("2) Download TCP")
    print("3) Exit")
    mode = input("Selecione uma opção: ")

    if (mode.find("1")):
        client_socket.send(b"udp")
        downloadArquivo(client_socket)

    if (mode.find("2")):
        client_socket.send(b"tcp")
        downloadArquivo(client_socket)

    if (mode.find("3")):
        client_socket.send(b"tcp")
        print("Fechando conexão")
        client_socket.close()
