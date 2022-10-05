import requests
import pickle

ips = ["http://127.0.0.1:8080"]
ips = []


def broadcastTx(transactions):
    serializedData=pickle.dumps({'transactions' : transactions})
    for i in ips:
        print(111111111111)
        requests.post(i+'/tx', data=serializedData, timeout=(1, 50))
        print(2222222222222)
        print(res)
    return


#블록 다른 노드(ip)에 전송
def broadcastBlock(block):
    serializedData=pickle.dumps({'block' : block})
    for i in ips:
        print(33333333333)

        res = requests.post(i+'/block', data=serializedData,timeout=(1, 50))
        print(44444444444444)
        print(res)
    return

#브로드 캐스트할 ip 추가하기.
def addBroadcastIp(ip):
    global ips
    ips.append(ip)


# import socket
 
# server_ip = "127.0.0.1"
# server_port = 3000
# server_addr_port = (server_ip, server_port)
 
# msg_from_client = "Hello Server from client"
# bytes_to_send = str.encode(msg_from_client)
 
# udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# udp_client_socket.sendto(bytes_to_send, server_addr_port)