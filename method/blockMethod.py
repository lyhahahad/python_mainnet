import hashlib
import classes.blockClass as blockClass

#블록 생성하기.
def genBlock(mempool, client, diff):
    newBlock = mining(mempool, "0"*64, -1, diff, client)
    while(True):
        newBlock = mining(mempool,newBlock.BlockHash, newBlock.blockHeight,  diff, client)
        print("previousBlockHash : ", len(newBlock.previousBlockHash))
        print("Blockhash : ", newBlock.BlockHash)
        print(newBlock.blockHeight)

#블록 채굴하기.
def mining(mempool, previousBlockHash, previousBlockHeight, diff, client):
    nonce= 0 
    str = previousBlockHash
    difficulty = "0"*diff
    verifiedTx = []
    while(mempool):
        i = mempool.pop(0)
        str += ("from : %s, to : %s, value: %s \n" %(i.sender, i.recipient, i.value))
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
    for i in newBlock.verifiedTx:
        print("from : %s, to : %s, value: %s \n" %(i.sender, i.recipient,i.value))

    return newBlock


#블록 검증하기.
def verifyBlock(block):
    #return bool
    return

#블록 데이터 베이스에 저장하기.
def saveBlock(block):
    return

#account 데이터 베이스에 적용하기.
def modifyAccount(tx):
    return

# #fork 선택하기.
# def forkChoice(blockchain, block):
#     return