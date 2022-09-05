from distutils.log import error
import classes.txClass as txClass
import classes.clientClass as clients
import networking.broadcast as broadcast
import collections
import ecdsa
import pickle


#트랜잭션 입력 받기.
def inputTx(mempool,client):
    try : 
        recipient = input("recipient : ")
        value = input("value : ")
        newTx = txClass.tx(client.address.digest(), recipient, value, client.address)
        dataBytes = txToBytes(newTx)
        signTx(newTx, dataBytes, client.privateKey)
        if not verifyTx(newTx.signature, dataBytes, client.publicKey):
            return
        addToMempool(mempool, newTx)
        broadcast.broadcastTx(newTx)
    except(error) :
        print(error)
        print("트랜잭션 입력 중 에러 발생!")

# 트랜잭션 데이터 규격에 맞게 수정.
def txToBytes(tx):
    return pickle.dumps(collections.OrderedDict({
                'sender': tx.sender,
                'recipient': tx.recipient,
                'value': tx.value,
                'time' : tx.time}))

#트랜잭션 데이터 collections 형태로 변환
def txToCollection(dataBytes):
    return pickle.loads(dataBytes)

#개인키로 트랜잭션에 서명하기.
def signTx(tx, dataBytes, privateKey):
    tx.signature = privateKey.sign(b"%s"%dataBytes)

#공개키로 트랜잭션 검증하기.
def verifyTx(newTx):
    #공개키로 트랜잭션 검증.
    try:
        dataBytes = txToBytes(newTx)
        newTx.publickey.verify(newTx.signature, dataBytes)
        print("The signature is valid.")
        return True
    except (error):
        print(error)
        print("The signature is not valid.")
        return False


#트랜잭션을 mempool에 추가한다.
def addToMempool(mempool, tx):
    print("mempool에 추가됨.")
    if inMempool(mempool,tx) :
        return
    mempool.append(tx)
    return

#mempool에 해당 트랜잭션이 있는지 확인한다.
def inMempool(mempool, tx):
    return tx in mempool

#트랜잭션을 받았을 때 처리.
def receptTx(mempool, tx):
    if verifyTx(tx):
        addToMempool(mempool, tx)
    return

#블록을 받았을 때 처리.
def receptBlock():


    return