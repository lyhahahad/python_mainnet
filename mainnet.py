# todo list_1 : genNewTx genNewBlock로 로컬 블록체인 만들기.
# 1. 블록 보상 client에 추가되도록 하기.
# 2. 트랜잭션 검증하기.
import threading
from types import new_class
import method.blockMethod as blockMethod
import method.txMethod as txMethod
import classes.blockClass as block
import classes.txClass as txClass
import classes.clientClass as client

PORT = 8000
mempool = []
ip = []
accountData = { }
blockchain = { }

#새로운 트랜잭션을 생성한다.
#후에 개인 키 추가하기.
def genNewTx():
    while(True):
        if(input()=="gentx"):
            sender = input("sender : ")
            recipient = input("recipient : ")
            value = input("value : ")
            newTx = txClass.tx(sender, recipient, value)
            txMethod.addToMempool(mempool, newTx)
            print(mempool)
    # txMethod.broadcastTx(newTx, ip)

# #새로운 트랜잭션을 전송 받았을 때 처리하기.
# def recNewTx(rectx, signature):
#     txMethod.inMempool(mempool, rectx)
#     txMethod.verifySign(rectx, signature)
#     txMethod.verifyTx(rectx, signature, accountData)
#     txMethod.addToMempool(mempool, rectx, signature)
#     txMethod.broadcastTx(rectx, signature, ip)

#새로운 블록을 생성할 때의 프로세스
def genNewBlock():
    newBlock = blockMethod.mining(mempool, "0000000000000000000000000000000",6)
    while(True):
        newBlock = blockMethod.mining(mempool,newBlock.BlockHash,5)
        print("previousBlockHash : ", newBlock.previousBlockHash)
        print("Blockhash : ", newBlock.BlockHash)
    # blockMethod.broadcastBlock(newBlock)
    # blockMethod.modifyAccount(newBlock)

# #새로운 블록을 받았을 때의 프로세스
# def recNewBlock(recblock):
#     blockMethod.verifyBlock(recblock)
#     blockMethod.saveBlock(recblock)
#     blockMethod.modifyAccount(recblock)
#     blockMethod.broadcastBlock(recblock)

genNewTx_thread = threading.Thread(target = genNewTx)
genNewBlock_thread = threading.Thread(target = genNewBlock)
genNewTx_thread.start()
genNewBlock_thread.start()