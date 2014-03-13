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

__all__ = ['BoardCtrl']

class BoardCtrl(wx.Panel):
    '''This is the board widget, which shows the board and pieces of the game.
    '''

    def __init__(self, parent):
        '''Constructor.

        :param parent: the parent widget, passed directly to wx.Panel.
        '''
        super(BoardCtrl, self).__init__(
            parent=parent,
            id=-1,
            size=(640, 640),
            style=wx.NO_BORDER
        )

        self._cells = []
        self._matrix = [[None for i in xrange(8)] for j in xrange(8)]
        self._selected = None

        self._create_ui()
        self._bind_events()
        self.set_theme()

    def _create_ui(self):
        '''Create the GUI elements of this panel.'''

        grid = wx.FlexGridSizer(3, 3, 0, 0)
        grid.AddMany([
            (_Label(self, ''),           0, wx.EXPAND),
            (self._create_ui_hlabels(), 0, wx.EXPAND),
            (_Label(self, ''),           0, wx.EXPAND),
            (self._create_ui_vlabels(), 0, wx.EXPAND),
            (self._create_ui_board(),   0, wx.EXPAND),
            (self._create_ui_vlabels(), 0, wx.EXPAND),
            (_Label(self, ''),           0, wx.EXPAND),
            (self._create_ui_hlabels(), 0, wx.EXPAND),
            (_Label(self, ''),           0, wx.EXPAND),
        ])
        grid.AddGrowableRow(1)
        grid.AddGrowableCol(1)
        
        self.SetBackgroundColour('#DDDDDD')
        self.SetSizer(grid)

    def _create_ui_hlabels(self):
        '''Create the horizontal labels of the board, i.e, the column names.'''
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(_Label(self, 'a'), 1, wx.EXPAND)
        hbox.Add(_Label(self, 'b'), 1, wx.EXPAND)
        hbox.Add(_Label(self, 'c'), 1, wx.EXPAND)
        hbox.Add(_Label(self, 'd'), 1, wx.EXPAND)
        hbox.Add(_Label(self, 'e'), 1, wx.EXPAND)
        hbox.Add(_Label(self, 'f'), 1, wx.EXPAND)
        hbox.Add(_Label(self, 'g'), 1, wx.EXPAND)
        hbox.Add(_Label(self, 'h'), 1, wx.EXPAND)
        vbox.Add(hbox, 1, wx.EXPAND)
        return vbox

    def _create_ui_vlabels(self):
        '''Create the vertical labels of the board, i.e, the row names.'''
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(_Label(self, '8'), 1, wx.EXPAND)
        vbox.Add(_Label(self, '7'), 1, wx.EXPAND)
        vbox.Add(_Label(self, '6'), 1, wx.EXPAND)
        vbox.Add(_Label(self, '5'), 1, wx.EXPAND)
        vbox.Add(_Label(self, '4'), 1, wx.EXPAND)
        vbox.Add(_Label(self, '3'), 1, wx.EXPAND)
        vbox.Add(_Label(self, '2'), 1, wx.EXPAND)
        vbox.Add(_Label(self, '1'), 1, wx.EXPAND)
        hbox.Add(vbox, 1, wx.EXPAND)
        return hbox

    def _create_ui_board(self):
        '''Create the board itself.'''
        self._cells = []
        self._matrix = [[None for i in xrange(8)] for j in xrange(8)]

        grid = wx.GridSizer(8, 8, 0, 0)
        for row in xrange(7, -1, -1):
            for col in xrange(0, 8):
                cell = _BoardCell(self, board_position=(row, col))
                self._matrix[row][col] = cell
                self._cells.append(cell)
        grid.AddMany([(c, 0, wx.EXPAND) for c in self._cells])
        return grid

    def _bind_events(self):
        '''Bind chess events.'''

        chess.events.on(chess.EVT_GAME_NEW, self._on_board_update)
        chess.events.on(chess.EVT_GAME_RESET, self._on_board_update)
        chess.events.on(chess.EVT_TURN_MOVE, self._on_board_update)
        chess.events.on(chess.EVT_CELL_SELECT, self._on_cell_select)

    def _on_board_update(self, event):
        '''Callback called for all events that changes the board configuration.

        :param event: a `chess.Event` object.
        '''
        board = event.board
        for piece, cell in zip(board, self._cells):
            if piece != cell.piece_name:
                cell.set_piece(piece)
            
            cell.clear_overlay()

    def _on_cell_select(self, event):
        '''Callback called for the cell selection event.

        :param event: a `chess.Event` object.
        '''
        for cell in self._cells:
            cell.clear_overlay()

        if event.selected_cell is not None:
            row, col = event.selected_cell
            self._matrix[row][col].select()

        for row, col in event.highlighted_cells:
            self._matrix[row][col].highlight()

    def set_theme(self, name='default'):
        '''Set the theme of the board.

        The name must be a registred theme.

        :param name: a string with the theme name.
        '''
        theme = chess.themes[name]

        cell_colors = [
            theme['light_color'],
            theme['dark_color']
        ]
        for i, cell in enumerate(self._cells):
            idx = (i + i/8)%2
            cell.SetBackgroundColour(cell_colors[idx])
            cell.Refresh()


