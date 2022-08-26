import requests


#트랜잭션을 다른 노드(ip)에 전송한다.
ip = "http://127.0.0.1:8080/tx"
def broadcastTx(dataBytes, sig, publickey):
    print(dataBytes)
    print(sig)
    print(publickey)
    publickey = publickey.to_string()
    requests.post(ip, {'data' : dataBytes, 'signature': sig, 'publicKey' : publickey})
    return


#블록 다른 노드(ip)에 전송하기.
def broadcastBlock(block, ip):
    return

# broadcastTx("sss")