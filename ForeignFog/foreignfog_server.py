import socket
from _thread import *
import threading

authenticated = False


def threaded(c):
    received_imsi = c.recv(1024).decode()
    print("Foreign fog Received imsi from UE : " + received_imsi)

    # Create a socket object
    proxyidps = socket.socket()
    # Define the proxy port on which you want to connect
    port = 22000
    # connect to the server on local computer
    proxyidps.connect(('127.0.0.1', port))
    proxyidps.send(received_imsi.encode())

    auth_challenge = proxyidps.recv(1024)
    print("Received auth_challenge: " + auth_challenge.decode())

    c.send(auth_challenge)
    print("Sent auth_challenge to UE : " + auth_challenge.decode())

    received_res = c.recv(1024)
    print("Received RES from UE : " + received_res.decode())

    proxyidps.send(received_res)
    print("Sent RES to ProxyIDP : " + received_res.decode())

    msg = proxyidps.recv(1024)
    print("Received msg from proxyidp : " + msg.decode())

    c.send(msg)
    print("Sent msg to UE : " + msg.decode())

    print_lock.release()
    # close the connection
    proxyidps.close()
    # Close the connection with the client
    c.close()


print_lock = threading.Lock()
# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 21000

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("foreignfog socket binded to %s" % port)

# put the socket into listening mode
s.listen(5)
print("foreignfog socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    cl, addr = s.accept()
    print_lock.acquire()
    print('Got connection from', addr)
    start_new_thread(threaded, (cl,))
