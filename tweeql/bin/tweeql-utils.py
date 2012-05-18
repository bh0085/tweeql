#!/usr/bin/env python
import sys, os
import tweeql.econtains.tweeql_econtains as tweeql_econtains
import argparse

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get metanym aliases.')
    parser.add_argument('--get-metanym','-g', metavar='id', type=str, nargs=1,
                        dest = 'get_metanym',
                        help='Get metanym aliases for the metanym having idstring of the form "type:key".')
    parser.add_argument('--make-metanym', '-m', metavar='id', type=str,nargs=1,
                        dest= 'make_metanym',
                        help='Generate metanym aliases for the metanym having idstring of the form "type:key".')
    parsed = parser.parse_args()

    if parsed.get_metanym:
        aliases = tweeql_econtains.getAliases(parsed.get_metanym[0])
        print aliases
    if parsed.make_metanym:
        info = tweeql_econtains.setAliasesIfNeeded(parsed.make_metanym[0], reset = True)
        print info

