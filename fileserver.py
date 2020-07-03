import socket

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print("Server listening on port:",port)
c, addr = s.accept()
filename = c.recv(1024)

try:
    f = open(filename,'rb')
    content=f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    print("File does not exist")
    c.send(b"file does not exist")
c.close()
