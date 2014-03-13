import unittest

class BoardTestCase(unittest.TestCase):
    def setUp(self):
        import chess
        chess.config = {
            "slot_0_ip": "",
            "slot_0_port": 50100,
            "slot_1_ip": "",
            "slot_1_port": 50200,
            "update_frequency": 10,
            "max_move_time": 5.9,
            "max_infractions": 5
        }