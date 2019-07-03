import socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'micheal',b'tracy',b'sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close