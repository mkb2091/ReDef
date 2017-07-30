import argparse
import re
class ReDef(object):
    def __init__(self, code, language):
        with open('stdlib.redef') as stdlib:
            with open(language + '.redef') as llib:
                code = stdlib.read() + llib.read() + code
        def_regex = r'def "((?:(?:\\")|[^"])*)"\s*:\s*"((?:(?:\\")|[^"])*)"'
        cdefs = dict(re.findall('c' + def_regex, code))
        code = re.sub('c' + def_regex, '', code)
        redefs = dict(re.findall(def_regex, code))
        code = re.sub(def_regex, '', code)
        self.code = code
        self.apply_redefs(redefs)
        self.apply_cdefs(cdefs)
    def apply_redefs(self, redefs):
        code = self.code
        old = ''
        while old != code:
            old = code
            for regex in sorted(redefs):
                code = re.sub(regex, redefs[regex], code)
        self.code = code
    def apply_cdefs(self, cdefs):
        code = self.code
        compiled = []
        while code:
            found = False
            for regex in sorted(cdefs):
                m = re.match(regex, code)
                if m and not found:
                    compiled.append(re.sub(regex, cdefs[regex], m.group()))
                    code=code[m.end():]
                    found = True
            if not found:
                compiled.append(code[0])
                code = code[1:]
        self.code = ''.join(compiled)
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='ReDef code file')
    parser.add_argument('-l', '--language', help='Target language, default is c++',
                        default='c++')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()
    with open(args.file) as file:
        code = file.read()
    redef = ReDef(code, args.language)
    with open(args.output, 'w') as file:
        file.write(redef.code)
    
if __name__ == '__main__':
    main()
