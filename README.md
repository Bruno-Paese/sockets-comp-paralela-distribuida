# Autores
Bruno Falcade Paese e Henrique Mulinari Ambrosi

# Instruções para a compilação
* Instalar a biblioteca socket do python.
* Executar o código com `python file_transfer_socket_server.py` (servidor) e `python file_tranfer_client.py` (cliente).

# Decisões técnicas do projeto

## Uso do buffer de 4096B
Essa decisão foi tomada por ser um tamanho comum de bloco em discos rígidos e SSDs. Além disso, o buffer do cliente não gera um overhead de pacotes na rede, mas também não desperdiça memória.

## Resultados

Fazendo a transferência de um computador para outro, o UPD teve o seguinte resultado

```
[*] Recebendo ./downloaded_video.mp4 (17839845 bytes)
Recebido: 100%
Execução durou 3.1330199241638184 segundos
```

Já o TCP obteve o seguinte

```
[*] Recebendo ./downloaded_video.mp4 (17839845 bytes)
Execução durou 12.331703424453735 segundos
```
