# Autores
Bruno Falcade Paese e Henrique Mulinari Ambrosi

# Instruções para a compilação
* Instalar a biblioteca socket do python.
* Executar o código `python file_transfer_socket_server.py` para iniciar o servidor (o arquivo do servidor é o mesmo para UDP e TCP)
* Selecionar 1 ou 2 para decidir rodar o servidor com UDP ou TCP
* Executar o código `python file_transfer_client_udp.py` e `python file_transfer_client_tcp.py` para executar o cliente UDP e TCP respectivamente

Lembre se de configurar o IP do servidor em ambos os arquivos de cliente. As portas já estão pré configuradas para a 60000, mas podem ser alteradas no cliente e servidor.

# Decisões técnicas do projeto

## Uso do buffer de 4096B
Essa decisão foi tomada por ser um tamanho comum de bloco em discos rígidos e SSDs. Além disso, o buffer do cliente não gera um overhead de pacotes na rede, mas também não desperdiça memória.

## Resultados

Fazendo a transferência de um computador para outro em uma mesma rede, o UPD teve o seguinte resultado

```
[*] Recebendo ./downloaded_video.mp4 (17839845 bytes)
Execução durou 3.1330199241638184 segundos
```

Já o TCP obteve o seguinte

```
[*] Recebendo ./downloaded_video.mp4 (17839845 bytes)
Execução durou 12.331703424453735 segundos
```

