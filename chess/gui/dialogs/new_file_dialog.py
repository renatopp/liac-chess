import math

import wx
import wx.lib.scrolledpanel as scrolled
from wx.lib.wordwrap import wordwrap

import chess

__all__ = ['NewFileDialog']

class NewFileDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(NewFileDialog, self).__init__(*args, **kwargs)

        self.main_panel = wx.Panel(self, -1)
        self.player_panel = wx.Panel(self.main_panel, -1, style=wx.STATIC_BORDER)
        # self.player_panel.SetBackgroundColour('#eeeeee')
        self.mode_panel = wx.Panel(self.main_panel, -1, style=wx.STATIC_BORDER)
        # self.mode_panel.SetBackgroundColour('#eeeeee')
        self.button_panel = wx.Panel(self.main_panel, -1, style=wx.STATIC_BORDER)
        self.button_panel.SetBackgroundColour('#bbbbbb')

        # b = wx.ToggleButton(self.panel, -1, "Pawns and Rooks", size=(100, 100))
        # b.SetBitmap(chess.resources.get('preview_pawnbattle_pr'), wx.TOP)

        self.create_player_box(self.player_panel)
        self.create_mode_box(self.mode_panel)
        self.create_button_box(self.button_panel)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.player_panel, 2, wx.EXPAND)
        hbox.Add(self.mode_panel, 8, wx.EXPAND)
        vbox.Add(hbox, 1, wx.EXPAND)
        vbox.Add(self.button_panel, 0, wx.EXPAND)
        self.main_panel.SetSizer(vbox)

        # b.Bind(wx.EVT_SET_FOCUS, self.on_set_focus)
        # b.Bind(wx.EVT_KILL_FOCUS, self.on_kill_focus)
        self.Centre()

    def create_player_box(self, panel):
        images = [
            chess.resources.get('mode_free'),
            chess.resources.get('mode_humanvshuman'),
            chess.resources.get('mode_humanvsai'),
            chess.resources.get('mode_aivsai')
        ]
        titles = ['Free Move', 'Human vs Human', 'Human vs AI', 'AI vs AI']
        names = [chess.PLAYER_MODE_FREE, chess.PLAYER_MODE_HUMANHUMAN, 
                 chess.PLAYER_MODE_HUMANAI, chess.PLAYER_MODE_AIAI,]


        self.player_box_tile = wx.StaticText(panel, -1, 'Player Mode', style=wx.ALIGN_CENTER)
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self.player_box_tile.SetFont(font)
        self.player_box_tile.SetBackgroundColour('#dddddd')

        self.player_box = ButtonBox(panel, -1, names, images, titles, 1)
        self.player_box.select(-1)
        
        hbox = wx.BoxSizer(wx.VERTICAL)
        hbox.AddSpacer(15)
        hbox.Add(self.player_box_tile, 0, wx.EXPAND)
        hbox.Add(self.player_box, 1, wx.EXPAND)
        # hbox.AddSpacer(15)
        panel.SetSizer(hbox)

    def create_mode_box(self, panel):
        self.mode_box = None

        levels = chess.levels.values()
        keys = chess.levels.keys()
        categories = set([l['category'] for l in levels])
        
        self.player_box_tile = wx.StaticText(panel, -1, 'Game Mode', style=wx.ALIGN_CENTER)
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        # self.player_box_tile.SetBackgroundColour('cyan')
        self.player_box_tile.SetFont(font)
        self.player_box_tile.SetBackgroundColour('#dddddd')

        images = []
        titles = []
        names = []

        for category in categories:
            images_ = []
            titles_ = []
            names_ = []

            for key, level in zip(keys, levels):
                if level['category'] != category: continue

                img_name = 'preview_'+key
                if img_name in chess.resources.bitmaps:
                    img = chess.resources.get(img_name)
                else:
                    img = chess.resources.get('preview_unknown')

                title = level['name']

                images_.append(img)
                titles_.append(title)
                names_.append(key)

            images.append(images_)
            titles.append(titles_)
            names.append(names_)

            # box = ButtonBox(panel, -1, images, titles, 4)
            # hbox.Add(box, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.ALIGN_TOP)
            # self.mode_boxes.append(box)


        self.mode_box = ButtonBox(panel, -1, names, images, titles, 5, categories)
        self.mode_box.select(0)

        hbox = wx.BoxSizer(wx.VERTICAL)
        hbox.AddSpacer(15)
        hbox.Add(self.player_box_tile, 0, wx.EXPAND)
        hbox.AddSpacer(15)
        hbox.Add(self.mode_box, 1, wx.EXPAND|wx.ALIGN_TOP)
        hbox.AddSpacer(15)
        panel.SetSizer(hbox)

    def create_button_box(self, panel): 

        button = wx.Button(panel, -1, 'New Game')

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(15)
        vbox.Add(button, 0, wx.ALIGN_CENTER)
        vbox.AddSpacer(15)

        panel.SetSizer(vbox)

        button.Bind(wx.EVT_BUTTON, self.on_button)

    def on_button(self, event):
        game_mode = self.mode_box._selected.GetName()
        player_mode = self.player_box._selected.GetName()
        
        chess.app.new_game(player_mode, game_mode)
        self.Destroy()

class ButtonBox(scrolled.ScrolledPanel):
    def __init__(self, parent, id, names, images, titles, columns, categories=None):
        super(ButtonBox, self).__init__(parent, id)

        self._buttons = []
        self._selected = None

        self.create_buttons(names, images, titles, columns, categories)

    def select(self, idx):
        btn = self._buttons[idx]

        if self._selected is not None:
            self._selected.SetValue(False)

        self._selected = btn
        self._selected.SetValue(True)
        
    def create_buttons(self, names, images, titles, columns, categories):
        if categories is None:
            box = self.create_category(names, images, titles, columns)
            self.SetAutoLayout(1)
            self.SetSizer(box)
        else:

            hbox = wx.BoxSizer(wx.VERTICAL)
            for category, nams, imgs, tits in zip(categories, names, images, titles):

                title = wx.StaticText(self, -1, category, style=wx.ALIGN_CENTER)
                font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
                title.SetFont(font)

                box = self.create_category(nams, imgs, tits, columns, hbox)

                hbox.Add(title, 0, wx.EXPAND)
                hbox.AddSpacer(5)
                hbox.Add(box, 0, wx.EXPAND)
                hbox.AddSpacer(30)

            self.SetSizer(hbox)
            self.SetAutoLayout(1)
            self.SetupScrolling()

    def create_category(self, names, images, titles, columns, parent=None):
        size = len(images)
        rows = math.ceil(size/float(columns))

        buttons = []
        for name, img, title in zip(names, images, titles):
            title = wordwrap(title, 110, wx.ClientDC(self))
            button = wx.ToggleButton(self, -1, title, size=(110, 120), name=name)
            button.SetBitmap(img, wx.TOP)
            button.Bind(wx.EVT_TOGGLEBUTTON, self.on_button)
            button.Bind(wx.EVT_SET_FOCUS, lambda event:None)
            self._buttons.append(button)
            buttons.append(button)

        _grid = wx.GridSizer(rows, columns, 1, 1)
        _grid.AddMany([(b, 0, wx.ALIGN_CENTER) for b in buttons])

        return _grid

    def on_button(self, event):
        # print dir(event)
        if self._selected is not None:
            self._selected.SetValue(False)
        self._selected = event.EventObject
        # print event
