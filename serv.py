import socket


s=socket.socket() #IPV4 ,TCP connection optional
print('Socket created')

s.bind(('localhost',9999)) #Ip , port number 

s.listen(3) # set to connect to 3 differnt client connections 
print("waiting for connections...")

while True:
 	c, addr = s.accept() #client socket= c addr= IP address 
 	name = c.recv(1024).decode() # recieve messege from client 1024 bytes and decode it

 	print("Connected with" , addr, name) #address and name of client 
 	c.send(bytes('Welcome to Issacs server','utf-8')) #utf -8 format to send to client in bytes 
 	c.close()

