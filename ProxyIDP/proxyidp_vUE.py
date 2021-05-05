import socket
from _thread import *
import threading

autn = ""
rand = ""


def threaded(c):
    received_imsi = c.recv(1024).decode()
    print("Received UE imsi from foreign fog : " + received_imsi)

    # Create a socket object
    edges = socket.socket()

    # Define the port on which you want to connect
    port = 12000

    # connect to the server on local computer
    edges.connect(('127.0.0.1', port))

    # receive data from the server
    # print(s.recv(1024))
    edges.send(received_imsi.encode())
    print("Sent IMSI to Edge : " + received_imsi)

    received_challenge = edges.recv(1024)
    print("Received Auth. Challenge from Edge : " + received_challenge.decode())

    global autn
    global rand
    autn = received_challenge.decode().split()[0]
    rand = received_challenge.decode().split()[1]

    c.send(received_challenge)
    print("Sent Auth. Challenge to Foreign fog: " + received_challenge.decode())

    received_res = c.recv(1024)
    print("Recieved RES from Foreign fog : " + received_res.decode())

    edges.send(received_res)
    print("Sent RES to Edge: " + received_res.decode())

    msg = edges.recv(1024)
    print("Received msg from Edge : " + msg.decode())

    c.send(msg)
    print("Sent msg to foreign fog :" + msg.decode())

    print_lock.release()
    # close the connection
    edges.close()


print_lock = threading.Lock()
idpsock = socket.socket()
print("ProxyIDP Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 22000

idpsock.bind(('', port))
print("Proxy socket binded to %s" % port)

# put the socket into listening mode
idpsock.listen(5)
print("Proxy socket is listening")

while True:
    cl, addr = idpsock.accept()
    print_lock.acquire()
    print('Got connection from', addr)
    start_new_thread(threaded, (cl,))
