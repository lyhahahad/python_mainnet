from distutils.log import error
import classes.txClass as txClass
import classes.clientClass as clients
import networking.broadcast as broadcast
import collections
import ecdsa
import pickle


#트랜잭션 입력 받기.
def inputTx(mempool,client):
    while(True):
        if(input()=="gentx"):
            try : 
                recipient = input("recipient : ")
                value = input("value : ")
                newTx = txClass.tx(client.publicKey, recipient, value)
                dataBytes = txToBytes(newTx)
                signTx(newTx, dataBytes, client.privateKey)
                addToMempool(newTx.signature, dataBytes, client.publicKey, mempool, newTx)
                broadcast.broadcastTx(dataBytes, newTx.signature, newTx.sender)
            except(error) :
                print(error)

                print("트랜잭션 입력 중 에러 발생!")

#트랜잭션 데이터 규격에 맞게 수정.
def txToBytes(tx):
    return pickle.dumps(collections.OrderedDict({
                'sender': tx.sender,
                'recipient': tx.recipient,
                'value': tx.value,
                'time' : tx.time}))

# def txToObject(tx):


#개인키로 트랜잭션에 서명하기.
def signTx(tx, dataBytes, privateKey):
    tx.signature = privateKey.sign(b"%s"%dataBytes)

#공개키로 트랜잭션 검증하기.
def verifyTx(sig, data, publicKey):
    #공개키로 트랜잭션 검증.
    try:
        publicKey.verify(sig, data)
        print("The signature is valid.")
        return True
    except (ValueError, TypeError):
        print("The signature is not valid.")
        return False


#트랜잭션을 mempool에 추가한다.
def addToMempool(sig, dataBytes, publicKey, mempool, tx):
    #mempool에 추가 전 트랜잭션 검증.
    verifyTx(sig, dataBytes, publicKey)
    if inMempool(mempool,tx) :
        return
    mempool.append(tx)
    return

#mempool에 해당 트랜잭션이 있는지 확인한다.
def inMempool(mempool, tx):
    return tx in mempool

#트랜잭션을 받았을 때 처리.
def receptTx(mempool, tx):
    # if not txMethod.verifyTx(tx):
    #     txMethod.addToMempool(mempool, tx)
    return

#블록을 받았을 때 처리.
def receptBlock():


    return