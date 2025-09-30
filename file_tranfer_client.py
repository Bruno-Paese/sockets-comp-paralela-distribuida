import socket
import os

BUFFER_SIZE = 512

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 60000))
print("Conectado ao servidor", client_socket.getpeername())


def downloadArquivo(sock, BUFFER_SIZE):
    sock.send(f"{BUFFER_SIZE}".encode())

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
        f.close()
        timeToExecute = sock.recv(BUFFER_SIZE)
        print(f"Execução durou {timeToExecute.decode()} segundos");
    return float(timeToExecute.decode())

times = [0] * 30
runsForAverage = 20

for k in range(1, 30):
    times[k] = 0
    for i in range(1, runsForAverage):
        tte = downloadArquivo(client_socket, BUFFER_SIZE * k)
        times[k] = times[k] + tte
    times[k] = times[k]/runsForAverage
        
for k in range(1, 30):
    print(f"Média para buffer de {BUFFER_SIZE * k}: {times[k]}")

client_socket.close()