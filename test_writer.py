#!/usr/bin/env python3

import sys
import os, os.path
import yaml
import json
import argparse

import httpd_pyparser.apache
import httpd_pyparser.nginx

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A HTTPD config writer example")
    parser.add_argument("-t", "--httpdtype", dest="httpdtype", metavar='Type of HTTPD', type=str,
                            help='Type of HTTPD, could be apache or nginx', required=True)
    parser.add_argument("-c", "--config", dest="config", metavar='/path/to/config.conf', type=str,
                            help="Path to config file", required=True)
    parser.add_argument("-o", "--outputdir", dest="outputdir", metavar='/path/to/outputdir', type=str,
                            help="Output directory, if it's empty, stdout will be used", required=False)
    parser.add_argument("-f", "--format", dest="format", type=str,
                            help="Input format, could be json or yaml - default is autodetect", required=False)
    args = parser.parse_args()

    httpdtype = args.httpdtype
    srcobj = args.config
    if args.outputdir is not None:
        outputdir = args.outputdir
    else:
        outputdir = os.path.dirname(os.path.realpath(__file__))
    format = args.format

    print("Parsing CRS structure: %s" % srcobj)

    if srcobj.endswith(".yaml") or srcobj.endswith(".yml") or (format is not None and format == "yaml"):
        try:
            with open(srcobj) as file:
                if yaml.__version__ >= "5.1":
                    data = yaml.load(file, Loader=yaml.FullLoader)
                else:
                    data = yaml.load(file)
        except:
            print("Exception catched - ", sys.exc_info())
            sys.exit(-1)

    if srcobj.endswith(".json") or (format is not None and format == "json"):
        try:
            with open(srcobj) as file:
                data = json.load(file)
        except:
            print("Exception catched - ", sys.exc_info())
            sys.exit(-1)

    dname = ".".join(os.path.basename(srcobj).split(".")[:-1]) + ".conf"

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

    try:
        with open(os.path.join(outputdir, dname), "w") as file:
            mwriter.generate()
            # add extra new line at the end of file
            mwriter.output.append("")
            file.write("\n".join(mwriter.output))
    except:
        print("Exception catched - ", sys.exc_info())
        sys.exit(1)
