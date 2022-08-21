import datetime
from inspect import signature

#개인키 추가하기.
class tx:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()
        # self.signature = privatekey