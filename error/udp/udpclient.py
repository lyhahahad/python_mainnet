import socket
import pickle
import datetime

class tx:
    def __init__(self, sender, recipient, value, publickey):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.publickey = publickey
        self.signature = ""
        self.time = datetime.datetime.now()

    def timeInit(self, time):
        self.time =time


# 클라이언트가 보내고자 하는 서버의 IP와 PORT
server_ip = "127.0.0.1"
server_port = 3000

server_addr_port = (server_ip, server_port)
 
# 보낼 메시지를 byte 배열로 바꾼다.
bytes_to_send = pickle.dumps(tx(1,10,100,1000))
 
# 소켓을 UDP로 열고 서버의 IP/PORT로 메시지를 보낸다.
udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_client_socket.sendto(bytes_to_send, server_addr_port)