#!/usr/bin/env python

import os
import sys
import json
import argparse
import glob

def main():

    parser = argparse.ArgumentParser( description='Dump JSON file' )
    parser.add_argument(
        '-i',
        '--input_file',
        dest='input_file',
        default=None,
        required=True,
        help='Source directory for json files (mandatory)'
    )

    args = parser.parse_args()
    input_file = args.input_file

    with open(input_file,'r') as fp:
        json_data = json.load(fp)
        fp.close()

    print json.dumps(json_data, sort_keys = True, indent = 4)


if __name__ == "__main__":
    main()
