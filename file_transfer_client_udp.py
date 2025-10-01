import socket
import os

BUFFER_SIZE = 512
SERVER_ADDR = ('127.0.0.1', 60000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def downloadArquivo(sock, BUFFER_SIZE):
    # request file with buffer size info
    sock.sendto(f"{BUFFER_SIZE}".encode(), SERVER_ADDR)

    # receive header first (blocking until we get it)
    header, _ = sock.recvfrom(BUFFER_SIZE)
    try:
        filename_bytes, filesize_bytes = header.split(b';', 1)
    except ValueError:
        raise RuntimeError("Header mal formatado: " + repr(header))

    original_name = filename_bytes.decode(errors='replace')
    filesize = int(filesize_bytes.decode())

    out_name = "./downloaded_" + os.path.basename(original_name)
    print(f"[*] Recebendo {out_name} ({filesize} bytes)")

    with open(out_name, "wb") as f:
        received = 0
        while received < filesize:
            to_read = min(BUFFER_SIZE, filesize - received)
            chunk, _ = sock.recvfrom(to_read + 64)  # UDP might merge or split differently
            if not chunk:
                raise RuntimeError("Socket fechado antes do fim do arquivo")
            f.write(chunk)
            received += len(chunk)
            print(f"Recebido: {int(received/filesize * 100)}%", end='\r')

        # espera mensagem de tempo de execução
        timeToExecute, _ = sock.recvfrom(BUFFER_SIZE)
        print(f"\nExecução durou {timeToExecute.decode()} segundos")

    return float(timeToExecute.decode())

times = [0] * 25
runsForAverage = 10  # reduzido para não sobrecarregar UDP

for k in range(1, 25):
    times[k] = 0
    for i in range(1, runsForAverage):
        tte = downloadArquivo(client_socket, BUFFER_SIZE * k)
        times[k] += tte
    times[k] = times[k] / runsForAverage
        
for k in range(1, 25):
    print(f"Média para buffer de {BUFFER_SIZE * k}: {times[k]}")

client_socket.close()
