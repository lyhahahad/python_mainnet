import threading
from types import new_class
import method.blockMethod as blockMethod
import method.txMethod as txMethod
import classes.blockClass as block
import classes.txClass as txClass
import classes.clientClass as client
import networking.reception as reception

mempool = []
ip = []
accounts = []
client = client.Client()
print(type(client.publicKey.to_string()))
print(client.publicKey.to_string())

#새로운 트랜잭션을 생성한다.
def genNewTx():
    txMethod.inputTx(mempool, client)

# #새로운 트랜잭션을 전송 받았을 때 처리하기.
def recNewTx(portNum):
    reception.receptionServerStart(mempool,portNum)

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
genNewBlock_thread = threading.Thread(target = genNewBlock)
genNewBlock_thread.start()

while(True):
    comm = input("gentx or recepstart \n")
    if comm == 'gentx':
        genNewTx_thread = threading.Thread(target = genNewTx)
        genNewTx_thread.start()
        genNewTx_thread.join()
    elif comm == 'recepstart':
        portNum = iter(input("portNum : "))
        # print(type(portNum))
        reception_thread = threading.Thread(target = recNewTx, args=portNum)
        reception_thread.start()
    elif comm == 'recep quit':
        reception_thread.join()
        continue
    else : 
        print('존재하지 않는 명령어입니다.')
        continue