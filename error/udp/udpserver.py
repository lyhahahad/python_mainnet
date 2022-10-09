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
buffersize = 1024

# 소켓을 UDP로 열고 서버의 IP/PORT를 연결한다. 그리고 Non-blocking로 바꾼다.
udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket.bind(server_addr_port)
udp_server_socket.setblocking(False)
# udp_server_socket.settimeout(1.0)
 
print("UDP server is up and listening")
 
# Listen Datagram incoming
while(True):
  try:
    byte_addr_pair = udp_server_socket.recvfrom(buffersize)
  except BlockingIOError:
    continue
  msg  = byte_addr_pair[0]
  addr = byte_addr_pair[1]
  client_msg = "msg from client : {}".format(len(msg))
  client_ip  = "client IP Addr : {}".format(addr)
 
  print(client_msg)
  print(client_ip)
  msg = pickle.loads(msg)
  print(msg.sender)
  print(msg.recipient)
  print(msg.value)
  print(msg.publickey)


