import socket


c=socket.socket()

c.connect(('localhost',9999)) #connecting with local host with Port number 

while True:
    name=input("Enter your name")
    c.send(bytes(name,'utf-8')) # sending your name in utf-8 format to server 
    print(c.recv(1024).decode()) #Receiving message from server and decoding it