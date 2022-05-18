#!/usr/bin/env python3

import sys
import os
import yaml
import httpd_pyparser.apache
import httpd_pyparser.nginx
import simplejson
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Komplex tétel XLS betöltés")
    parser.add_argument("-t", "--httpdtype", dest="httpdtype", metavar='Type of HTTPD', type=str,
                            help='Type of HTTPD, could be apache or nginx', required=True)
    parser.add_argument("-c", "--config", dest="config", metavar='/path/to/config.conf', type=str,
                            help="Path to config file", required=True)
    parser.add_argument("-o", "--outputdir", dest="outputdir", metavar='/path/to/outputdir', type=str,
                            help="Output directory, if it's empty, stdout will be used", required=False)
    parser.add_argument("-d", "--debug", dest="debug",
                            help="Debug", required=False, action='store_true')
    parser.add_argument("-f", "--format", dest="format", type=str,
                            help="Output format, could be json (default) or yaml", required=False)
    args = parser.parse_args()

    httpdtype = args.httpdtype
    conffile = args.config
    outputdir = args.outputdir
    pdebug = args.debug
    if args.format is not None:
        if args.format == "yaml":
            format = "yaml"
        elif args.format == "json":
            format = "json"
        else:
            print("Unknown format, use json or yaml")
            sys.exit(1)
    else:
        format = "json"

    #if outputdir is None:
    #    outputdir = os.path.dirname(os.path.realpath(__file__))

    if httpdtype == 'apache':
        mparser = httpd_pyparser.apache.Parser()
    elif httpdtype == 'nginx':
        mparser = httpd_pyparser.nginx.Parser()
    else:
        print("Unknown httpd type (%s) - choose 'apache' or 'nginx'" % (httpdtype))
        sys.exit(1)

    if format is None:
        format = 'json'

    print("Config: %s" % conffile)

    with open(conffile) as file:
        data = file.read()

    try:
        mparser.parser.parse(data, debug = pdebug)
    except:
        print(sys.exc_info()[1])
        sys.exit(1)


    if format == 'json':
        if outputdir is None:
            print(simplejson.dumps(mparser.configlines, indent=4, sort_keys=True))
        else:
            outfile = conffile.split("/")[-1].replace(".conf", ".json")
            with open(outputdir + "/" + outfile, "w") as file:
                file.write(simplejson.dumps(mparser.configlines, indent=4, sort_keys=True))
    elif format == 'yaml':
        if outputdir is None:
            print(yaml.dump(mparser.configlines, default_flow_style=False))
        else:
            outfile = conffile.split("/")[-1].replace(".conf", ".yaml")
            with open(outputdir + "/" + outfile, "w") as file:
                file.write(yaml.dump(mparser.configlines, default_flow_style=False))

