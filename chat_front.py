from base64 import encode
import socket 

sock = socket.socket()
sock.connect(('localhost', 9090))

name = input('Enter name: ')
sock.send(name.encode(encoding='UTF-8'))
print( "Binding successful!")


data = sock.recv(1024).decode(encoding='UTF-8')
sock.send(name.encode(encoding='UTF-8'))


data=sock.recv(1024).decode(encoding = 'UTF-8')
#print (data)
sock.send(name.encode())
while True:
    message = input('Me : ')
    sock.send(message.encode())
    message = sock.recv(1024)
    message = message.decode()
    print(data, ':', message)




