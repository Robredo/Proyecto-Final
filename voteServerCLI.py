# Voting Server CLI

import socket
import time
import os

global v1
global v2
global v3
global v4
global v5

v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
host = '127.0.0.1' 
port = 8081 
backlog = 5 
size = 1024 


def refreshScreen():
	os.system("clear")
	global v1
	global v2
	global v3
	global v4
	global v5
	print "     ..:: Running Voting Server ::.."
	print
	print  'Candidato 1 = %d' % (v1,)
	print  'Candidato 2 = %d' % (v2,)
	print  'Candidato 3 = %d' % (v3,)
	print  'Candidato 4 = %d' % (v4,)
	print  'Candidato 5 = %d' % (v5,)

def addVote(candidate):
	n = candidate
	global v1
	global v2
	global v3
	global v4
	global v5

	if n == 1:
		v1 = v1 + 1
	elif n == 2:
		v2 = v2 + 1
	elif n == 3:
		v3 = v3 + 1
	elif  n== 4:
		v4 = v4 + 1
	elif n == 5:
		v5 = v5 + 1
	elif n > 6:
		print "DAFUQ?"
		#time.sleep(3)
	print "(!) Vote Added"
	time.sleep(1)
	refreshScreen()
	print

def sendVotes(myData, client):
	n = myData
	global v1
	global v2
	global v3
	global v4
	global v5

	if n == 11:
		MESSAGE = str(v1)
		client.send(MESSAGE)
	elif n == 12:
		MESSAGE = str(v2)
		client.send(MESSAGE)
	elif n == 13:
		MESSAGE = str(v3)
		client.send(MESSAGE)
	elif  n== 14:
		MESSAGE = str(v4)
		client.send(MESSAGE)
	elif n == 15:
		MESSAGE = str(v5)
		client.send(MESSAGE)
	elif n > 16:
		print "DAFUQ?"

	print "(!) Votes Requested"

	#print "Ya se envio"
	#print MESSAGE
	time.sleep(1)
	refreshScreen();


def analyzeData(data, client):
	myData = int(data)
	if myData >= 10:
		sendVotes(myData, client)
	else :
		addVote(int(data))
	#print "myData"


#Main Loop
refreshScreen()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while 1: 
	client, address = s.accept() 
	data = client.recv(size) 
	if data: 
		#client.send(data)
		analyzeData(data, client)
		client.close()
