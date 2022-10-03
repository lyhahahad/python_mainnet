from cgi import test
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


#트랜잭션 생성.
def genNewTx():
    txMethod.inputTx(mempool, client)

#트랜잭션 recept 서버 시작.
def recNewTx(portNum):
    reception.receptionServerStart(mempool,portNum)

#블록 생성.
def genNewBlock():
    blockMethod.genBlock(mempool, client, 8)

genNewBlock_thread = threading.Thread(target = genNewBlock)
genNewBlock_thread.start()


while(True):
    comm = input("gentx, recepstart, recep quit, genblock quit, addip \n")
    #트랜잭션 생성.
    if comm == 'gentx':
        genNewTx_thread = threading.Thread(target = genNewTx)
        genNewTx_thread.start()
        genNewTx_thread.join()
    #트랜잭션 recept 서버 시작
    elif comm == 'recepstart':
        portNum = int(input("portNum : "))
        reception_thread = threading.Thread(target = recNewTx, args=(portNum,))
        reception_thread.start()
    #트랜잭션 recept 서버 종료
    elif comm == 'recep quit':
        reception_thread._delete()
        print("reception서버 종료")
    #블록 생성 종료.
    elif comm == 'genblock quit':
        genNewBlock_thread._delete()
        print("블록생성 종료")
        break
    #브로드 캐스트 ip 추가하기.
    elif comm == 'addip':
        ip = input("ip address : ")
        broadcast.addBroadcastIp(ip)
    #없는 명령어
    else : 
        print('존재하지 않는 명령어입니다.')