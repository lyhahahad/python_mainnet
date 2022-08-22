#sign을 검증한다.
def verifySign(tx):
    #return bool
    return

#mempool에 해당 트랜잭션이 있는지 확인한다.
def inMempool(mempool, tx):
    #return bool
    return

#트랜잭션을 mempool에 추가한다.
def addToMempool(mempool, tx):
    # verifyTx(tx)
    mempool.append(tx)
    return

#트랜잭션을 검증한다.
def verifyTx(tx, accountData):
    # return bool
    return

#트랜잭션을 다른 노드(ip)에 전송한다.
def broadcastTx(tx, ip):
    return