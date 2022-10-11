from hashlib import new
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import NewType
import classes.txClass as txClass
import method.txMethod as txMethod
import method.blockMethod as blockMethod
import classes.clientClass as client
from inspect import signature
import pickle 
from ecdsa import VerifyingKey
import socket

def receptionServerStart(mempool, portNum, genNewTx_thread):
    ip = "127.0.0.1"
    server_addr_port = (ip, portNum)
    buffersize = 100000000

    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_server_socket.bind(server_addr_port)
    udp_server_socket.setblocking(False)
    # udp_server_socket.settimeout(1.0)
    
    print("UDP server is up and listening")
    
    # Listen Datagram incoming
    while(True):
        try:
            rec_data = udp_server_socket.recvfrom(buffersize)
        except BlockingIOError:
            continue
        print(len(rec_data[0]))
        print(rec_data[0])
        msg  = pickle.loads(rec_data[0])
        print(type(msg))
        if(str(type(msg))=="<class 'classes.txClass.tx'>"):
            if not txMethod.verifyTx(msg):
                raise("새로 들어온 트랜잭션 유효성 검증 실패")
            txMethod.addToMempool(mempool, msg)
            print(msg)
        if(str(type(msg)) == "<class 'classes.blockClass.Block'>"):
            if not blockMethod.verifyBlock(msg):
                raise("새로 들어온 블록 유효성 검증 실패")
            genNewTx_thread._delete()
            genNewTx_thread.start()


# def receptionServerStart(mempool, portNum):
#     class MyServer(BaseHTTPRequestHandler):
#         def do_POST(self):
#             # tx 받았을 때 처리.
#             if self.path == "/tx":
#                 # 역직렬화하고 서명 검증하기.
#                 content_len = int(self.headers.get('Content-Length'))
#                 post_body = self.rfile.read(content_len)
#                 post_body = pickle.loads(post_body)
#                 txDeserialized = post_body['transactions']
#                 if not txMethod.verifyTx(txDeserialized):
#                     raise("새로 들어온 트랜잭션 유효성 검증 실패")
#                 txMethod.addToMempool(mempool, txDeserialized)
#                 self.send_response(200)
#             #block 받았을 때 처리.
#             if self.path == "/block":
#                 content_len = int(self.headers.get('Content-Length'))
#                 post_body = self.rfile.read(content_len)
#                 post_body = pickle.loads(post_body)
#                 blockDeserialized = post_body['block']
#                 if (blockMethod.verifyBlock(blockDeserialized)):
#                     print(blockDeserialized.verifiedTx)
#                     print(blockDeserialized.previousBlockHash)
#                     print(blockDeserialized.nonce)
#                     print(blockDeserialized.BlockHash)
#                     print(blockDeserialized.difficulty)
#                     print(blockDeserialized.coinbase)
#                     print(blockDeserialized.blockproducer)
#                 self.send_response(200)

    
#     webServer = HTTPServer(("127.0.0.1", portNum), MyServer)
#     print("Server started http://%s:%s" % ("127.0.0.1", portNum))

#     try:
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         pass

#     webServer.server_close()
#     print("Server stopped.")


