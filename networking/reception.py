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
        def do_POST(self):
            # tx 받았을 때 처리.
            if self.path == "/tx":
                # 역직렬화하고 서명 검증하기.
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                post_body = pickle.loads(post_body)
                txDeserialized = post_body['transactions']
                if not txMethod.verifyTx(txDeserialized):
                    raise("새로 들어온 트랜잭션 유효성 검증 실패")
                txMethod.addToMempool(mempool, txDeserialized)
                self.send_response(200)
            #block 받았을 때 처리.
            if self.path == "/block":
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                post_body = pickle.loads(post_body)
                blockDeserialized = post_body['block']
                if (blockMethod.verifyBlock(blockDeserialized)):
                    print(blockDeserialized.verifiedTx)
                    print(blockDeserialized.previousBlockHash)
                    print(blockDeserialized.nonce)
                    print(blockDeserialized.BlockHash)
                    print(blockDeserialized.difficulty)
                    print(blockDeserialized.coinbase)
                    print(blockDeserialized.blockproducer)
                self.send_response(200)

    
    webServer = HTTPServer(("127.0.0.1", portNum), MyServer)
    print("Server started http://%s:%s" % ("127.0.0.1", portNum))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


    # class MyServer(BaseHTTPRequestHandler):
    #     def __init__(self, request: bytes, client_address: tuple(str), server: socketserver.BaseServer) -> None:
    #         super().__init__(request, client_address, server)
    #         self.mempool = []

    #     def do_GET(self):
    #         self.send_response(200)
    #     def do_POST(self):

    #         # tx 받았을 때 처리.
    #         if self.path == "/tx":
    #             # 역직렬화하고 서명 검증하기.
    #             content_len = int(self.headers.get('Content-Length'))
    #             post_body = self.rfile.read(content_len)
    #             post_body = pickle.loads(post_body)
    #             txDeserialized = post_body['transactions']
 

    #             if not txMethod.verifyTx(txDeserialized):
    #                 raise("새로 들어온 트랜잭션 유효성 검증 실패")
    #             txMethod.addToMempool(mempool, txDeserialized)
    #             self.send_response(200)
    #         #block 받았을 때 처리.
    #         if self.path == "/block":
    #             content_len = int(self.headers.get('Content-Length'))
    #             post_body = self.rfile.read(content_len)
    #             post_body = pickle.loads(post_body)
    #             blockDeserialized = post_body['block']
    #             print(blockDeserialized.verifiedTx)
    #             print(blockDeserialized.previousBlockHash)
    #             print(blockDeserialized.nonce)
    #             print(blockDeserialized.BlockHash)
    #             print(blockDeserialized.difficulty)
    #             print(blockDeserialized.coinbase)
    #             print(blockDeserialized.blockproducer)


    # hostName = "localhost"
    # serverPort = portNum

    # webServer = HTTPServer((hostName, serverPort), MyServer)
    # print("Server started http://%s:%s" % (hostName, serverPort))

    # try:
    #     webServer.serve_forever()
    # except KeyboardInterrupt:
    #     pass

    # webServer.server_close()
    # print("Server stopped.")

