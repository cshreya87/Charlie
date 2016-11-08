#Group Name : Charlie
#Rinku Chowdhury : 216101118
#M.Rauf Qureshi : 216100729
#Shreya Chatterjee : 216100848
import socket
import sys
import re
HOST = 'localhost'
PORT = 8080 
_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	_socket.connect((HOST, PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

	#Start listening 



while 1:
#wait to accept a connection - blocking call
	print 'Please enter that Name'
	_Name=raw_input()
	print 'Please enter that Age'
	_Age=raw_input()
	print 'Please enter that Name'
	_Matrikelnummer=raw_input()
	_socket.sendall(_Name+'::'+_Age+'::'+_Matrikelnummer)	
	reply= _socket.recv(1024)
	lk = "\n".join(reply.split("\r\n"))
	print lk
	

conn.close()

_socket.close()