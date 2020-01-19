import socket 

'''references:
	https://docs.python.org/3/library/socket.html
	https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
	https://wiki.python.org/moin/TcpCommunication'''

host = "www.google.com" 
port = 80
buffer_size = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

#connect to host
client.connect((host,port))  
 
#send get request
request = "GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n"
client.send(request.encode())
 
#ouput result of get request
data = client.recv(buffer_size) 
print(repr(data))

#close connection
client.close() 

