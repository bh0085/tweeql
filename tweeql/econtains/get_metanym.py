#!/usr/bin/env python
import sys, os
import tweeql_econtains
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get metanym aliases.')
    parser.add_argument('idstring', metavar='idstring', type=str, nargs=1,
                        help='Idstring of the form "type:key" for which to receive metanym aliases.')
    parsed = parser.parse_args()
    aliases = tweeql_econtains.getAliases(parsed.idstring[0])
    print aliases
    exit(0)
