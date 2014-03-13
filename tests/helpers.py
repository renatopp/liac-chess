

WHITE = 1
BLACK = -1
NONE = 0

POS = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
}

def C(pos):
    row = int(pos[1]) - 1
    col = POS[pos[0]]
    return row, col

class StubBoard(object):
    def __init__(self):
        self._cells = [[None for j in xrange(8)] for i in xrange(8)]
        self.enpassant = None

    def __getitem__(self, pos):
        row, col = pos
        return self._cells[row][col]

    def __setitem__(self, pos, piece):
        row, col = pos
        self._cells[row][col] = piece

    def is_empty(self, pos):
        return self[pos] is None

    def is_enpassant(self, pos):
        enp = self.enpassant
        return enp and enp[0] == pos[0] and enp[1] == pos[1]

        
class StubPiece(object):
    def __init__(self, board, team, position):
        self.board = board
        self.team = team
        self.position = position
