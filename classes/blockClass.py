class Block:
    def __init__(self, client):
        self.blockHeight = 0
        self.verifiedTx = []
        self.previousBlockHash = ""
        self.nonce = ""
        self.BlockHash = ""
        self.difficulty = 0
        self.coinbase = 100
        self.blockproducer = client.identity
    
    # def blockVerify