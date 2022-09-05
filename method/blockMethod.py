from __future__ import barry_as_FLUFL
from distutils.log import error
import errno
import hashlib
import classes.blockClass as blockClass
import networking.broadcast as broadcast
import pickle

#블록 생성하기.
def genBlock(mempool, client, diff):
    newBlock = mining(mempool, "0"*64, -1, diff, client)
    while(True):
        newBlock = mining(mempool,newBlock.BlockHash, newBlock.blockHeight,  diff, client)
        print("previousBlockHash : ", newBlock.previousBlockHash)
        print("Blockhash : ", newBlock.BlockHash)
        print(newBlock.blockHeight)

#블록 채굴하기.
def mining(mempool, previousBlockHash, previousBlockHeight, diff, client):
    nonce= 0 
    str = previousBlockHash
    difficulty = "0"*diff
    verifiedTx = []
    print("mempool : ",mempool)
    while(mempool):
        i = mempool.pop(0)
        str += ("\n from : %s, to : %s, value: %s \n" %(i.sender, i.recipient, i.value))
        verifiedTx.append(i)
    
    while(hashlib.sha256((str+"%s" %nonce).encode()).hexdigest()[:diff]!=difficulty):
        nonce+=1
    print(str+"%s" %nonce)
    
    newBlock = blockClass.Block(client)
    newBlock.verifiedTx = verifiedTx
    newBlock.previousBlockHash = previousBlockHash
    newBlock.nonce = nonce
    newBlock.BlockHash = hashlib.sha256((str+"%s" %nonce).encode()).hexdigest()
    newBlock.blockHeight = previousBlockHeight+1
    newBlock.difficulty = diff
    for i in newBlock.verifiedTx:
        print("from : %s, to : %s, value: %s \n" %(i.sender, i.recipient,i.value))

    broadcast.broadcastBlock(newBlock)

    return newBlock

#블록 데이터 collections 형태로 변환
def blockDeserialized(dataBytes):
    return pickle.loads(dataBytes)

#블록 검증하기.
def verifyBlock(block):
    for i in block.verifiedTx:
        if  i.publickey.verify(i.signature, data)
            # return false
        str += ("\n from : %s, to : %s, value: %s \n" %(i.sender, i.recipient, i.value))
    if hashlib.sha256((str+"%s" %block.nonce).encode()).hexdigest() != block.BlockHash:
        return False
    return

#블록 데이터 베이스에 저장하기.
def saveBlock(block):
    return

#account 데이터 베이스에 적용하기.
def modifyAccount(tx):
    return
