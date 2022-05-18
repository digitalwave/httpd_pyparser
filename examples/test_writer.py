#!/usr/bin/env python3

import sys
import os, os.path
import yaml
import json

import httpd_pyparser.apache
import httpd_pyparser.nginx

if len(sys.argv) < 3:
    print("Argument missing!")
    print("Use: %s HTTPDTYPE /path/to/parsed_struct.file" % (sys.argv[0]))
    sys.exit(-1)

httpdtype = sys.argv[1]
srcobj = sys.argv[2]

print("Parsing CRS structure: %s" % srcobj)

dname = srcobj.replace(".yml", "_out.conf")

try:
    with open(srcobj) as file:
        if yaml.__version__ >= "5.1":
            data = yaml.load(file, Loader=yaml.FullLoader)
        else:
            data = yaml.load(file)
except:
    print("Exception catched - ", sys.exc_info())
    sys.exit(-1)

try:
    if httpdtype == 'apache':
        mwriter = httpd_pyparser.apache.Writer(data, "        ")
    elif httpdtype == 'nginx':
        mwriter = httpd_pyparser.nginx.Writer(data, "        ")
    else:
        print("Unknown httpd type - choose 'apache' or 'nginx'")
        sys.exit(1)
except:
    print(sys.exc_info()[1])
    sys.exit(1)

if True:
    with open(dname, "w") as file:
        mwriter.generate()
        # add extra new line at the end of file
        mwriter.output.append("")
        file.write("\n".join(mwriter.output))
#except:
#    print("Exception catched - ", sys.exc_info())
#    sys.exit(1)
