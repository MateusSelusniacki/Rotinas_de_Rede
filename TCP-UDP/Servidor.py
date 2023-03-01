import socket
import datetime

def listening(ip,port,TCP_UDP = 'TCP'):
    print(f'Esperando no ip: {ip}:{port}')
    #abrindo socket para comunicação TCP/IP
    if(TCP_UDP == 'TCP'):
        server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    else:
        server = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

    #fazendo bind do ip e porta
    #server.bind( ( 'localhost', 50055 ) )
    server.bind ( (ip,port) )

    #listen
    print("Esperando cliente")
    server.listen(1)

    #cria looping de conexão com o cliente
    while(1):
        try:
            #aceita conexão
            connection, address = server.accept()
            print(f"Conexão aceita {datetime.datetime.now()}")

            #recebe dados do cliente e transforma em string
            content = connection.recv(8192).decode()
            
            #verifica se ainda há comunicação
            if not content:
                break
            else:
                print("Dado recebido: ", content )

            #envia dados
            connection.send( ("200 - Dado recebido").encode() )
            print('\n')
        except Exception as E:
            print(E)