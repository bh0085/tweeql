#!/usr/bin/env python
import sys, os
import argparse
import tweeql_econtains

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make metanym aliases.')
    parser.add_argument('idstring', metavar='idstring', type=str, nargs=1,
                    help='Idstring of the form "type:key" for which to receive metanym aliases.')
    parser.add_argument('--reset', dest='reset', action='store_const',
                        const=True, default=False,
                        help='Recompute metanym values if already stored.')
    parsed = parser.parse_args()
    info = tweeql_econtains.setAliasesIfNeeded(parsed.idstring[0], reset = parsed.reset)
    print info
    exit(0)
