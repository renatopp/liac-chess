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

import logging

__all__ = ['Logger']


class Logger(object):
    def __init__(self):
        logging.basicConfig(
            # filename=FILE,
            format='%(message)s', 
            level=logging.DEBUG
        )
        self.logger = logging.getLogger('LIAC_CHESS')
        # self.logger.addFilter(DebugFilter())

    def __format(self, scope, message):
        return '%s: %s' % (scope.upper(), message)

    def info(self, scope, message):
        self.logger.info(self.__format(scope, message))

    def debug(self, scope, message):
        self.logger.debug(self.__format(scope, message))

    def warning(self, scope, message):
        self.logger.warning(self.__format(scope, message))

    def error(self, scope, message):
        self.logger.error(self.__format(scope, message))