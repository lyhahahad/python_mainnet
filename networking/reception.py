from hashlib import new
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from typing import NewType
import classes.txClass as txClass
import method.txMethod as txMethod
import method.blockMethod as blockMethod
import classes.clientClass as client
from inspect import signature
import pickle 
from ecdsa import VerifyingKey



def receptionServerStart(mempool, portNum):

    class MyServer(BaseHTTPRequestHandler):
        def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer) -> None:
            super().__init__(request, client_address, server)
            self.mempool = []

        def do_GET(self):
            self.send_response(200)
        def do_POST(self):
            self.send_response(200,"hihi")
            # tx를 전송 받았을 때 처리.
            if self.path == "/tx":
                # 역직렬화하고 서명 검증하기.
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                post_body = pickle.loads(post_body)
                dataBytes = post_body['data']
                sig = post_body['signature']
                
                txCollection = txMethod.txToCollection(dataBytes)
                newTx = txClass.tx(txCollection['sender'],txCollection['recipient'],txCollection['value'])
                newTx.timeInit(txCollection['time'])
                newTx.signature = sig
                print(txCollection['sender'])
                print(txCollection['recipient'])
                print(txCollection['value'])
                print(txCollection['time'])
                print(txCollection['publicKey'])

                if not txMethod.verifyTx(sig, dataBytes, txCollection['publicKey']):
                    raise("새로 들어온 트랜잭션 유효성 검증 실패")
                txMethod.addToMempool(mempool, newTx)
                #검증을 거친 tx 브로드 캐스트하기.
                # txMethod.broadcast.broadcastTx(dataBytes, newTx.signature)

                # if self.path == "/block":
                #     # 블록 검증
                #     # 블록 내에 포함된 트랜잭션 mempool에서 제거하기.
                self.send_response(200)

            if self.path == "/block":
                # 역직렬화하고 서명 검증하기.
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                post_body = pickle.loads(post_body)
                blockDeserialized = post_body['block']
                print(blockDeserialized.verifiedTx)
                print(blockDeserialized.previousBlockHash)
                print(blockDeserialized.nonce)
                print(blockDeserialized.BlockHash)
                print(blockDeserialized.difficulty)
                print(blockDeserialized.coinbase)
                print(blockDeserialized.blockproducer)


    hostName = "localhost"
    serverPort = portNum

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

