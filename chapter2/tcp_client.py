#! /usr/bin/python3

import socket
import ssl

target_name = "www.finiq.com"
target_port = 443
data = "GET /uploads HTTP/1.1\r\nHost:finiq.com\r\n\r\nUser-Agent:GoogleBot;echo\r\n"
if target_port == 80:
    # client for http..
    # create the socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the host
    client.connect((target_name, target_port))
    # send the data
    client.send(data.encode('UTF-8'))
    # receive the data
    response = client.recv(4096)
    print(response.decode())

else:
    # client for https..
    context = ssl.create_default_context()
    with socket.create_connection((target_name, target_port)) as sock:
        with context.wrap_socket(sock, server_hostname=target_name) as ssock:
            ssock.send(data.encode())

            # receive some data
            response = ssock.recv(4096)
            print(response.decode())
    
