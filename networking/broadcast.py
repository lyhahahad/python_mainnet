import requests
import json
import pickle

#트랜잭션을 다른 노드(ip)에 전송한다.
# ips = ["http://127.0.0.1:8080", "http://127.0.0.1:8081"]
ips = []

def broadcastTx(dataBytes, sig):
    #직렬화해서 보내기.
    serializedData=pickle.dumps({'data' : dataBytes, 'signature': sig})
    for i in ips:
        res = requests.post(i+'/tx', data=serializedData)
        print(res)
    return


#블록 다른 노드(ip)에 전송하기.
def broadcastBlock(block):
    serializedData=pickle.dumps({'block' : block})
    for i in ips:
        res = requests.post(i+'/block', data=serializedData)
        print(res)
    return

#브로드 캐스트할 ip추가하기.
def addBroadcastIp(ip):
    global ips
    ips.append(ip)