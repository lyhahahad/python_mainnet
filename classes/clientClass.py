from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import binascii

class Client:
   def __init__(self, seed):
      self.privateKey = RSA.generate(seed)
      self.publicKey = self.privateKey.publickey()
      self.signer = PKCS1_v1_5.new(self.privateKey)

   @property
   def identity(self):
      return binascii.hexlify(self.publicKey.exportKey(format='DER')).decode('ascii')