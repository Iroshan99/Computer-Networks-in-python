import socket

port=1234
address="localhost"
BUF_SIZE=1024

con=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
con.connect((address,port))

data=con.recv(BUF_SIZE)
con.close()
print(data.decode("utf-8"))