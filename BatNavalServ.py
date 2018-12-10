import socket

UDP_IP = "10.160.108.2"
UDP_PORT = 5005
MESSAGESERV = "YOOO"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) #buffer size is 1024 bytes
	print("received message : ", data.decode())
	MESSAGESERV = input("Votre reponse : ")
	sock.sendto(MESSAGESERV.encode(), addr)
