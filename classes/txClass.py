import datetime


#트랜잭션 구성 요소
#sender : 보내는 사람의 퍼블릭키 or 주소
#recipient : 받는 사람의 퍼블릭키 or 주소
#
class tx:
    def __init__(self, sender, recipient, value, publickey):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()
        self.signature = ""
        self.publickey = ''
        
    def timeInit(self, time):
        self.time =time
