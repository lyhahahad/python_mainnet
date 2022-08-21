import hashlib
import classes.blockClass as blockClass

# 무작위 대입을 통한 채굴하기.
def mining(txs, previousBlockHash, diff):
    #return block
    nonce= 0 
    str = previousBlockHash
    difficulty = "0"*diff
    for i in txs:
        str += ("from : %s, to : %s, value: %s \n" %(i.sender, i.recipient,i.value))  
    while(hashlib.sha256((str+"%s" %nonce).encode()).hexdigest()[:diff]!=difficulty):
        nonce+=1

    newBlock = blockClass.Block()
    newBlock.verifiedTx = txs
    newBlock.previousBlockHash = previousBlockHash
    newBlock.nonce = nonce
    newBlock.BlockHash = hashlib.sha256((str+"%s" %nonce).encode()).hexdigest()
    newBlock.difficulty = diff
    return newBlock

#mempool에서 트랜잭션 가져오기.
def makeTxChunk(mempool):
    # return tx 묶음.
    return

# block 검증하기.
def verifyBlock(block):
    #return bool
    return

#block 데이터 베이스에 저장하기.
def saveBlock(block):
    return

#account 데이터 베이스에 적용하기.
def modifyAccount(tx):
    return

#block 다른 노드(ip)에 전송하기.
def broadcastBlock(block, ip):
    return

#fork 선택하기.
def forkChoice(blockchain, block):
    return