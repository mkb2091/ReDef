'''Log infomation, warnings and errors'''
import platform
import time
import sys
__isatty__ = sys.stdout.isatty()


def cprint(*value, sep=' ', end='\n', colour=1, bold=True):
    '''
    A functions that works like print, but allows use of colour.
    It uses ANSI escape characters, which mostly aren't supported on windows so,
        it reverts to just printing the plain text. Windows is detected by use
        of platform.system()
    IDLE also doesn't support ANSI, but text printed to stderr is red so if the
        colour is red it prints to stderr instead for IDLE. IDLE is detected by
        checking if the "idlelib" module has been imported.
    '''
    msg = sep.join(map(str, value)) + end
    file = sys.stdout
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
    '''Create a Logger object'''
    def __init__(self, level=0):
        if level < 1:
            self.level = 0
        elif level < 2:
            self.level = 1
        elif level < 3:
            self.level = 2
        else:
            self.level = 3

    def info(self, *value, sep=' ', end='\n'):
        '''Print infomation, does nothing at log levels above 0'''
        if self.level == 0:
            msg = [time.strftime('[%H:%M:%S]'),
                   '[INFO]',
                   *value]
            cprint(*msg, sep=sep, end=end, colour=32)

    def warning(self, *value, sep=' ', end='\n'):
        '''Print warnings, does nothing at log levels above 1'''
        if self.level < 2:
            msg = [time.strftime('[%H:%M:%S]'),
                   '[WARNING]',
                   *value]
            cprint(*msg, sep=sep, end=end, colour=33)

    def error(self, *value, sep=' ', end='\n'):
        '''Print erros, does nothing at log levels above 2'''
        if self.level < 3:
            msg = [time.strftime('[%H:%M:%S]'),
                   '[WARNING]',
                   *value]
            cprint(*msg, sep=sep, end=end, colour=31)
