import abc
import json

class Message():  #object in json = dict in python
    def __init__(self, mID: int, msg):
        self.ID = int(mID)
        self.message = msg

    @staticmethod
    def decoding(msg):
        rec = json.loads(msg)
        out = Message(rec['ID'], rec['message'])
        return out

    def encoding(self):
        return str.encode(json.dumps(self.__dict__))


class MsgDict():
    def __init__(self):
        self.key = 1
        self.mdict = {}
        self.mdict[0] = UnknownMsg()
        self.mdict[1] = GameInit()
        self.mdict[5] = Move()
        self.mdict[7] = GameEnded()
        self.mdict[9] = PlayGuess()
        self.mdict[11] = PrintMessage()
        self.mdict[99] = Error()
        self.available = {}
        self.available[0] = [5,11]
        self.available[1] = [1,9,99,11]
        self.available[5] = [5,7,99,11]
        self.available[11] = [5,7,11,99]
        self.available[9] = [9,7,99,11]
    def handle(self, msg):
        if msg.ID not in self.available.setdefault(self.key, self.available[0]):
            msg.ID = -1
        return self.mdict.setdefault(msg.ID, self.mdict[0]).handle(msg, self)

class MessageHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, msg, obj):
        '''Message handler'''

class PrintMessage(MessageHandler):
    def handle(self, msg, obj):
        print(msg.message)

class Error(MessageHandler):
    def handle(self, msg, obj):
        return Exit().handle(msg, obj)

class Exit(MessageHandler):
    def __init__(self):
        self.message = ''
    def handle(self, msg, obj):
        self.message = msg.message
        return self

class UnknownMsg(MessageHandler):
    def handle(self, msg, obj):
        print('Unknown message')
        #if msg.message == 5:
        #    Move(msg,obj)
        #else:
        return Message(msg.ID,'')

class GameInit(MessageHandler):
    def handle(self, msg, obj):
        print(msg.message)
        text = ''
        while not len(text):
            text = input()
        ret = Message(2, text)
        return ret

class Move(MessageHandler):
    def handle(self, msg, obj):
        obj.key = 5
        print(msg.message)
        x, y = '', ''
        while not len(x):
            x = input("Enter x value\n")
        while not len(y):
            y = input("Enter y value\n")
        ret = Message(6, (x,y))
        return ret

class GameEnded(MessageHandler):
    def handle(self, msg, obj):
        return Exit().handle(msg, obj)

class PlayGuess(MessageHandler):
    def handle(self, msg, obj):
        obj.key = 9
        print(msg.message)
        text = ''
        while not len(text):
            text = input()
        ret = Message(9, text)
        return ret
