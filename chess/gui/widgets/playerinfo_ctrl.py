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

import wx
import chess

__all__ = ['PlayerInfoCtrl']

class PlayerInfoCtrl(wx.Panel):
    '''A panel which shows the information of a given Player.

    The PlayerInfoCtrl shows the basic information of a given Player. These
    information include: the player's name, color, connection status and the 
    number of infractions.
    '''

    def __init__(self, parent, color):
        '''Constructor.

        :param parent: the parent widget, passed directly to wx.Panel.
        :param color: the color of player handled by this panel..
        '''

        super(PlayerInfoCtrl, self).__init__(
            parent=parent, 
            id=-1, 
            style=wx.DOUBLE_BORDER
        )

        self._color = color
        self._name = '[empty]'
        self._status = chess.STATUS_DISCONNECTED
        self._infractions = 0

        self._create_ui()
        self._bind_events()

    # INTERNAL ================================================================
    def _create_ui(self):
        '''Create the GUI elements of this panel.'''

        if self._color == chess.WHITE:
            piece_name = 'P'
            color_name = 'White'
        else:
            piece_name = 'p'
            color_name = 'Black'

        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.VERTICAL)
        box3 = wx.BoxSizer(wx.HORIZONTAL)
        box4 = wx.BoxSizer(wx.HORIZONTAL)

        # USER INFO ELEMENTS ==================================================
        # piece bitmap
        bitmap = chess.resources.get(piece_name)
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(48, 48, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.BitmapFromImage(image)
        self._color_bitmap = wx.StaticBitmap(self, -1, bitmap)
        
        # name
        font = wx.Font(12, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self._user_name = wx.StaticText(self, -1, '[Empty]')
        self._user_name.SetFont(font)

        # color
        font = wx.Font(8, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.LIGHT)
        self._user_color = wx.StaticText(self, -1, color_name)
        self._user_color.SetFont(font)

        # infraction
        bitmap = chess.resources.get('icon_infraction')
        font = wx.Font(10, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self._user_infractions_bitmap = wx.StaticBitmap(self, -1, bitmap)
        self._user_infractions = wx.StaticText(self, -1, '0')
        self._user_infractions.SetFont(font)

        # status
        font = wx.Font(8, wx.FONTFAMILY_MODERN, wx.ITALIC, wx.NORMAL)
        self._user_status = wx.StaticText(
            parent=self,
            id=-1,
            label='Disconnected',
            style=wx.ALIGN_RIGHT
        )
        self._user_status.SetFont(font)
        # =====================================================================

        # CONFIGURE LAYOUT ====================================================
        box1.Add(self._color_bitmap, flag=wx.EXPAND|wx.BOTTOM|wx.TOP, border=0)
        box2.AddSpacer(10)

        box4.Add(self._user_name, proportion=1, flag=wx.EXPAND, border=0)
        box4.Add(self._user_infractions_bitmap, proportion=.1, border=0)
        box4.Add(self._user_infractions, proportion=.1, border=0)
        box4.AddSpacer(10)

        box3.Add(self._user_color, proportion=1, flag=wx.EXPAND, border=0)
        box3.Add(self._user_status, proportion=1, flag=wx.EXPAND, border=0)
        box3.AddSpacer(10)

        box2.Add(box4, flag=wx.EXPAND, border=0)
        box2.Add(box3, flag=wx.EXPAND, border=0)
        box1.Add(box2, proportion=1, flag=wx.EXPAND, border=0)
        box2.AddSpacer(3)

        self.SetSizer(box1)
        # =====================================================================

    def _bind_events(self):
        '''Bind chess events.'''

        chess.events.on(chess.EVT_PLAYER_SWITCH, self._on_player_update)
        chess.events.on(chess.EVT_PLAYER_CONNECT, self._on_player_update)
        chess.events.on(chess.EVT_PLAYER_DISCONNECT, self._on_player_update)
        chess.events.on(chess.EVT_PLAYER_INFRACTION, self._on_player_update)
        chess.events.on(chess.EVT_GAME_NEW, self._on_player_update)
        chess.events.on(chess.EVT_GAME_RESET, self._on_player_update)

    def _set_infractions(self, n):
        '''Change the infraction label.

        :param n: an integer with the number of infractions.
        '''
        if self._infractions != n:
            self._infractions = n
            self._user_infractions.SetLabel(str(n))

    def _set_name(self, name):
        '''Change the player's name label.

        Note that, the player's name is limited to 15 characters.

        :param name: a string with the player's name.
        '''
        if self._name != name:
            self._name = name
            self._user_name.SetLabel(name[:15])

    def _set_status(self, status):
        '''Change the status label.

        :param status: a chess.STATUS_* constant.
        '''
        if self._status != status:
            self._status = status

            if status == chess.STATUS_CONNECTED:
                status_name = 'Connected'
                self._user_status.SetForegroundColour('#72B340')
            else:
                status_name = 'Disconnected'
                self._user_status.SetForegroundColour('#797E7A')

            self._user_status.SetLabel(status_name)

    def _on_player_update(self, event):
        '''Callback called for all events that changes a player information.

        :param event: a `chess.Event` object.
        '''
        for p in event.players:
            if p.team == self._color:
                self._set_infractions(p.infractions)
                self._set_name(p.name)
                self._set_status(p.status)
                break
        else:
            self._set_infractions(0)
            self._set_name('[empty]')
            self._set_status(chess.STATUS_DISCONNECTED)

        self.Refresh()
    # =========================================================================
