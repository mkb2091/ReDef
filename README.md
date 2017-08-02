# ReDef
**ReDef** is programming language. It is compiled into c++ at the moment, but hopefully it will support more languages in the future.
## Syntax
**ReDef** has two basic commands **cdef** and **def**, both use regular expressions and are written as **command** "regex1":"regex2". e.g. def "i":"input()", regex1 is replaced by regex2 using regular expression substitution in python3
### def
All **def**s are applied first. They are used for optimizations and shortcuts. They are applied until the code is the same after applying all of them, so if used wrong, they could cause problems. e.g. def "":"a" would replace the blank character between every character in the code with a turning "1+1" into "a1a+a1a" and then turn that into "aaa1aaa+aaa1aaa" and so on.
### cdef
These are used for controlling the generated code.They are together, sequencially through the code once. Strings which don't match any of the **cdef**s are ignored. For example 
cdef "p":"print();"
cdef "parse":"parser();"
parse

would generate print(); whereas 
cdef "parse":"parser();"
cdef "p":"print();"
parse
would generate parse();
## Hello World
