import socket
host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print("Server listening on port:", port)
connection, address = s.accept()

print("Connection from: "+str(connection))

connection.send(b"Hello! how are you?")
connection.send('bye'.encode())
c.close()