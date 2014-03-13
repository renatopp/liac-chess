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

WHITE = 1
NONE = 0
BLACK = -1

PAWN = 'p'
ROOK = 'r'
KING = 'k'
QUEEN = 'q'
KNIGHT = 'n'
BISHOP = 'b'

BLACK_PAWN = 'p'
BLACK_ROOK = 'r'
BLACK_KING = 'k'
BLACK_QUEEN = 'q'
BLACK_KNIGHT = 'n'
BLACK_BISHOP = 'b'

WHITE_PAWN = 'P'
WHITE_ROOK = 'R'
WHITE_KING = 'K'
WHITE_QUEEN = 'Q'
WHITE_KNIGHT = 'N'
WHITE_BISHOP = 'B'

STATUS_CONNECTED = 0
STATUS_DISCONNECTED = 1

STATE_IDLE = 0
STATE_READY = 1
STATE_PLAY = 2
STATE_PAUSE = 3
STATE_GAMEOVER = 4

PLAYER_MODE_FREE = 'FREE'
PLAYER_MODE_HUMANHUMAN = 'HUMANHUMAN'
PLAYER_MODE_HUMANAI = 'HUMANAI'
PLAYER_MODE_AIAI = 'AIAI'

EVT_GAME_NEW = 0
EVT_GAME_PLAY = 1
EVT_GAME_PAUSE = 2
EVT_GAME_RESET = 3
EVT_GAME_OVER = 4
EVT_PLAYER_SWITCH = 5
EVT_PLAYER_CONNECT = 6
EVT_PLAYER_DISCONNECT = 7
EVT_PLAYER_INFRACTION = 8
EVT_TURN_MOVE = 9
EVT_TURN_BEGIN = 10
EVT_TURN_END = 11
EVT_TURN_TICK = 12
EVT_CELL_SELECT = 13