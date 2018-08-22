    import socket
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 5000))
    server.listen(1)
    while 1:
        (client, address) = server.accept()
        request = ""
        while 1:
            chunk = client.recv(1)
            if chunk:
                request += chunk.decode()
            if request[-4:] == '\r\n\r\n':
                break
            client.close()
            print(request)



