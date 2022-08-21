# todo list_1 : genNewTx genNewBlock로 로컬 블록체인 만들기.
from threading import Thread
import socket
import method.blockMethod as blockMethod
import method.txMethod as txMethod
import classes.blockClass as block
import classes.txClass as txClass
import classes.clientClass as client

PORT = 8000
mempool = { }
ip = []
accountData = { }
blockchain = { }

#새로운 트랜잭션을 생성한다.
#후에 개인 키 추가하기.
def genNewTx(sender, recipient, value):
    newTx = ()
    txMethod.addToMempool(mempool, newTx)
    txMethod.broadcastTx(newTx, ip)
    return newTx

#새로운 트랜잭션을 전송 받았을 때 처리하기.
def recNewTx(rectx, signature):
    txMethod.inMempool(mempool, rectx)
    txMethod.verifySign(rectx, signature)
    txMethod.verifyTx(rectx, signature, accountData)
    txMethod.addToMempool(mempool, rectx, signature)
    txMethod.broadcastTx(rectx, signature, ip)

#새로운 블록을 생성할 때의 프로세스
def genNewBlock():
    txs = blockMethod.makeTxChunk(mempool)
    newBlock = blockMethod.mining(txs)
    blockMethod.broadcastBlock(newBlock)
    blockMethod.modifyAccount(newBlock)

#새로운 블록을 받았을 때의 프로세스
def recNewBlock(recblock):
    blockMethod.verifyBlock(recblock)
    blockMethod.saveBlock(recblock)
    blockMethod.modifyAccount(recblock)
    blockMethod.broadcastBlock(recblock)

tx_1 = txClass.tx('a','b',10)
tx_2 = txClass.tx('b','c',10)
txs = [tx_1, tx_2]
newBlock = blockMethod.mining(txs, "0000000000000000000000000000000",5)
for i in range(99):
    tx_1.value += i
    tx_2.value += i
    newBlock = blockMethod.mining(txs,newBlock.BlockHash,5)
    print("previousBlockHash : ", newBlock.previousBlockHash)
    print("BlockHash : ", newBlock.BlockHash,"\n")
