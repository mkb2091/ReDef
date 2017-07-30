import argparse
import re
class ReDef(object):
    def __init__(self, code, language):
        with open('stdlib.redef') as file:
                stdlib = file.read()
        with open(language + '.redef') as file:
            clib = file.read()
        #clib can overwrite stdlib and code can overwrite both
        code = stdlib + clib + code
        cdef = dict(re.findall(r'cdef "((?:(?:\\")|[^"])*)":"((?:(?:\\")|[^"])*)"', code))
        code = re.sub(r'cdef "((?:(?:\\")|[^"])+)":"((?:(?:\\")|[^"])*)"', '', code)
        redefs = dict(re.findall(r'def "((?:(?:\\")|[^"])*)":"((?:(?:\\")|[^"])*)"', code))
        code = re.sub(r'def "((?:(?:\\")|[^"])+)":"((?:(?:\\")|[^"])*)"', '', code)
        self.code = code
        self.apply_redefs(redefs)
        self.apply_cdefs(cdefs)
    def apply_redefs(self, redefs):
        code = self.code
        old = ''
        while old != code:
            old = code
            for regex in redefs:
                code = re.sub(regex, redefs[regex], code)
        self.code = code
    def apply_cdef(self, cdefs):
        code = self.code
        pos = 0
        while pos <= len(self.code):
            break
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='ReDef code file')
    parser.add_argument('-l', '--language', help='Target language, default is c++',
                        default='c++')
    args = parser.parse_args()
    with open(args.file) as file:
        code = file.read()
    ReDef(code, args.language)
    
if __name__ == '__main__':
    main()
