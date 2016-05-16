# Voting Server CLI
#Esta aplicacion funciona de esta manera debido a que solo manda un byte y no presenta los problemas de "fragmentación"

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



def refreshScreen():  #Esta funcion toma los valores acualizados de los candidatos y reimprime en pantalla
	os.system("clear")
	global v1
	global v2
	global v3
	global v4
	global v5
	print "     ..:: Running Voting Client ::.."
	print
	print  'Candidato 1 = %d' % (v1,)
	print  'Candidato 2 = %d' % (v2,)
	print  'Candidato 3 = %d' % (v3,)
	print  'Candidato 4 = %d' % (v4,)
	print  'Candidato 5 = %d' % (v5,)
	print
	print '------- Actions: '
	print '[1a] > Vote for candidate 1'
	print '[1b] > Request Votes of candidate 1'

	print '[2a] > Vote for candidate 2'
	print '[2b] > Request Votes of candidate 2'

	
	print '[3a] > Vote for candidate 3'
	print '[3b] > Request Votes of candidate 3'
	
	print '[4a] > Vote for candidate 4'
	print '[4b] > Request Votes of candidate 4'
	
	print '[5a] > Vote for candidate 5'
	print '[5b] > Request Votes of candidate 5'
	


def actions(key,s): #Detecta el texto ingresado y decide
	#print key
	n = key
	if n == '1a':
		sendVote(1)
	elif n == '1b':
		sendVotesRequest(1)
	elif n == '2a':
		sendVote(2)
	elif  n== '2b':
		sendVotesRequest(2)
	elif n == '3a':
		sendVote(3)
	elif n == '3b':
		sendVotesRequest(3)
	elif n == '4a':
		sendVote(4)
	elif  n== '4b':
		sendVotesRequest(4)
	elif n == '5a':
		sendVote(5)
	elif n == '5b':
		sendVotesRequest(5)
	#print
	#time.sleep(3)
		
def sendVote(candidate):  #Crea una conexion y envia 1-5 para votar
	TCP_IP = '127.0.0.1'
	TCP_PORT = 8081
	BUFFER_SIZE = 1024
	MESSAGE = str(candidate)  # ------------------------------- PROTOCOL STRING

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	MESSAGE = ""
	data = s.recv(BUFFER_SIZE)
	s.close()
	#print "***"
	#print candidate

def sendVotesRequest(candidate): #Crea una conexion y envia 10-15 para solicitar los votos 
	TCP_IP = '127.0.0.1'
	TCP_PORT = 8081
	BUFFER_SIZE = 1024
	MESSAGE = str(candidate + 10)  # ------------------------------- PROTOCOL STRING
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	data2 = s.recv(BUFFER_SIZE)

	if data2 :
		totalVotes(candidate, data2)
		#print data2
		time.sleep(1)
	s.close()

	#print "+++"


def totalVotes(candidate, votes): #Recibe la cantidad de votos de un candidato y actualiza los valores
	n = int(candidate)
	myVotes = int(votes)
	global v1
	global v2
	global v3
	global v4
	global v5

	if n == 1:
		v1 = myVotes
	elif n == 2:
		v2 = myVotes
	elif n == 3:
		v3 = myVotes
	elif  n== 4:
		v4 = myVotes
	elif n == 5:
		v5 = myVotes
	elif n > 6:
		print "DAFUQ?"
		#time.sleep(3)
	#refreshScreen()
	#print


s = 0
while 1:   #Ciclo de espera de comandos
	refreshScreen()
	print
	key = raw_input(">> ")
	actions(key,s)


