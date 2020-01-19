import socket 
from multiprocessing.connection import Listener
from array import array

'''references:
	https://docs.python.org/3/library/socket.html
	https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
	https://wiki.python.org/moin/TcpCommunication
	https://docs.python.org/3.4/library/multiprocessing.html?highlight=process'''


#create server with local client
address = ('localhost', 8001)     # family is deduced to be 'AF_INET'

with Listener(address, authkey=b'secret password') as listener:
	with listener.accept() as conn:
		print('connection accepted from', listener.last_accepted)
		data_received = conn.recv()
		print(repr(data_received))

		#connect to google
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
		s.connect(("www.google.com",80))  

		#send info from local client to google
		s.send(data_received.encode())

		#return response from google
		google_response = s.recv(1024) 
		print(repr(google_response))

		#close connection with google
		s.close() 

		#send google's response back to local client
		conn.send(google_response)
