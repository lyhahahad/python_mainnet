import requests
import json
import pickle

#트랜잭션을 다른 노드(ip)에 전송한다.
ip = "http://127.0.0.1:8080/tx"
def broadcastTx(dataBytes, sig, publickey):
    publickey = publickey.to_string()
    serializedData=pickle.dumps({'data' : dataBytes, 'signature': sig, 'publicKey' : publickey})
    requests.post(ip, data=serializedData)
    return


#블록 다른 노드(ip)에 전송하기.
def broadcastBlock(block, ip):
    return

# broadcastTx("sss")