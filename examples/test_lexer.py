#!/usr/bin/python3

import sys
import httpd_pyparser.apache
import httpd_pyparser.nginx

if len(sys.argv) < 3:
    print("Argument missing!")
    print("%s HTTPDTYPE /path/to/config for tokenize the config!" % sys.argv[0])
    sys.exit(1)

httptype = sys.argv[1]
conffile = sys.argv[2]
debug = False

if len(sys.argv) > 3 and sys.argv[3] == "debug":
    debug = True

with open(conffile) as file:
   data = file.read()

if httptype == 'apache':
    mlexer = httpd_pyparser.apache.Lexer(debug = debug)
elif httptype == 'nginx':
    mlexer = httpd_pyparser.nginx.Lexer(debug = debug)
else:
    print("Unknown httpd type - choose 'apache' or 'nginx'")
    sys.exit(1)

mlexer.lexer.input(data)

while True:
    try:
        tok = mlexer.lexer.token()
        if not tok: 
            break
        print(tok, mlexer.lexer.lexstate, mlexer.lexer.lineno)
        if debug == True:
            print(mlexer.lexer.lexstate, mlexer.lexer.lexstatestack)
            print("==")
    except:
        print(sys.exc_info()[1])
        sys.exit(1)
