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

__author__ = 'Renato de Pontes Pereira'
__version__ = '1.0.0'

import sys
import os
import json
import collections

from chess.constants import *

from chess import network
from chess import models
from chess import gui
from chess.app import *
from chess.resources import *
from chess.events import *
from chess.logger import Logger

def load_themes():
    '''Loads the themes file.'''

    global themes
    log.debug('INIT', 'Loading themes file.')
    themes = json.load(open('data/themes.json'), object_pairs_hook=collections.OrderedDict)
    log.debug('INIT', 'Themes loaded successfully.')

def load_configs():
    '''Loads the configuration file.'''

    global config
    log.debug('INIT', 'Loading configuration file.')
    config = json.load(open('data/config.json'), object_pairs_hook=collections.OrderedDict)
    log.debug('INIT', 'Configurations loaded successfully.')

def load_levels():
    '''Loads the levels file.'''

    global levels
    log.debug('INIT', 'Loading levels file.')
    levels = json.load(open('data/levels.json'), object_pairs_hook=collections.OrderedDict)
    log.debug('INIT', 'Levels loaded successfully.')

def get_documentation():
    '''Get the path for documentation.'''

    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        datadir = os.path.dirname(__file__)
        datadir = os.path.join(datadir, '..')

    filename = os.path.join(datadir, 'docs', 'build', 'html', 'index.html')
    path = 'file:///' + filename
    return path

def run():
    '''Run Liac Chess.'''

    global app
    global resources 

    app = App()
    load_themes()
    load_levels()
    load_configs()
    resources = Resources()

    app.MainLoop()

# GLOBALS =====================================================================
app = None
config = None
resources = None
log = Logger()
events = EventDispatcher()
themes = {}
levels = {}
# =============================================================================

