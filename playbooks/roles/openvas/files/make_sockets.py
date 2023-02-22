#!/usr/local/bin/python

import socket as s
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-s', nargs='+')
parser.add_argument('-d')
args = parser.parse_args()
sockets = args.s
dir = args.d
try:
    os.mkdir(dir)
except FileExistsError:
    print("Directory already exists, skipping...")
finally:
    for addr in sockets:
        sock = s.socket(s.AF_UNIX)
        sock.bind(dir + "/" + addr)
