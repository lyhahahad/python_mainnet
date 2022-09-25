
import hashlib
import classes.blockClass as blockClass
import networking.broadcast as broadcast
import pickle
import collections


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

# 트랜잭션 데이터 규격에 맞게 수정.
def txToBytes(tx):
    return pickle.dumps(collections.OrderedDict({
                'sender': tx.sender,
                'recipient': tx.recipient,
                'value': tx.value,
                'time' : tx.time}))

#블록 검증하기.
def verifyBlock(block):
    for i in block.verifiedTx:
        # 트랜잭션 서명 검증.
        if not (i.publickey.verify(i.signature, txToBytes(i))):
            return False
        # 블록 해시 값 검증
        if hashlib.sha256((str+"%s" %block.nonce).encode()).hexdigest() != block.BlockHash:
            return False
    return True

#블록 데이터 베이스에 저장하기.
def saveBlock(block):
    return

#account 데이터 베이스에 적용하기.
def modifyAccount(tx):
    return
