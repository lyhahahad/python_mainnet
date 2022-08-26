import threading
from types import new_class
import method.blockMethod as blockMethod
import method.txMethod as txMethod
import classes.blockClass as block
import classes.txClass as txClass
import classes.clientClass as client

mempool = []
ip = []
accounts = []
client = client.Client()
# print(type(client.privateKey))
# print(client.privateKey)
# print(type(client.publicKey))
# print(client.publicKey)
print(type(client.publicKey.to_string()))
print(client.publicKey.to_string())
# print(type())
# print()
# print(type())
# print()
# print(type())
# print()
# print(type())
# print()
#새로운 트랜잭션을 생성한다.
def genNewTx():
    txMethod.inputTx(mempool, client)

# #새로운 트랜잭션을 전송 받았을 때 처리하기.
# def recNewTx(rectx, signature):
#     txMethod.inMempool(mempool, rectx)
#     txMethod.verifySign(rectx, signature)
#     txMethod.verifyTx(rectx, signature, accountData)
#     txMethod.addToMempool(mempool, rectx, signature)
#     txMethod.broadcastTx(rectx, signature, ip)

#새로운 블록을 생성할 때의 프로세스
def genNewBlock():
    blockMethod.genBlock(mempool, client, 7)
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