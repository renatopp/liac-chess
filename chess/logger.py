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