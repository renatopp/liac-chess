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

import  wx
import  wx.lib.mixins.listctrl  as  listmix

__all__ = ['HistoricCtrl']


class HistoricCtrl(wx.Panel):
    def __init__(self, parent):
        super(HistoricCtrl, self).__init__(parent, -1)

        self._create_ui()

    def _create_ui(self):
        self._list = _HistoricList(
            parent=self,
            id=-1,
            style=wx.LC_REPORT|wx.DOUBLE_BORDER|wx.LC_SORT_ASCENDING
                              |wx.LC_VRULES|wx.LC_HRULES
        )

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self._list, 1, flag=wx.EXPAND)
        self.SetSizer(hbox)

class _HistoricList(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

        self.InsertColumn(0, "#", wx.LIST_FORMAT_RIGHT)
        self.InsertColumn(1, "White Move", wx.LIST_FORMAT_CENTER)
        self.InsertColumn(2, "Black Move", wx.LIST_FORMAT_CENTER)

        self.SetColumnWidth(0, 30)
        self.SetColumnWidth(1, 130)
        self.SetColumnWidth(2, 130)
