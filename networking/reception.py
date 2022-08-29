from http.server import BaseHTTPRequestHandler, HTTPServer
from inspect import signature
import pickle 
from ecdsa import VerifyingKey

def receptionServerStart(mempool, portNum):
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


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
    def do_POST(self):
        self.send_response(200,"hihi")

        # tx를 전송 받았을 때 처리.
        if self.path == "/tx":
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            post_body = pickle.loads(post_body)
            dataBytes = post_body['data']
            sig = post_body['signature']
            publicKey = post_body['publicKey']
            print(publicKey)
            publicKey = VerifyingKey.from_string(publicKey)
            # try : 
            #     receptTx(mempool, tx)
            print(publicKey.verify(sig, dataBytes))
            # receptTx
