from http import client
import socket 
#import tkinter
#tk=tkinter()


sock = socket.socket ()
#sock.bind (('',5050)) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Несколько прог слушают сокет
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)#Шировещательные пакеты
#client_adress=[] #Храним данные адерсов пользователей


#tk.title('Djungarik notSafe Messenger')
#tk.geometry('500X600')
#text_meesange=tkinter.StringVar()
#nick=tkinter.StringVar()
#text_meesange.set('')

host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 9090
sock.bind(('localhost', port))
print( "Binding successful!")
print("This is your IP: ", s_ip)
sock.listen() 

conn, add =sock.accept()
print('address unit:', add)

name = input('Enter name: ')
data = conn.recv(1024).decode(encoding='UTF-8')
conn.send(name.encode(encoding='UTF-8'))




print('Connection Established. Connected From: ',add[0])



conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(data, ':', message)







