import telnetlib

def telnet(host, port, user, password, command):
    #definindo timeout
    timeout = 20

    #usuario e senha
    user = user
    password = password

    #inicia conexão via ip
    tn = telnetlib.Telnet(host)

    #open no ip e porta
    tn.open(host,port, timeout)

    #insere o usuario
    tn.read_until(b"User:")
    tn.write(user.encode('ascii') + b"\r\n")

    #insere a senha
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\r\n")

    #envia o comando de trigger (se8)
    tn.read_until(b"Logged")
    tn.write(command.encode('ascii') + b"\r\n")

    #finaliza a conexão
    tn.close()

telnet("localhost",7000,"user","password","dado")