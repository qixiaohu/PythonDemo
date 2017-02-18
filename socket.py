#coding:utf-8


#import socket
from socket import *

myhost=""
myport=8080

if __name__=="__main__":

    sock = socket(AF_INET, SOCK_STREAM)

    sock.bind((myhost, myport))

    sock.listen(128)

    while True: 
        cfd, address = sock.accept()
        print "remote ip: "+ str(address[0])
        print "remote port: "+ str(address[1])

        while True:
            data = cfd.recv(1)
            if not data:
                break 
            cfd.send("echo:"+data)

        cfd.close()

    sock.close()
            
            

