import socket

'''references:
	https://docs.python.org/3/library/socket.html
	https://wiki.python.org/moin/TcpCommunication'''

#local host
host = '127.0.0.1'

port = 8001
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#allow it to reuse the same bind port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()

#print connection information
print('Connection address:', addr)

#listen for data and print what it receives
while True:
	data = conn.recv(buffer_size)
	if not data: break

	#print information received from the client
	print("Received data:", data)
	
	#echo
	conn.send(data)
conn.close()
