#블록 구성 요소
class Block:
    def __init__(self, client):
        self.blockHeight = 0
        self.verifiedTx = []
        self.previousBlockHash = ""
        self.BlockHash = ""
        self.nonce = ""
        self.difficulty = 0
        self.coinbase = 100
        self.blockproducer = client.publicKey