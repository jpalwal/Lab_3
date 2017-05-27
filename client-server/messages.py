import abc
import json

class Message(object):
    def __init__(self, ID, msg):
        self.ID = ID
        self.message = msg

    @staticmethod
    def decoding(msg):
        rec = json.loads(msg)
        return Message(rec['ID'], rec['message'])


class MsgDict(object):
    def __init__(self):
        self.key = ''
        self.dict = {}
        self.dict['unknown_msg'] = UnknownMsg()
        self.dict['game_init'] = GameInit()
        self.dict['board_size'] = BoardSize()
        self.dict['move'] = Move()
        self.dict['game_ended'] = GameEnded()
        self.dict['playing'] = Play()
        self.dict['error'] = Error()


class MessageHandler(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, msg, obj):
        '''Message handler'''

class Error(MessageHandler):
    def handle(self, msg, obj):
        return Exit().handle(msg, obj)

class Exit(MessageHandler):
    def handle(self, msg, obj):
        text = msg.message
        return text

class UnknownMsg(MessageHandler):
    def handle(self, msg, obj):
        print('Unknown message')
        return Message(msg.ID,'')

class GameInit(MessageHandler):
    def handle(self, msg, obj):
        print(msg.message)
        text = input()
        return Message(2, text)

class BoardSize(MessageHandler):
    def handle(self, msg, obj):
        obj.key = 'board_size'
        print('Choose your board size')
        size = input()
        return Message(4, size)

class Move(MessageHandler):
    def handle(self, msg, obj):
        obj.key = 'move'
        print(msg.message)
        x = input("Enter x value\n")
        y = input("Enter y value\n")
        return Message(6, (x,y))

class GameEnded(MessageHandler):
    def handle(self, msg, obj):
        print(msg.message)
        return Exit().handle(msg, obj)

class Play(MessageHandler):
    def handle(self, msg, obj):
        obj.key = 'playing'
        print(msg.message)
        text = input()
        return Message(obj.key, text)
