#! /usr/bin/env python3
import platform
import time
import sys
__isatty__=sys.stdout.isatty()
def cprint(*value, sep=' ', end='\n', colour=1, bold=True):
    msg = sep.join(map(str, value)) + end
    file=sys.stdout
    if __isatty__:
        if 'idlelib' in list(sys.modules):
            if colour == 31:
                file = sys.stderr
        else:
            if platform.system() == 'Linux':
                addcolour = '\033[%s;%sm' % (int(bool(bold)), colour)
                endcolour = '\x1b[0m'
                msg = addcolour + msg.replace(endcolour, addcolour) + endcolour
    file.write(msg)
class Logger(object):
    def __init__(self, level=0):
        if level<1:
            self.level=0
        elif level<2:
            self.level=1
        elif level<3:
            self.level=2
        else:
            self.level=0
            self.error('Specified log level(%s) not in allowed levels [0, 1, 2]' % level)
            self.info('Log level 0 assumed')

    def info(self, *value, sep=' ', end='\n'):
        if self.level==0:
            msg=[time.strftime('[%H:%M:%S]'),
                 '[INFO]',
                 *value]
            cprint(*msg, sep=sep, end=end, colour=32)
    def warning(self, *value, sep=' ', end='\n'):
        if self.level<2:
            msg=[time.strftime('[%H:%M:%S]'),
                 '[WARNING]',
                 *value]
            cprint(*msg, sep=sep, end=end, colour=33)
    def error(self, *value, sep=' ', end='\n'):
        msg=[time.strftime('[%H:%M:%S]'),
                 '[WARNING]',
                 *value]
        cprint(*msg, sep=sep, end=end, colour=31)

if __name__=='__main__':
    logger=Logger()
    logger.info('this is some infomation')
    logger.warning('this is a warning')
    logger.error('this is a critical error')
    sys.stderr.write('hi\n')
