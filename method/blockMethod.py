
import hashlib
import classes.blockClass as blockClass
import networking.broadcast as broadcast
import pickle
import collections


#블록 생성
def genBlock(mempool, client, diff, prevHash):
    newBlock = mining(mempool, prevHash, -1, diff, client)
    while(True):
        newBlock = mining(mempool,newBlock.BlockHash, newBlock.blockHeight,  diff, client)
        print("blockheight",newBlock.blockHeight)
        print("previousBlockHash : ", newBlock.previousBlockHash)
        print("Blockhash : ", newBlock.BlockHash)
        for i in newBlock.verifiedTx:
            print("from : %s, to : %s, value: %s \n" %(i.sender, i.recipient,i.value))

#블록 채굴
def mining(mempool, previousBlockHash, previousBlockHeight, diff, client):
    nonce= 0 
    str = previousBlockHash
    difficulty = "0"*diff
    verifiedTx = []

    while(mempool):
        i = mempool.pop(0)
        str += ("\n from : %s, to : %s, value: %s \n" %(i.sender, i.recipient, i.value))
        verifiedTx.append(i)
    
    while(hashlib.sha256((str+"%s" %nonce).encode()).hexdigest()[:diff]!=difficulty):
        nonce+=1

    newBlock = blockClass.Block(client)
    newBlock.verifiedTx = verifiedTx
    newBlock.previousBlockHash = previousBlockHash
    newBlock.nonce = nonce
    newBlock.BlockHash = hashlib.sha256((str+"%s" %nonce).encode()).hexdigest()
    newBlock.blockHeight = previousBlockHeight+1
    newBlock.difficulty = diff

    broadcast.broadcast(newBlock)

    return newBlock

#블록 검증하기.
def verifyBlock(block):
    str = block.previousBlockHash
    for i in block.verifiedTx:
        str += ("\n from : %s, to : %s, value: %s \n" %(i.sender, i.recipient, i.value))
        if not (i.publickey.verify(i.signature, txToBytes(i))):
            return False
    if hashlib.sha256((str+"%s" %block.nonce).encode()).hexdigest() != block.BlockHash:
        return False
    return True

#블록 데이터 collections로 변환.
def blockDeserialized(dataBytes):
    return pickle.loads(dataBytes)

# 트랜잭션 데이터 규격에 맞게 수정.
def txToBytes(tx):
    return pickle.dumps(collections.OrderedDict({
                'sender': tx.sender,
                'recipient': tx.recipient,
                'value': tx.value,
                'time' : tx.time}))

# #블록 데이터 베이스에 저장하기.
# def saveBlock(block):
#     return

# #account 데이터 베이스에 적용하기.
# def modifyAccount(tx):
#     return
