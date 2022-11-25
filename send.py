import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IP address of the sender
server.bind((socket.gethostname(), 12876)) #creating sockect using ipaddress and port number
server.listen(5)
size=1024  #size of the file to be sent
print("Host Name: ", server.getsockname())

sock, addr = server.accept()
file = input("File Name:") # giving the name of the file to transfer

sock.send(file.encode()) # sending the file 
sock.send(str(size).encode()) #sending the size size of the file to transfer

with open(file, "rb") as file: # openng the folder ehere the file has to be transfered
    
    for c in range (int(size) +1):  
        res = file.read(1024)
        if not (res):
            break
        sock.sendall(res)
        c = c + len(res)
file.close() 
server.close() # removing the connection