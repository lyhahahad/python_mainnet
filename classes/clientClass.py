import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self, seedPhrase):
        random = Crypto.Random.new().read
        self.privateKey = RSA.generate(seedPhrase, random)
        self.publicKey = self._private_key.publickey()
        self.signer = PKCS1_v1_5.new(self._private_key)

# a = Client(seedPhrase="11")
