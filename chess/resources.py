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

import os
import glob

import wx

import chess

__all__ = ['Resources']

class Resources(object):
    def __init__(self):
        self.bitmaps = {}

        self.bitmaps['r'] = wx.Bitmap('assets/pieces/br.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['n'] = wx.Bitmap('assets/pieces/bn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['q'] = wx.Bitmap('assets/pieces/bq.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['k'] = wx.Bitmap('assets/pieces/bk.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['b'] = wx.Bitmap('assets/pieces/bb.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['p'] = wx.Bitmap('assets/pieces/bp.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['R'] = wx.Bitmap('assets/pieces/wr.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['N'] = wx.Bitmap('assets/pieces/wn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['Q'] = wx.Bitmap('assets/pieces/wq.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['K'] = wx.Bitmap('assets/pieces/wk.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['B'] = wx.Bitmap('assets/pieces/wb.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['P'] = wx.Bitmap('assets/pieces/wp.png', wx.BITMAP_TYPE_PNG)

        self.bitmaps['overlay_selected'] = wx.Bitmap('assets/pieces/overlay_selected.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['overlay_moveable'] = wx.Bitmap('assets/pieces/overlay_moveable.png', wx.BITMAP_TYPE_PNG)
        # self.bitmaps['icon'] = wx.Bitmap('assets/ico/liac_chess.ico', wx.BITMAP_TYPE_ICO)

        self.bitmaps['icon_switch'] = wx.Bitmap('assets/icons/icon_switch.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['icon_play'] = wx.Bitmap('assets/icons/icon_play.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['icon_pause'] = wx.Bitmap('assets/icons/icon_pause.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['icon_reload'] = wx.Bitmap('assets/icons/icon_reload.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['icon_infraction'] = wx.Bitmap('assets/icons/icon_infraction.png', wx.BITMAP_TYPE_PNG)
        
        self.bitmaps['preview_pawnbattle_pr'] = wx.Bitmap('assets/modes/pawnbattle_pr.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pb'] = wx.Bitmap('assets/modes/pawnbattle_pb.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pq'] = wx.Bitmap('assets/modes/pawnbattle_pq.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_prb'] = wx.Bitmap('assets/modes/pawnbattle_prb.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pqb'] = wx.Bitmap('assets/modes/pawnbattle_pqb.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pqr'] = wx.Bitmap('assets/modes/pawnbattle_pqr.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pqrb'] = wx.Bitmap('assets/modes/pawnbattle_pqrb.png', wx.BITMAP_TYPE_PNG)

        self.bitmaps['preview_pawnbattle_pn'] = wx.Bitmap('assets/modes/pawnbattle_pn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pbn'] = wx.Bitmap('assets/modes/pawnbattle_pbn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_prn'] = wx.Bitmap('assets/modes/pawnbattle_prn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pqn'] = wx.Bitmap('assets/modes/pawnbattle_pqn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_prbn'] = wx.Bitmap('assets/modes/pawnbattle_prbn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_pqrn'] = wx.Bitmap('assets/modes/pawnbattle_pqrn.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_complete'] = wx.Bitmap('assets/modes/pawnbattle_complete.png', wx.BITMAP_TYPE_PNG)

        self.bitmaps['preview_pawnbattle_2p'] = wx.Bitmap('assets/modes/pawnbattle_2p.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_4p'] = wx.Bitmap('assets/modes/pawnbattle_4p.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_6p'] = wx.Bitmap('assets/modes/pawnbattle_6p.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_pawnbattle_8p'] = wx.Bitmap('assets/modes/pawnbattle_8p.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['preview_unknown'] = wx.Bitmap('assets/modes/unknown.png', wx.BITMAP_TYPE_PNG)

        self.bitmaps['mode_free'] = wx.Bitmap('assets/modes/free.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['mode_humanvshuman'] = wx.Bitmap('assets/modes/humanvshuman.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['mode_humanvsai'] = wx.Bitmap('assets/modes/humanvsai.png', wx.BITMAP_TYPE_PNG)
        self.bitmaps['mode_aivsai'] = wx.Bitmap('assets/modes/aivsai.png', wx.BITMAP_TYPE_PNG)

    def get(self, name):
        return self.bitmaps[name]
        