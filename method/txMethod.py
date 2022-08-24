import classes.txClass as txClass
import collections
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

#트랜잭션 입력 받기.
def inputTx(mempool,client):
    while(True):
        if(input()=="gentx"):
            try : 
                sender = input("sender : ")
                recipient = input("recipient : ")
                value = input("value : ")
                newTx = txClass.tx(client._public_key, recipient, value)
                signTx(newTx, client._private_key)
                addToMempool(mempool, newTx)
            except :
                print("트랜잭션 입력 중 에러 발생!")

#트랜잭션 데이터 규격에 맞게 수정.
def toMsgHash(tx):
    msg = collections.OrderedDict({
                'sender': tx.sender,
                'recipient': tx.recipient,
                'value': tx.value})
    msgHash = SHA256.new((str(msg)).encode('utf8'))
    return msgHash

#개인키로 트랜잭션에 서명하기.
def signTx(tx, privateKey):
    tx.signature = pkcs1_15.new(privateKey).sign(toMsgHash(tx))
    return tx.signature

#공개키로 트랜잭션 검증하기.
def verifyTx(tx):
    #공개키로 트랜잭션 검증.
    try:
        pkcs1_15.new(tx.sender).verify(toMsgHash(tx), tx.signature)
        print("The signature is valid.")
    except (ValueError, TypeError):
        print("The signature is not valid.")

    #account 데이터로 트랜잭션 검증.
    return

#트랜잭션을 mempool에 추가한다.
def addToMempool(mempool, tx):
    verifyTx(tx)
    mempool.append(tx)
    return

#트랜잭션을 다른 노드(ip)에 전송한다.
def broadcastTx(tx, ip):
    return

# #mempool에 해당 트랜잭션이 있는지 확인한다.
# def inMempool(mempool, tx):
#     #return bool
#     return