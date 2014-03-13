import threading
import socket
import json
import time

import chess

__all__ = ['Server', 'Communicator', 'Communicator2']

class Server(object):
    def __init__(self, app):
        self.app = app

        self._names = [
            None, 
            None
        ]
        # self._communicators = [
        #     Communicator(0, chess.config['slot_0_ip'], chess.config['slot_0_port']), 
        #     Communicator(1, chess.config['slot_1_ip'], chess.config['slot_1_port'])
        # ]
        # self._threads = [
        #     threading.Thread(target=self._communicators[0].run),
        #     threading.Thread(target=self._communicators[1].run)
        # ]

    def clear_buffers(self):
        for c in self._communicators:
            c.clear_buffers()

    def start(self):
        for t in self._threads:
            t.daemon = True
            t.start()

    def verify_connection(self):
        pass
        # for i in xrange(2):
        #     comm = self._communicators[i]

        #     if comm.name and self._names[i] is None:
        #         self._names[i] = comm.name
        #         self.app.connect_user(i, comm.name)
        #     elif self._names[i] is not None and comm.name is None:
        #         self._names[i] = None
        #         self.app.disconnect_user(i)

    def send_state(self, id_, state):
        self._communicators[id_].send(json.dumps(state))

    def receive_movement(self, id_):
        r = self._communicators[id_].receive()
        if r:
            return json.loads(r)
            
        return None

class Communicator2(object):
    def __init__(self, id_, host, port):
        self._id = id_

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((host, port))
        self._socket.listen(1)

        self._connection = None
        self._address = None

        self._inbox = []
        self._outbox = []

        self.name = None

    def clear_buffers(self):
        self._inbox = []
        self._outbox = []

    def send(self, msg):
        self._outbox.append(msg)

    def receive(self):
        if self._inbox:
            return self._inbox.pop(0)

    def _listen(self):
        try:
            chess.log.debug('NETWORK', 'Slot %d waiting connection.'%self._id)
            self._connection, self._address = self._socket.accept()
            chess.log.debug('NETWORK', 'Slot %d connected.'%self._id)
            return True
        except:
            chess.log.error('NETWORK', 'Error on connection at slot %d.'%self._id)
            return False

    def _receive_name(self):
        try:
            chess.log.debug('NETWORK', 'Slot %d waiting for user name.'%self._id)
            data = self._connection.recv(2**12)
            name = json.loads(data)

            self.name = name['name']
            chess.log.debug('NETWORK', 'Slot %d connected with user "%s".'%(self._id, self.name))
            return True
        except:
            chess.log.error('NETWORK', 'Error on receiving name at slot %d.'%self._id)
            return False

    def _receive_data(self):
        try:
            data = self._connection.recv(2**12)

            if data:
                self._inbox.append(data)
                chess.log.debug('NETWORK', 'Slot %s received: "%s"'%(self._id, data))
                return True
            else:
                return False
        except socket.timeout as e:
            return True

    def _send_data(self):
        while self._outbox:
            data = self._outbox.pop(0)
            self._connection.sendall(data)
            chess.log.debug('NETWORK', 'Slot %s sent: "%s"'%(self._id, data))

        return True

    def run(self):
        while True:
            self.name = None

            worked = self._listen()
            if not worked: continue

            worked = self._receive_name()
            if not worked: continue

            try:
                self._connection.settimeout(0.01)

                while True:
                    worked = self._receive_data()
                    if not worked: raise socket.error

                    worked = self._send_data()
                    if not worked: raise socket.error

            except socket.error as e:
                chess.log.debug('NETWORK', 'Slot %d disconnected.'%self._id)

class Communicator(object):
    def __init__(self, host, port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((host, port))
        self._socket.listen(1)
        self._running = True

        self._connection = None
        self._address = None

        self._inbox = []
        self._outbox = []

        self.name = None

    def clear_buffers(self):
        self._inbox = []
        self._outbox = []

    def send(self, msg):
        self._outbox.append(msg)

    def receive(self):
        if self._inbox:
            return self._inbox.pop(0)

    def stop(self):
        self._socket.close()
        self._running = False

    def _listen(self):
        try:
            # chess.log.debug('NETWORK', 'Communicator waiting connection.')
            self._connection, self._address = self._socket.accept()
            chess.log.debug('NETWORK', 'Communicator connected.')
            return True
        except socket.timeout as e:
            return False
        except:
            chess.log.error('NETWORK', 'Error on connection.')
            return False

    def _receive_name(self):
        try:
            # chess.log.debug('NETWORK', 'Communicator waiting for user name.')
            data = self._connection.recv(2**12)
            name = json.loads(data)

            self.name = name['name']
            chess.log.debug('NETWORK', 'Communicator connected with user "%s".'%self.name)
            return 1
        except socket.timeout as e:
            return 0
        except:
            chess.log.error('NETWORK', 'Error on receiving name.')
            return -1

    def _receive_data(self):
        try:
            data = self._connection.recv(2**12)

            if data:
                self._inbox.append(data)
                chess.log.debug('NETWORK', 'Communicator received: "%s"'%data)
                return True
            else:
                return False
        except socket.timeout as e:
            return True

    def _send_data(self):
        while self._outbox:
            data = self._outbox.pop(0)
            self._connection.sendall(data)
            chess.log.debug('NETWORK', 'Communicator sent: "%s"'%data)

        return True

    def run(self):
        while self._running:
            self.name = None

            self._socket.settimeout(0.1)
            worked = self._listen()
            if not worked: continue

            try:
                self._connection.settimeout(0.01)

                while self._running:
                    worked = self._receive_name()
                    if worked == 1: break
                    elif worked == -1: raise socket.error

                while self._running:
                    # print 'trying to receive'
                    worked = self._receive_data()
                    if not worked: raise socket.error

                    # print 'trying to send'
                    worked = self._send_data()
                    if not worked: raise socket.error

            except socket.error as e:
                chess.log.debug('NETWORK', 'Communicator disconnected.')
