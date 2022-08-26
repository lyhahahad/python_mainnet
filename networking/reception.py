from http.server import BaseHTTPRequestHandler, HTTPServer
import pickle 
import json

# from classes.txClass import tx
# import method.txMethod as txMethod

#트랜잭션을 받았을 때 처리.
def receptTx(mempool, tx):
    # if not txMethod.verifyTx(tx):
    #     txMethod.addToMempool(mempool, tx)
    return

#블록을 받았을 때 처리.
def receptBlock():


    return


hostName = "localhost"
# serverPort = int(input("serverport"))
serverPort = 8080
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
    def do_POST(self):
        self.send_response(200,"hihi")

        # tx를 전송 받았을 때 처리.
        if self.path == "/tx":
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            post_body = json.loads(post_body)
            print(post_body)


        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")