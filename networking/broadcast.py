import requests
import json
import pickle

#트랜잭션을 다른 노드(ip)에 전송한다.
ip = ["http://127.0.0.1:8081/tx"]
def broadcastTx(dataBytes, sig):
    #직렬화해서 보내기.
    serializedData=pickle.dumps({'data' : dataBytes, 'signature': sig})
    for i in ip:
        res = requests.post(i, data=serializedData)
        print(res)
    return


#블록 다른 노드(ip)에 전송하기.
def broadcastBlock(block, ip):
    return

# broadcastTx("sss")