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
	_socket.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

	#Start listening 
_socket.listen(10)

conn, addr = _socket.accept()
while 1:
		reply= conn.recv(1024)
		if len(reply)>1:
			a=reply.split('::')
			data= 'Name: '+str(a[0])+';\n' + 'Age: '+str(a[1])+';\n' + 'Matrikelnummer: '+str(a[2])+'\n'
			conn.sendall(data)
			print str(data)+'/n'
	

conn.close()

_socket.close()