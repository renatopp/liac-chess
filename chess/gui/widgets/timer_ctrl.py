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

__all__ = ['TimerCtrl']

class TimerCtrl(wx.Panel):
    '''A timer widget to tracking the turn time.'''

    def __init__(self, parent):
        '''Constructor.

        :param parent: the parent widget, passed directly to wx.Panel.
        '''
        super(TimerCtrl, self).__init__(parent, -1, style=wx.DOUBLE_BORDER)

        self._minutes = 0
        self._seconds = 0

        self._create_ui()
        self._bind_events()

    def _create_ui(self):
        '''Create the GUI elements of this panel.'''

        font = wx.Font(48, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL)
        self._static_text = wx.StaticText(
            parent=self, 
            id=-1,
            label='00:00',
            style=wx.ALIGN_CENTER
        )
        self._static_text.SetForegroundColour('#DDDDDD')
        self._static_text.SetBackgroundColour('#555555')
        self._static_text.SetFont(font)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self._static_text, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def _bind_events(self):
        '''Bind chess events.'''

        chess.events.on(chess.EVT_TURN_TICK, self._on_timer_update)
        chess.events.on(chess.EVT_TURN_END, self._on_timer_update)
        chess.events.on(chess.EVT_GAME_NEW, self._on_timer_update)

    def _on_timer_update(self, event):
        '''Callback called for all events that update this clock.

        :param event: a `chess.Event` object.
        '''
        time = event.move_time
        minutes = time//60
        seconds = time%60

        self.set_value(minutes, seconds)

    def set_value(self, minutes, seconds):
        '''Set the timer to minutes:seconds.

        :param minutes: an integer with the minutes.
        :param seconds: an integer with the seconds.
        '''
        if self._minutes == minutes and self._seconds == seconds:
            return

        self._minutes = minutes
        self._seconds = seconds

        l_minutes = ('%02d'%minutes)[-2:]
        l_seconds = ('%02d'%seconds)[-2:]

        value = ':'.join([l_minutes, l_seconds])
        self._static_text.SetLabel(value)
        self.Refresh()
        self.Layout()
