import socket

UDP_IP ="10.160.108.2"
UDP_PORT = 5005
MESSAGE = "Hello world!!"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("Réponse serveur :", data.decode())
    MESSAGE=input("Votre Reponse :")
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))