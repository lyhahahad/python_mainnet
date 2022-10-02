import datetime


#트랜잭션 구성 요소
class tx:
    def __init__(self, sender, recipient, value, publickey):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.publickey = publickey
        self.signature = ""
        self.time = datetime.datetime.now()

    def timeInit(self, time):
        self.time =time
