from collections import OrderedDict
import argparse
import re

import logger
class ReDef(object):
    def __init__(self, code, language, Logger):
        try:
            with open('stdlib.redef') as stdlib:
                Logger.info('Successfully opened stdlib')
                try:
                    with open(language + '.redef') as llib:
                        Logger.info('Successfully opened language file')
                        code = stdlib.read() + llib.read() + code
                except FileNotFoundError:
                    Logger.error('Language file not found, check language argument')
                    exit(1)
        except FileNotFoundError:
            Logger.error('Stdlib file not found')
            exit(1)
        def_regex = r'def "([^"]*)"\s*:\s*"([^"]*)"'
        cdefs = OrderedDict(re.findall('c' + def_regex, code))
        code = re.sub('c' + def_regex, '', code)
        Logger.info('Found', len(cdefs), 'cdefs')
        redefs = OrderedDict(re.findall(def_regex, code))
        code = re.sub(def_regex, '', code)
        Logger.info('Found', len(redefs), 'redefs')
        self.code = code
        self.logger = Logger
        self.apply_redefs(redefs)
        Logger.info('Applied redefs')
        self.apply_cdefs(cdefs)
        Logger.info('Applied cdefs')
    def apply_redefs(self, redefs):
        code = self.code
        old = ''
        while old != code:
            old = code
            for regex in redefs:
                code = re.sub(regex, redefs[regex], code)
        self.code = code
    def apply_cdefs(self, cdefs):
        regex_master = '|'.join('(?:%s)' % i for i in cdefs)
        comp = []
        for m1 in re.finditer(regex_master, self.code):
            for regex in cdefs:
                for m2 in re.finditer(regex, self.code):
                    if m1.span() == m2.span():
                        self.logger.info(regex, m1.group())
                        comp.append(re.sub(regex, cdefs[regex], m1.group()))
        self.code = ''.join(comp)
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='ReDef code file')
    parser.add_argument('output', help='Output file')
    parser.add_argument('-l', '--language', help='Target language, default is c++',
                        default='c++')
    parser.add_argument('-v', '--verbosity', help='How verbose for output to be, default=2',
                        default=2, type=int)
    args = parser.parse_args()
    Logger = logger.Logger(args.verbosity)
    try:
        with open(args.file) as file:
            Logger.info('Successfully opened', args.file)
            code = file.read()
    except FileNotFoundError:
        Logger.error('No such file:', args.file)
        exit(1)
    redef = ReDef(code, args.language, Logger)
    Logger.info('Successfully generated code')
    with open(args.output, 'w') as file:
        file.write(redef.code)
    
if __name__ == '__main__':
    main()