class _Label(wx.PyWindow):
    '''A centered label, for descriving the board columns and rows labels.'''

    def __init__(self, parent, text):
        wx.PyWindow.__init__(self, parent, -1)#, style=wx.SIMPLE_BORDER)
        self.text = text
        self.bestsize = (20, 20)
        self.SetSize(self.GetBestSize())
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.SetBackgroundColour('#DDDDDD')
    
    def OnPaint(self, evt):
        sz = self.GetSize()
        dc = wx.PaintDC(self)
        w,h = dc.GetTextExtent(self.text)
        dc.Clear()
        dc.DrawText(self.text, (sz.width-w)/2, (sz.height-h)/2)

    def OnSize(self, evt):
        self.Refresh()

    def DoGetBestSize(self):
        return self.bestsize

class _BoardCell(wx.Panel):
    '''A single board cell.'''

    def __init__(self, parent, board_position):
        '''Constructor.

        :param parent: the widget parent.
        :board_position: the cell position in board.
        '''
        super(_BoardCell, self).__init__(
            parent=parent,
            id=-1,
            size=(64, 64),
            style=wx.NO_BORDER
            # style=wx.SIMPLE_BORDER
        )

        self.board = parent
        self.board_position = board_position
        self.piece_name = '.'
        self.piece_bitmap = None
        self.overlay_bitmap = None
        
        self._size = (128, 128)
        self._highlighted = False
        self._selected = False

        self.SetBackgroundColour('#FFF')
        self.Bind(wx.EVT_SIZE, self._on_resize)
        self.Bind(wx.EVT_LEFT_DOWN, self._on_click)
        self.Bind(wx.EVT_PAINT, self._on_paint)

    def _resize_bitmap(self, bitmap):
        w, h = self._size

        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(w, h, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.BitmapFromImage(image)

        return bitmap

    def highlight(self):
        self._highlighted = True
        self._selected = False
        self.Refresh()

    def select(self):
        self._selected = True
        self._highlighted = False
        self.Refresh()

    def clear_overlay(self):
        if self._selected or self._highlighted:
            self._selected = False
            self._highlighted = False
            self.Refresh()

    def set_piece(self, name):
        if name == '.':
            self.piece_name = name
            self.piece_bitmap = None
        
        else:
            self.piece_name = name
            self.piece_bitmap = self._resize_bitmap(chess.resources.get(name))

        self.Refresh()

    def _on_paint(self, evt):
        dc = wx.PaintDC(self)
        dc.Clear()
        if self.piece_bitmap is not None:
            dc.DrawBitmap(self.piece_bitmap, 0, 0, False)

        if self._highlighted:
            image = chess.resources.get('overlay_moveable')
            bitmap = self._resize_bitmap(image)
            dc.DrawBitmap(bitmap, 0, 0, True)
        
        elif self._selected:
            image = chess.resources.get('overlay_selected')
            bitmap = self._resize_bitmap(image)
            dc.DrawBitmap(bitmap, 0, 0, True)

    def _on_click(self, event):
        chess.app.select_cell(self.board_position)

    def _on_resize(self, event):
        self._size = event.GetSize()
        
        if self.piece_bitmap:
            image = chess.resources.get(self.piece_name)
            self.piece_bitmap = self._resize_bitmap(image)

        self.Refresh()
        