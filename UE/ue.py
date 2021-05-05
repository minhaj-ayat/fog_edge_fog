import socket

authenticated = False

ffogs = socket.socket()
# Define the port on which you want to connect
port = 21000

# connect to the server on local computer
ffogs.connect(('127.0.0.1', port))

imsi = "111501234512345"
ffogs.send(imsi.encode())
print("UE sent attach request : " + imsi)

challenge = ffogs.recv(1024).decode()
print("UE received challenge from Foreign fog : " + challenge)

res = "a54211d5e3ba50bf"
ffogs.send(res.encode())
print("UE sent RES to foreign fog : " + res)

msg = ffogs.recv(1024).decode()
print("Msg from Foreign fog : " + msg)

if msg == "200 ok":
    authenticated = True
