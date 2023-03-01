import socket

def enviaDadoTCPIP(data, host, port):
    #abrindo socket para comunicação TCP/IP
    cliente = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    #conecta no servidor
    try:
        cliente.connect( ( host, port ) )

        #envia requisições para o servidor
        cliente.send( data.encode() )

        content = cliente.recv(8192).decode()
        return content

    except Exception as E:
        print(f'Conexão com servidor falhou {E}')
        return E