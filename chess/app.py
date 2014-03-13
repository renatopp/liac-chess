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

import math
import wx

import chess

__all__ = ['App']

class Timer(wx.Timer):
    '''A helper class to handle the framerate of the game.'''
    def __init__(self, callback):
        super(Timer, self).__init__()
        self.callback = callback

    def Notify(self):
        tick = self.GetInterval()/1000.0
        self.callback(tick)

class App(wx.App):
    '''App is the main object of Liac Chess.

    The App controls de game loop, the board representation, the user 
    interface, and player controls.
    '''

    def __init__(self):
        '''Constructor.'''

        # Calls wx.App constructor and disable the redirection of output
        super(App, self).__init__(redirect=False)

        # Internal variables
        self._state = chess.STATE_IDLE
        self._game_timer = Timer(self._game_loop)
        self._play_waiting_move = False

        self.player_mode = chess.PLAYER_MODE_FREE
        self.selected_cell = None
        self.highlighted_cells = []

        # The following variable are initialized when MainLoop is called
        self.players = []
        self.current_level = None
        self.board = None
        self.window = None

    # OVERRIDE APP ============================================================
    def MainLoop(self):
        '''Initializes the game.

        Consult the wxPython documentation.
        '''

        # Configure the GUI 
        self.window = chess.gui.MainWindow(self,
            parent=None,
            id=-1,
            title='LIAC CHESS v%s'%chess.__version__,
            size=(900, 640)
        )

        # Configure Models
        self.board = None

        # Update Player Info
        self._update_players()

        # Configure Game
        self.new_game(chess.PLAYER_MODE_FREE, 'pawnbattle_complete')
        # self.new_game(chess.PLAYER_MODE_FREE, None)

        # Start timer
        fps = 1000./chess.config['update_frequency']
        self._game_timer.Start(fps) # 10 calls per second

        super(App, self).MainLoop()
    # =========================================================================

    # INTERFACE (CAN BE USED BY OTHER MODULES) ================================
    def new_game(self, player_mode, level_name=None):
        '''Create a new game.

        This method is used to create a new game, which will erase all current 
        information about the board and player. Note that, this method will
        disconnect all networked players.

        :param player_mode: a player mode, consult chess constants.
        :param level_name: a string with the name of the level, the level must
                           be present at the ``levels.json`` file.
        '''

        chess.log.info('APP', 
            'Creating a new game (%s, %s).'%(player_mode, level_name)
        )

        self._reset()
        self._go_idle()
        self._set_level(level_name)
        
        # Disconnect and reset all players
        for player in self.players:
            player.stop()

        self.players = []

        if player_mode == chess.PLAYER_MODE_FREE:
            self.window.enable_reset_game(True)
            self.window.enable_switch_players(False)

        elif player_mode == chess.PLAYER_MODE_HUMANHUMAN:
            player1 = chess.models.HumanPlayer(
                app=self,
                team=chess.WHITE
            )

            player2 = chess.models.HumanPlayer(
                app=self,
                team=chess.BLACK
            )
            self.players = [player1, player2]
            self._go_ready()

        elif player_mode == chess.PLAYER_MODE_HUMANAI:
            player1 = chess.models.HumanPlayer(
                app=self,
                team=chess.WHITE
            )

            player2 = chess.models.NetworkPlayer(
                app=self,
                team=chess.BLACK,
                ip=chess.config['slot_1_ip'],
                port=chess.config['slot_1_port']
            )
            self.players = [player1, player2]

        elif player_mode == chess.PLAYER_MODE_AIAI:
            player1 = chess.models.NetworkPlayer(
                app=self,
                team=chess.WHITE,
                ip=chess.config['slot_0_ip'],
                port=chess.config['slot_0_port']
            )

            player2 = chess.models.NetworkPlayer(
                app=self,
                team=chess.BLACK,
                ip=chess.config['slot_1_ip'],
                port=chess.config['slot_1_port']
            )
            self.players = [player1, player2]

        else:
            chess.log.error('APP', 'Invalid player mode.')

        for player in self.players:
            player.start()
            
        self.player_mode = player_mode
        self._update_players()
        chess.events.trigger(chess.EVT_GAME_NEW)
     
    def start_game(self):
        '''Start the game.

        This method just start a idle/paused game.
        '''

        chess.log.info('APP', 'The game just start.')
        chess.events.trigger(chess.EVT_GAME_PLAY)
        self._go_play()

    def pause_game(self):
        '''Pause a game.'''

        chess.log.info('APP', 'The game just paused.')
        chess.events.trigger(chess.EVT_GAME_PAUSE)
        self._go_pause()

    def reset_game(self):
        '''Reset the current game, erasing players infractions and the board 
        configuration.'''

        chess.log.info('APP', 'The game was reseted.')

        if self.player_mode != chess.PLAYER_MODE_FREE:
            self._go_ready()

        self._reset()
        self._set_level(self.current_level)
        self._update_players()
        chess.events.trigger(chess.EVT_GAME_RESET)

    def switch_player(self):
        '''Switch the color of players.'''

        if self.players:
            team0 = self.players[0].team
            team1 = self.players[1].team
            self.players[0].team = team1
            self.players[1].team = team0
            self._update_players()

            chess.events.trigger(chess.EVT_PLAYER_SWITCH)

    def connect_user(self, player):
        '''Tells app that a player connected.

        :param player: a Player object.
        '''
        chess.log.info('APP', 'Player "%s" connected.'%player.name)
        chess.events.trigger(chess.EVT_PLAYER_CONNECT)

        if self._state == chess.STATE_IDLE:
            if all(p.status == chess.STATUS_CONNECTED for p in self.players):
                self._go_ready()

        elif self._state == chess.STATE_PAUSE:
            if all(p.status == chess.STATUS_CONNECTED for p in self.players):
                self._go_play()

        self._update_players()

    def disconnect_user(self, player):
        '''Tells app that a player disconnected.

        :param player: a Player object.
        '''

        chess.log.info('APP', 'Player "%s" disconnected.'%player.name)
        chess.events.trigger(chess.EVT_PLAYER_DISCONNECT)
        self._update_players()

        if self._state == chess.STATE_READY:
            self._go_idle()

        elif self._state == chess.STATE_PLAY:
            self._go_pause()

    def select_cell(self, pos):
        '''Called when the user click on the chess board.

        :param pos: a tuple with the clicked square.
        '''

        # FREE PLAY
        if self.player_mode == chess.PLAYER_MODE_FREE:
            self._select_cell_free(pos)


        # HUMAN PLAY
        if self.player_mode == chess.PLAYER_MODE_HUMANHUMAN or \
           self.player_mode == chess.PLAYER_MODE_HUMANAI:

            if self._state == chess.STATE_PLAY:
                for player in self.players:
                    if self.board.who_moves == player.team and \
                       isinstance(player, chess.models.HumanPlayer):

                        self._select_cell_human(player, pos)

        chess.events.trigger(chess.EVT_CELL_SELECT)
    # =========================================================================

    # INTERNAL ================================================================
    def _select_cell_free(self, pos):
        if self.selected_cell is not None:
            if self.selected_cell[0] != pos[0] or \
               self.selected_cell[1] != pos[1]:

                self.board.raw_move(self.selected_cell, pos)
        
            self.selected_cell = None
            chess.events.trigger(chess.EVT_TURN_MOVE)

        elif self.selected_cell is None and self.board[pos] is not None:
            self.selected_cell = pos

    def _select_cell_human(self, player, pos):
        to_piece = self.board[pos]

        if self.selected_cell is not None:
            from_piece = self.board[self.selected_cell]

            if to_piece is None:
                player.move(self.selected_cell, pos)
                self.selected_cell = None
                self.highlighted_cells = []

            elif from_piece == to_piece:
                self.selected_cell = None
                self.highlighted_cells = []

            elif from_piece.team == to_piece.team:
                self.selected_cell = pos
                self.highlighted_cells = self.board[pos].generate()

            else:
                player.move(self.selected_cell, pos)
                self.selected_cell = None
                self.highlighted_cells = []

        elif self.selected_cell is None and to_piece is not None:
            if to_piece.team == self.board.who_moves:
                self.selected_cell = pos
                self.highlighted_cells = self.board[pos].generate()

    def _reset(self):
        pass
        self._play_waiting_move = False
 
    def _go_idle(self):
        chess.log.debug('APP', 'Going to state IDLE.')
        self.selected_cell = None
        self._state = chess.STATE_IDLE
        self.window.enable_start_game(False)
        self.window.enable_switch_players(True)
        self.window.enable_pause_game(False)
        self.window.enable_reset_game(False)

    def _go_ready(self):
        chess.log.debug('APP', 'Going to state READY.')
        self.selected_cell = None
        self._state = chess.STATE_READY
        self.window.enable_start_game(True)
        self.window.enable_switch_players(True)
        self.window.enable_pause_game(False)
        self.window.enable_reset_game(False)

    def _go_play(self):
        chess.log.debug('APP', 'Going to state PLAY.')
        self.selected_cell = None
        self._state = chess.STATE_PLAY
        self.window.enable_start_game(False)
        self.window.enable_switch_players(False)
        self.window.enable_pause_game(True)
        self.window.enable_reset_game(True)

    def _go_pause(self):
        chess.log.debug('APP', 'Going to state PAUSE.')
        self.selected_cell = None
        self._state = chess.STATE_PAUSE
        self.window.enable_start_game(True)
        self.window.enable_switch_players(False)
        self.window.enable_pause_game(False)
        self.window.enable_reset_game(True)

    def _go_gameover(self):
        chess.log.debug('APP', 'Going to state GAMEOVER.')
        self.selected_cell = None
        self._state = chess.STATE_GAMEOVER
        self.window.enable_start_game(False)
        self.window.enable_switch_players(False)
        self.window.enable_pause_game(False)
        self.window.enable_reset_game(True)

    def _update_players(self):
        for p in self.players:
            if p.team == chess.WHITE:
                p.infractions = self.board.white_infractions
            else:
                p.infractions = self.board.black_infractions

    def _set_level(self, name=None):
        self.current_level = name

        if name:
            level = chess.levels[name]
            self.board = chess.models.Board(
                board=level['board'],
                win_methods=level['win_methods'],
                tie_methods=level['tie_methods'],
                allow_enpassant=level['allow_enpassant'],
                allow_castle=level['allow_castle'],
                allow_rook_promotion=level['allow_rook_promotion'],
                allow_queen_promotion=level['allow_queen_promotion'],
                allow_knight_promotion=level['allow_knight_promotion'],
                allow_bishop_promotion=level['allow_bishop_promotion'],
            )
        else:
            self.board = chess.models.Board()
        

    def _game_loop(self, tick):
        '''Run the game loop.

        This method is called automatically by timer.

        :param tick: the time between this loop and the last one, in 
                     milliseconds.
        '''

        # Update players, this verify their connection
        for player in self.players:
            player.update(tick)

        # If the game is really running (i.e., player pressed the start button)
        if self._state == chess.STATE_PLAY:

            # Update the board state, it verify the players infractions
            if self.board.update(tick):
                self._update_players()
                chess.events.trigger(chess.EVT_PLAYER_INFRACTION)


            # Verify the players movement
            team = self.board.who_moves

            if not self._play_waiting_move:
                chess.events.trigger(chess.EVT_TURN_BEGIN)
                self._play_waiting_move = True

                # Send the state to the player and ask him to a movement
                state = self.board.get_state()
                for player in self.players:
                    if player.team == self.board.who_moves:
                        player.set_state(state)

            else:
                chess.events.trigger(chess.EVT_TURN_TICK)

                # Verify if the player performed a movement
                for player in self.players:
                    if player.team == self.board.who_moves:
                        move = player.get_move()

                if move is not None:
                    self._play_waiting_move = False
                    m = self.board.who_moves
                    self.board.move(move[0], move[1])

                    self._update_players()

                    if self.board.who_moves == m:
                        chess.events.trigger(chess.EVT_PLAYER_INFRACTION)
                    else:
                        chess.events.trigger(chess.EVT_TURN_MOVE)

                    chess.events.trigger(chess.EVT_TURN_END)

            # Verify if the game ended
            if self.board.winner != chess.NONE:
                self._go_gameover()
                state = self.board.get_state()

                for player in self.players:
                    player.set_state(state)
                chess.events.trigger(chess.EVT_GAME_OVER)
                    
            elif self.board.draw:
                self._go_gameover()
                state = self.board.get_state()

                for player in self.players:
                    player.set_state(state)
                chess.events.trigger(chess.EVT_GAME_OVER)
    # =========================================================================
