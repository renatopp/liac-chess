# =============================================================================
# Federal University of Rio Grande do Sul (UFRGS)
# Connectionist Artificial Intelligence Laboratory (LIAC)
# Renato de Pontes Pereira - rppereira@inf.ufrgs.br
# =============================================================================
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================


'''This is the base client for LIAC CHESS.

Use `LiacBot` as your base class to create a new bot.
'''

import sys
import json
import time
import socket
import random

class LiacBot(object):
    '''LiacBot implements a basic client for LIAC CHESS.

    LiacBot encapsulates the basic features to communicate with the LIAC CHESS 
    server, such as serialization and deserialization of json messages, 
    connection handshaking, etc. Use this class as a base implementation for 
    your bots. 
    '''

    name = ''
    ip = '127.0.0.1'
    port = 50100

    def __init__(self):
        '''Constructor.'''

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if not self.name:
            self.name = random.choice([
                'Liacnator', 'Liac Bot', 'Liaczors', 'Liaco'
            ])

    # INTERNAL METHODS ========================================================
    def _connect(self):
        '''(INTERNAL) Connects to the server.'''

        self._socket.connect((self.ip, self.port))

    def _send_data(self, data):
        '''(INTERNAL) Serialize a ``data`` object and sends it to the server.

        :param data: a Python object.
        '''

        d = json.dumps(data)
        self._socket.sendall(d)

    def _receive_data(self):
        '''(INTERNAL) Receives a message from server and deserialize it.

        :return: a Python object.
        '''

        data = self._socket.recv(2**12)
        return json.loads(data)

    def _send_name(self):
        '''(INTERNAL) Sends the bot's name to the server as part of the 
        handshaking procedure.
        '''

        self._send_data({
            'name':self.name
        })

    def _receive_state(self):
        '''(INTERNAL) Handle a state message.'''

        state = self._receive_data()
        if state['winner'] != 0 or state['draw']:
            self.on_game_over(state)
        else:
            self.on_move(state)
    # =========================================================================

    # INTERFACE ===============================================================
    def send_move(self, from_, to_):
        '''Sends a movement to the server.

        :param from_: a 2-tuple with the piece-to-move position.
        :param to_: a 2-tuple with the target position.
        '''

        self._send_data({
            'from': from_,
            'to': to_
        })

    def on_move(self, state):
        '''Receives the state from server, when the server asks for a movement.

        Consult the documentation see which information comes within the
        `state` object.

        :param state: a state object.
        '''

        pass

    def on_game_over(self, state):
        '''Receives the state from server, when the server acknowledges a 
        winner for the game.

        Consult the documentation see which information comes within the
        `state` object.

        :param state: a state object.
        '''

        pass

    def start(self):
        '''Starts the bot.'''

        self._connect()
        self._send_name()

        while True:
            self._receive_state()
    # =========================================================================

if __name__ == '__main__':
    bot = LiacBot()
    bot.start()