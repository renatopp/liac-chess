# =============================================================================
# Created by Renato de Pontes Pereira - renato.ppontes@gmail.com
# =============================================================================
# Copyright (c) 2014 Renato de Pontes Pereira, renato.ppontes at gmail dot com
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
'''
# EVT_GAME_NEW ok
    # Update board
    # Update players
    # Clear movements
    # Update buttons

# EVT_GAME_PLAY ok
    # Update buttons

# EVT_GAME_PAUSE ok
    # Update buttons

# EVT_GAME_RESET ok
    # Update board
    # Update players
    # Update buttons

# EVT_GAME_OVER ok
    # Update buttons

# EVT_PLAYER_SWITCH ok
    # Update players

# EVT_PLAYER_CONNECT ok
    # Update players

# EVT_PLAYER_DISCONNECT ok
    # Update players

# EVT_PLAYER_INFRACTION ok
    # Update players

# EVT_TURN_MOVE ok
    # Update board

# EVT_TURN_BEGIN ok

# EVT_TURN_END ok

# EVT_TURN_TICK ok
    # Update clock
'''

import chess

__all__ = ['Event', 'EventDispatcher']

class Event(object):
    '''This class represents an event into the flow of the game.

    This object is passed to EventDispatcher objects.
    '''

    def __init__(self, type, **kwargs):
        '''Constructor. 

        It receives the type of the event and the target object (the main 
        object selected to handle this event). The additional arguments are 
        inserted into the Event object in order to store specific variables,
        e.g., in mouse events.

        :param type: a string with the type of the event.
        :param target: (OPTIONAL) The target object of the event.
        :param **kwargs: (OPTINAL) Specific variables of the event.
        '''

        self.type = type
        self._create()

        for k in kwargs:
            setattr(self, k, kwargs[k])

    def _create(self):
        pass
        app = chess.app
        board = app.board

        self.board = board.get_board()
        self.winner = board.winner
        self.draw = board.draw
        self.who_moves = board.who_moves
        self.move_time = board.move_time

        self.players = app.players
        self.current_player = None
        self.player_mode = app.player_mode
        
        self.selected_cell = app.selected_cell
        self.highlighted_cells = app.highlighted_cells

        for p in self.players:
            if p.team == board.who_moves:
                self.current_player = p
                break

class EventDispatcher(object):
    '''EventDispatcher is the first object of the Batma hierarchy. An object 
    that inherit from this class is able to receive, handle, and dispatch 
    events.

    The EventDispatcher contains listener callbacks, which are the functions 
    that will handle the incoming events. A listener function must receive as 
    argument a single parameter, the event.

    For a complete list of default event types, consult the user guide in 
    documentation.
    '''

    def __init__(self):
        '''Constructor.'''

        self._listeners = {}
        '''(INTERNAL) The dictionary containing the listener functions. It must
        follow the format: ``{'EVENT_NAME':[LISTENER1, LISTENER2, ...]}.``'''

    def add_event_listener(self, type, listener):
        '''Adds a new listener for a given event.

        :param type: a string with the type of the event.
        :param listener: a function callback.

        :return: the listener function.
        '''
        if type not in self._listeners:
            self._listeners[type] = []
        
        self._listeners[type].append(listener)
        return listener

    def remove_event_listener(self, type, listener):
        '''Removes a listener for a given event. It raises an exception if 
        either the listener or the event type is not registered into this 
        object.

        :param type: a string with the type of the event.
        :param listener: a function callback.
        '''
        if type in self._listeners:
            if listener in self._listeners[type]:
                self._listeners[type].remove(listener)
            else:
                pass # TODO: ERROR
        else:
            pass # TODO: ERROR

    def remove_all_event_listener(self, type=None):
        '''Removes all listeners for this object (of any event type). If the 
        argument ``type`` is not null, it removes all listeners of the 
        provided type.

        :param type: (OPTIONAL) a string with the type of the event.
        '''
        if type is None:
            if type in self._listeners:
                self._listeners[type] = []
        else:
            self._listeners = {}

    def has_event_listener(self, type):
        '''Verify if there is any listener for the event type.

        :param type: a string with the type of the event.
        :return: True or False.
        '''
        return bool(self._listeners.get(type))

    def trigger(self, type):
        '''Trigger an event to this object. Notice that, this method is
        different from ``dispatch`` method in the way that it doesn't dispatch 
        the event to its children.

        :param event: An `batma.events.Event` object.
        '''
        event = Event(type)

        for listener in self._listeners.get(type, []):
            listener(event)

    # Alias for add and remove listener.
    on = add_event_listener
    off = remove_event_listener
