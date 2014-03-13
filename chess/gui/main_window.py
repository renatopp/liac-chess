import wx
import wx.gizmos
import chess
import time
import webbrowser

__all__ = ['MainWindow']

class MainWindow(wx.Frame):
    '''The main window.'''

    def __init__(self, app, *args, **kwargs):
        '''Constructor.

        :param app: the `chess.App` object.
        :param args: the argument list, passed directly to wx.Frame.
        :param kwargs: the argument list, passed directly to wx.Frame.
        '''
        super(MainWindow, self).__init__(*args, **kwargs)

        self.app = app
        
        self._create_ui()
        self._bind_events()

        self.SetMinSize((708, 446))
        self.Center()
        self.Show()

    def _create_ui(self):
        '''Create the GUI elements of this window.'''

        self._create_ui_icon()
        self._create_ui_menu()

        vbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(self._create_ui_board(), 1, wx.SHAPED|wx.ALIGN_CENTER, 0)
        vbox.Add(self._create_ui_sidebar(), 0, wx.EXPAND|wx.BOTTOM|wx.TOP, 0)
        self.SetSizer(vbox)

    def _create_ui_icon(self):
        '''Create the fav icon.'''

        favicon = wx.Icon('assets/ico/liac_chess.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        self.SetIcon(favicon)

    def _create_ui_menu(self):
        '''Create the menu bar.'''

        self._menu = wx.MenuBar()
        self.SetMenuBar(self._menu)

        # MENUS ---------------------------------------------------------------
        self._menu_game = wx.Menu()
        self._menu_themes = wx.Menu()
        self._menu_help = wx.Menu()

        self._menu.Append(self._menu_game, '&Game')
        self._menu.Append(self._menu_themes, '&Themes')
        self._menu.Append(self._menu_help, '&Help')
        # ---------------------------------------------------------------------

        # MENU GAME -----------------------------------------------------------
        self._menu_game_newgame = self._menu_game.Append(-1, '&New Game')
        self._menu_game.AppendSeparator()
        self._menu_game_startgame = self._menu_game.Append(-1, '&Start Game')
        self._menu_game_pausegame = self._menu_game.Append(-1, '&Pause Game')
        self._menu_game_resetgame = self._menu_game.Append(-1, '&Reset Game')
        self._menu_game.AppendSeparator()
        self._menu_game_quit = self._menu_game.Append(-1, '&Quit')

        self.Bind(wx.EVT_MENU, self._on_btn_newgame, self._menu_game_newgame)
        self.Bind(wx.EVT_MENU, self._on_btn_startgame, self._menu_game_startgame)
        self.Bind(wx.EVT_MENU, self._on_btn_pausegame, self._menu_game_pausegame)
        self.Bind(wx.EVT_MENU, self._on_btn_resetgame, self._menu_game_resetgame)
        self.Bind(wx.EVT_MENU, self._on_btn_quit, self._menu_game_quit)
        # ---------------------------------------------------------------------

        # MENU THEMES ---------------------------------------------------------
        id_ = 10000
        for theme in chess.themes.keys():
            name = chess.themes[theme]['name']
            item = self._menu_themes.Append(id_, name)
            self.Bind(wx.EVT_MENU, self._on_btn_changetheme, item)
            id_ += 1            
        # ---------------------------------------------------------------------

        # MENU HELP -----------------------------------------------------------
        self._menu_help_docs = self._menu_help.Append(-1, '&Documentation')
        self.Bind(wx.EVT_MENU, self._on_btn_doc, self._menu_help_docs)
        # ---------------------------------------------------------------------
    
    def _create_ui_board(self):
        '''Create the board widget.'''
        self.board = chess.gui.widgets.BoardCtrl(self)
        return self.board

    def _create_ui_sidebar(self):
        '''Create the side bar widgets.'''

        panel = wx.Panel(self, size=(300, 1), style=wx.DOUBLE_BORDER|wx.ALIGN_CENTER)

        # TIMER CONTROL -------------------------------------------------------
        self.timer = chess.gui.widgets.TimerCtrl(panel)
        # ---------------------------------------------------------------------

        # WHITE PLAYER INFO ---------------------------------------------------
        self.white_user = chess.gui.widgets.PlayerInfoCtrl(panel, chess.WHITE)
        # ---------------------------------------------------------------------

        # BLACK PLAYER INFO ---------------------------------------------------
        self.black_user = chess.gui.widgets.PlayerInfoCtrl(panel, chess.BLACK)
        # ---------------------------------------------------------------------

        # NOTIFICATION PANEL --------------------------------------------------
        self._notif_panel = wx.Panel(panel, -1, style=wx.DOUBLE_BORDER|wx.ALIGN_CENTER)
        
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.FONTWEIGHT_BOLD)
        self._notif_text = wx.StaticText(self._notif_panel, -1, '', style=wx.ALIGN_CENTER)
        self._notif_text.SetFont(font)

        self._button_switchplayers = wx.Button(self._notif_panel, -1, "Switch Players", size=(-1, 30))
        self._button_switchplayers.SetBitmap(chess.resources.get('icon_switch'), wx.LEFT)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.AddSpacer(7)
        vbox.Add(self._notif_text, wx.EXPAND|wx.ALIGN_CENTER, border=0)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(7)
        hbox.Add(vbox, 2, wx.EXPAND|wx.ALIGN_CENTER, border=0)
        hbox.Add(self._button_switchplayers, 1, wx.EXPAND, border=0)
        self._notif_panel.SetSizer(hbox)

        self._button_switchplayers.Bind(wx.EVT_BUTTON, self._on_btn_switchplayers)
        # ---------------------------------------------------------------------

        # BUTTON PANEL --------------------------------------------------------
        btn_panel = wx.Panel(panel, -1, style=wx.DOUBLE_BORDER|wx.ALIGN_CENTER)

        self._button_startname = wx.Button(btn_panel, -1, "Start Game", size=(-1, 30))
        self._button_pausegame = wx.Button(btn_panel, -1, "Pause Game", size=(-1, 30))
        self._button_resetgame = wx.Button(btn_panel, -1, "Reset Game", size=(-1, 30))
        # self._button_startname.SetBitmap(chess.resources.get('icon_play'), wx.LEFT)
        # self._button_pausegame.SetBitmap(chess.resources.get('icon_pause'), wx.LEFT)
        # self._button_resetgame.SetBitmap(chess.resources.get('icon_reload'), wx.LEFT)
        
        self._button_startname.Bind(wx.EVT_BUTTON, self._on_btn_startgame)
        self._button_pausegame.Bind(wx.EVT_BUTTON, self._on_btn_pausegame)
        self._button_resetgame.Bind(wx.EVT_BUTTON, self._on_btn_resetgame)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self._button_startname, 1, flag=wx.ALIGN_CENTER, border=5)
        hbox.Add(self._button_pausegame, 1, flag=wx.ALIGN_CENTER, border=5)
        hbox.Add(self._button_resetgame, 1, flag=wx.ALIGN_CENTER, border=5)
        btn_panel.SetSizer(hbox)
        # ---------------------------------------------------------------------

        # HISTORIC CONTROL ----------------------------------------------------
        self._historic = chess.gui.widgets.HistoricCtrl(panel)
        # ---------------------------------------------------------------------

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.timer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 1)
        vbox.AddSpacer(15)
        vbox.Add(self.white_user, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 1)
        vbox.AddSpacer(3)
        vbox.Add(self.black_user, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 1)
        vbox.AddSpacer(3)
        vbox.Add(self._notif_panel, 0, wx.ALIGN_CENTER, 1)
        vbox.AddSpacer(15)
        vbox.Add(btn_panel, 0, wx.EXPAND, 1)
        vbox.AddSpacer(15)
        vbox.Add(self._historic, 1, wx.EXPAND, 1)
        panel.SetSizer(vbox)

        return panel    

    def _bind_events(self):
        '''Bind chess events.'''

        chess.events.on(chess.EVT_GAME_NEW, self._on_notif_update)
        chess.events.on(chess.EVT_GAME_RESET, self._on_notif_update)
        chess.events.on(chess.EVT_TURN_BEGIN, self._on_notif_update)
        chess.events.on(chess.EVT_TURN_END, self._on_notif_update)

    # INTERFACE ===============================================================
    def set_notification(self, msg):
        self._notif_text.SetLabel(msg)
        self._notif_text.Refresh()
        self._notif_panel.Layout()

    def enable_start_game(self, value):
        self._menu_game_startgame.Enable(value)
        self._button_startname.Enable(value)

    def enable_pause_game(self, value):
        self._menu_game_pausegame.Enable(value)
        self._button_pausegame.Enable(value)

    def enable_reset_game(self, value):
        self._menu_game_resetgame.Enable(value)
        self._button_resetgame.Enable(value)

    def enable_switch_players(self, value):
        self._button_switchplayers.Enable(value)
    # =========================================================================

    # EVENTS ==================================================================
    def _on_btn_changetheme(self, event):
        idx = event.Id - 10000
        theme_keys = chess.themes.keys()
        self.board.set_theme(theme_keys[idx])
        
    def _on_btn_switchplayers(self, event):
        self.app.switch_player()

    def _on_btn_startgame(self, event):
        self.app.start_game()

    def _on_btn_pausegame(self, event):
        self.app.pause_game()

    def _on_btn_resetgame(self, event):
        self.app.reset_game()

    def _on_btn_newgame(self, event):
        dialog = chess.gui.dialogs.NewFileDialog(self, -1, 'New Game', 
            size=(800, 600),
            style=wx.CAPTION|wx.CLOSE_BOX)#|wx.THICK_FRAME)
        dialog.ShowModal()

    def _on_btn_doc(self, event):
        webbrowser.open(chess.get_documentation())

    def _on_btn_quit(self, event):
        self.Destroy()

    def _on_notif_update(self, event):
        if event.player_mode == chess.PLAYER_MODE_FREE:
            self.set_notification('Free Mode.')
            return

        if event.draw:
            self.set_notification('Draw!')

        elif event.winner != chess.NONE:
            name = 'Black' if event.winner == chess.BLACK else 'White'
            self.set_notification(name + ' won!')

        else:
            name = 'Black' if event.who_moves == chess.BLACK else 'White'
            self.set_notification(name + ' turn.')
    # =========================================================================