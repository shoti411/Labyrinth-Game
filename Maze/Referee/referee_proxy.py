import socket
import json

class RefereeProxy:

    FRAME_SIZE = 1024
    VALID_FUNCTION_NAMES = ['setup', 'take-turn', 'win']

    def __init__(self, player, conn):
        self.player = player
        self.socket = conn

    def receive_message(self):
        byte_string = b''
        while True:
            byte_string += self.socket.recv(self.FRAME_SIZE)
            if byte_string == b'':
                break
        try:
            message = self.parse_message(byte_string)
        except json.decoder.JSONDecodeError:
            self.receive_message()

        if self.__is_valid(message):
            func_name = message[0]
            args = message[1]
            
        self.receive_message()

    def __is_valid(self, msg):
        if len(msg) != 2:
            return False
        if not msg[0] in self.VALID_FUNCTION_NAMES:
            return False
        if msg[0] == 'setup' and len(msg[1]) != 2:
            return False
        if msg[0] == 'take-turn' and len(msg[1]) != 1:
            return False
        if msg[0] == 'win' and len(msg[1]) != 1:
            return False
        return True

    def parse_message(self, json_string):
        json_str = json_string.decode('utf-8')
        decoder = json.JSONDecoder()
        pos = 0
        objs = []
        while pos < len(json_str):
            json_str = json_str[pos:].strip()
            if not json_str:
                break
            obj, pos = decoder.raw_decode(json_str)
            objs.append(obj)
        return objs[0]

RefereeProxy('', '').parse_message(b'{ "eresr": "erere"')