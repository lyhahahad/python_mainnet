from ecdsa import SigningKey
import hashlib

#클라이언트 구성 요소

class Client:
   def __init__(self, seed = 1024):
      self.privateKey = SigningKey.generate() # uses NIST192p
      self.publicKey = self.privateKey.verifying_key
      self.address = hashlib.sha256((self.publicKey.to_string()))