import requests
import json
import pickle
import time
# https://hsyang.net/posts/python-requests-library-timeout/
# http tcp ip +에러 코드 중심으로 해결
ips = ["http://127.0.0.1:8080"]
# ips = []
# response가 올 때까지 기다려야 한다. 기다리지 않고 다른 것을 실행하면 에러가 발생함. js의 await같은 기능이 있어야 한다.
# 트랜잭션 다른 노드(ip)에 전송
def broadcastTx(transactions):
    serializedData=pickle.dumps({'transactions' : transactions})
    for i in ips:
        print(111111111111)
        res = requests.post(i+'/tx', data=serializedData, timeout=(1, 50))
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