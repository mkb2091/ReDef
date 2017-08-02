# ReDef
**ReDef** is stack-oriented programming language. It aims to never crash and always generate valid code. It is compiled into c++ at the moment, but hopefully it will support more languages in the future.
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
### Example programs
5 2 + p

Pushes 5 and 2, then adds them then prints top value of stack

'H'e'l'l'o' 'W'o'r'l'd'!+++++++++++p

Output >>> Hello World

Pushes indvidual chars of "Hello World!", adds them all together and then prints.

'H'e'l'l'o' 'W'o'r'l'd'!+++++++++++i:=1=:1+=:1*p

Input >>> 2

Output >>> Hello World!2Hello World!2

Pushes indvidual chars of "Hello World!", adds them all together, pushes input, stores input in a variable called 1, loads variable 1, adds it to the string, loads variable 1, multiplies, then prints.

i2/p

Input >>> 3

Output >>> 1.5

Pushes input, pushes 2, divide, print.
## How to run a ReDef program
### Requirements
This requires python 3 to run ReDef.py and g++-7 to compile the output c++ file
### Commands
git clone https://github.com/RaspPiTor/ReDef/

cd ReDef

python3 ReDef.py /path/to/code out.cpp

g++-7 out.cpp

./a.out
