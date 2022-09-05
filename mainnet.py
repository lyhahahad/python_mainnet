import threading
from types import new_class
import method.blockMethod as blockMethod
import method.txMethod as txMethod
import classes.blockClass as block
import classes.txClass as txClass
import classes.clientClass as client
import networking.reception as reception
import networking.broadcast as broadcast
import sys


mempool = []
ip = []
accounts = []
client = client.Client()
print(type(client.publicKey.to_string()))
print(client.publicKey.to_string())
print(sys.getsizeof(client.publicKey.to_string()))
print(client.address)
print(sys.getsizeof(client.address))



#새로운 트랜잭션을 생성한다.
def genNewTx():
    txMethod.inputTx(mempool, client)

# #새로운 트랜잭션을 전송 받았을 때 처리하기.
def recNewTx(portNum):
    reception.receptionServerStart(mempool,portNum)

#새로운 블록을 생성할 때의 프로세스
def genNewBlock():
    blockMethod.genBlock(mempool, client, 6)
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
    print(11)
    comm = input("gentx, recepstart, recep quit, genblock quit, addip \n")
    #트랜잭션 생성할 때
    if comm == 'gentx':
        genNewTx_thread = threading.Thread(target = genNewTx)
        genNewTx_thread.start()
        genNewTx_thread.join()
    #트랜잭션 받고 싶을 때
    elif comm == 'recepstart':
        portNum = int(input("portNum : "))
        reception_thread = threading.Thread(target = recNewTx, args=(portNum,))
        reception_thread.start()
    #트랜잭션 받고 싶지 않을 때
    elif comm == 'recep quit':
        reception_thread._delete()
        print("reception서버 종료")
    elif comm == 'genblock quit':
        genNewBlock_thread._delete()
        print("블록생성 종료")
        break
    elif comm == 'addip':
        ip = input("ip address : ")
        broadcast.addBroadcastIp(ip)
    #없는 명령어일 때
    else : 
        print('존재하지 않는 명령어입니다.')