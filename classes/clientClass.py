from ecdsa import SigningKey
import hashlib

# 지갑 생성
class Client:
   def __init__(self):
      self.privateKey = SigningKey.generate() # uses NIST192p
      self.publicKey = self.privateKey.get_verifying_key()
      self.address = hashlib.sha256((self.publicKey.to_string()))