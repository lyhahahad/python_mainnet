from ecdsa import SigningKey

class Client:
   def __init__(self, seed = 1024):
      self.privateKey = SigningKey.generate() # uses NIST192p
      self.publicKey = self.privateKey.verifying_key