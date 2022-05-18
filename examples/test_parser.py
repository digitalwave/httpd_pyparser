#!/usr/bin/env python3

import sys
import os
import yaml
import httpd_pyparser.apache
import httpd_pyparser.nginx
import simplejson

if len(sys.argv) < 3:
    print("Argument missing!")
    print("Use: %s httpdtype nginx.conf" % sys.argv[0])
    print("  where httpdtype is 'apache' or 'nginx'")
    sys.exit(1)

httpdtype = sys.argv[1]
conffile = sys.argv[2]
if len(sys.argv) > 3:
    outputdir = sys.argv[3]
else:
    outputdir = "/".join(conffile.split("/")[:-1])

if httpdtype == 'apache':
    mparser = httpd_pyparser.apache.Parser()
elif httpdtype == 'nginx':
    mparser = httpd_pyparser.nginx.Parser()
else:
    print("Unknown httpd type (%s) - choose 'apache' or 'nginx'" % (httpdtype))
    sys.exit(1)

pdebug = False
if len(sys.argv) > 3:
    if sys.argv[3] == "debug":
        pdebug = True

print("Config: %s" % conffile)

with open(conffile) as file:
   data = file.read()

try:
    mparser.parser.parse(data, debug = pdebug)
except:
    print(sys.exc_info()[1])
    sys.exit(1)

if pdebug == False:
    outfile = conffile.split("/")[-1].replace(".conf", ".yml")
    fp = open(os.path.join(outputdir, outfile), "w")
    yaml.dump(mparser.configlines, fp, default_flow_style=False)
    #print(simplejson.dumps(mparser.configlines, indent=4, sort_keys=True))
    #for c in mparser.configlines:
    #    print(c)
    fp.close()
