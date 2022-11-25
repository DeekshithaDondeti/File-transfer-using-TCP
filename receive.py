import socket

Host = input("Host Name: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IP address of the reciever
size=1024  # size of the file to be recieved

client.connect((Host, 12876)) # connecting the socket
print("Connected Successfully")

file= client.recv(100).decode()

with open("./file/" + file, "wb") as file:
    
    for c in range (int(size) +1):
        data = client.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)
file.close()
client.close() # closing the connection