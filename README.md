# Autores
Bruno Falcade Paese e Henrique Mulinari Ambrosi

# Instruções para a compilação
* Instalar a biblioteca socket do python.
* Executar o código com `python file_transfer_socket_server.py` (servidor) e `python file_tranfer_client.py` (cliente).

# Decisões técnicas do projeto

## Uso do buffer de 512B
Essa decisão foi tomada por ser um tamanho comum de bloco em discos rígidos e SSDs. A partir disso foi implementada uma rotina no protocolo de conexão do socket para a requisição de um tamanho de buffer arbitrário. Para que o tempo de transferência pudesse ser determinada foram realizadas 20 execuções para cada tempo e o tamanho inicial de buffer. A partir disso foram obtidos os seuguintes resultados, utilizando um ambiente em uma máquina única:

Média para buffer de 512: 2.1901411652565
Média para buffer de 1024: 1.3032003879547118
Média para buffer de 1536: 1.0508205890655518
Média para buffer de 2048: 0.8393382549285888
Média para buffer de 2560: 0.8729588747024536
Média para buffer de 3072: 0.9792119264602661
Média para buffer de 3584: 0.7549996852874756
Média para buffer de 4096: 0.6173283815383911
Média para buffer de 4608: 0.577573037147522
Média para buffer de 5120: 0.5452069997787475
Média para buffer de 5632: 0.5312787413597106
Média para buffer de 6144: 1.2911431193351746
Média para buffer de 6656: 0.4681749939918518
Média para buffer de 7168: 0.4464470863342285
Média para buffer de 7680: 0.4374024510383606
Média para buffer de 8192: 0.8332826733589173
Média para buffer de 8704: 0.9879615664482116
Média para buffer de 9216: 0.3778756380081177
Média para buffer de 9728: 0.3674954533576965
Média para buffer de 10240: 1.0571035742759705
Média para buffer de 10752: 0.7690808057785035
Média para buffer de 11264: 0.4472958207130432
Média para buffer de 11776: 1.1243668913841247
Média para buffer de 12288: 0.4250732779502869
Média para buffer de 12800: 0.3242043137550354
Média para buffer de 13312: 0.312326180934906
Média para buffer de 13824: 0.3104069471359253
Média para buffer de 14336: 0.2985827803611755
Média para buffer de 14848: 0.30209908485412595