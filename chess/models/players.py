import chess
import threading
import json
import socket

__all__ = ['Player', 'NetworkPlayer', 'HumanPlayer']

class Player(object):
    def __init__(self):
        self.app = None
        self.name = ''
        self.status = chess.STATE_DISCONNECTED
        self.team = chess.NONE
        self.infractions = 0

    def start(self):
        pass

    def stop(self):
        pass

    def update(self, tick):
        pass

    def set_state(self, state):
        pass

    def get_move(self):
        pass

class HumanPlayer(object):
    def __init__(self, app, team):
        chess.log.debug('HUMAN_PLAYER', 'Creating a new HumanPlayer.')
        self.app = app
        self.name = 'Human Player'
        self.team =team
        self.infractions = 0
        self.status = chess.STATUS_CONNECTED

        self._move = None

    def move(self, from_, to_):
        self._move = (from_, to_)

    def start(self):
        pass

    def stop(self):
        pass

    def update(self, tick):
        pass

    def set_state(self, state):
        pass

    def get_move(self):
        r = self._move
        self._move = None
        return r

class NetworkPlayer(object):
    def __init__(self, app, team, ip, port):
        chess.log.debug('NETWORK_PLAYER', 'Creating a new NetworkPlayer.')
        self.app = app
        self.name = ''
        self.team = team
        self.infractions = 0
        self.status = chess.STATUS_DISCONNECTED

        self._ip = ip
        self._port = port
        self._comm = chess.network.Communicator(ip, port)
        self._thread = threading.Thread(target=self._comm.run)

        self._set_default_name()

    def _set_default_name(self):
        self.name = ':'.join([str(self._ip), str(self._port)])

    def start(self):
        chess.log.debug('NETWORK_PLAYER', 'Starting a NetworkPlayer thread.')
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        self._comm.stop()
        self._thread.join()
        pass

    def update(self, tick):
        if self.status == chess.STATUS_DISCONNECTED and self._comm.name is not None:
            self.name = self._comm.name
            self.status = chess.STATUS_CONNECTED
            self.app.connect_user(self)

        elif self.status == chess.STATUS_CONNECTED and self._comm.name is None:
            self._set_default_name()
            self.status = chess.STATUS_DISCONNECTED
            self.app.disconnect_user(self)

    def set_state(self, state):
        self._comm.send(json.dumps(state))

    def get_move(self):
        r = self._comm.receive()
        if r:
            move = json.loads(r)
            return move['from'], move['to']

        return None