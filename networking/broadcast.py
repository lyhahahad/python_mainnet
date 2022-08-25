import requests
#트랜잭션을 다른 노드(ip)에 전송한다.
ip = "http://127.0.0.1:8080/tx"
def broadcastTx(tx):
    # C:\Users\USER\AppData\Local\Programs\Python\Python310\Lib\site-packages\requests\adapters.py - 489 conn.urlopen에서 에러 발생.
    requests.post(ip, tx)
    return


#블록 다른 노드(ip)에 전송하기.
def broadcastBlock(block, ip):
    return

broadcastTx("sss")