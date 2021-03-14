#!/usr/bin/env python3
import socket
import sys

#connect to server
#print(sys.argv[2])

#serv_address = ('192.171.20.84', 12345)
serv_host = '192.171.20.84'
serv_port = 12345
#serv_host = sys.argv[4]
#serv_port = int(sys.argv[2])
#case_id = sys.argv[5]
#case_id = sys.argv[3]
if (int(sys.argv[2]) == 12345) :
	if (sys.argv[4] == '192.171.20.84' or sys.argv[4] == 'pc4.geni.case.edu') :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((serv_host, serv_port))
else:
	print("invalid port/address")
	

#initiate contact with server and send first message
try :

	msg = 'csds325spring2021 HELLO emw119 \n'
	s.sendall(msg.encode('utf-8'))

	response = s.recv(1024)
	r = response.decode()
	

	text1 = r.split()
	#print(text1)
	head = "csds325spring2021"
	#math = ""
	answer = 0
	#print(text1)
	
	if (text1[0] != "csds325spring2021"):
		print("invalid message")
		s.close()
	if(text1[1] != "STATE" and text1[2] != "BYE"):
		print("invalid message")
		s.close()

	#solve the math equations
	while text1[1] == "STATE":
		if text1[3] == "+":				
			answer = int(text1[2]) + int(text1[4])
			#print(answer)
		if text1[3] == "-":				
			answer = int(text1[2]) - int(text1[4])
			#math = str(answer)
			#print(answer)
		if text1[3] == "*":
			answer = int(text1[2]) * int(text1[4])
			#math = str(answer)
						#print (answer)
		if text1[3] == "/":
			answer = int(int(text1[2]) / int(text1[4]))
			#math = str(answer)
			#print(answer)
		#else: 
		#	print("invalid message")
			#s.close()
			
			
		msg1 = head + " " + str(answer) + "\n"
	

		s.sendall(msg1.encode('utf-8'))
		response = s.recv(1024)
		r = response.decode()
		#print('Response: ' + r)
		text1 = r.split()
		
		
finally: 
	if (text1[2] == "BYE"):
		print(text1[1])
		s.close()





