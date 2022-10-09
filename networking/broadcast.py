import pickle
import socket
import requests
import classes.txClass as tx
ips = ["127.0.0.1"]
port = 8080

udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#트랜잭션 or 블록 브로드 캐스트
def broadcast(data):
    print(str(type(data)))
    serializedData=pickle.dumps(data)
    

    for i in ips:
        print(i)
        udp_client_socket.sendto(serializedData, (i, port))

#브로드 캐스트할 ip 추가하기.
def addBroadcastIp(ip):
    global ips
    ips.append(ip)


# def broadcastTx(transactions):
#     serializedData=pickle.dumps({'transactions' : transactions})
#     for i in ips:
#         requests.post(i+'/tx', data=serializedData, timeout=(1, 50))
#     return


# #블록 다른 노드(ip)에 전송
# def broadcastBlock(block):
#     serializedData=pickle.dumps({'block' : block})
#     for i in ips:
#         res = requests.post(i+'/block', data=serializedData,timeout=(1, 50))
#     return



# import socket
 
# server_ip = "127.0.0.1"
# server_port = 3000
# server_addr_port = (server_ip, server_port)
 
# msg_from_client = "Hello Server from client"
# bytes_to_send = str.encode(msg_from_client)
 
# udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# udp_client_socket.sendto(bytes_to_send, server_addr_port)