from multiprocessing.connection import Client
from array import array

#references:
	#https://docs.python.org/3.4/library/multiprocessing.html?highlight=process


#connect to local server
address = ('localhost', 8001)

with Client(address, authkey=b'secret password') as conn:

	conn.send("GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")

	data_received = conn.recv()
	print(repr(data_received))
                    

    