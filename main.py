import socket

target_host =  "insira seu host"
target_port = 80

#objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conectar com o cliente
client.connect((target_host,target_port))

#Envio de dados
client.send(b"GET / HTTP/1.1\r\nHost: hostinserido\r\n\r\n")

#Recebimento de dados
response = client.recv(4096)

print(response.decode())
client.close()

