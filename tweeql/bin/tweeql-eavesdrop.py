#!/usr/bin/env python
import argparse
from tweeql.settings_loader import get_settings
settings = get_settings()

#load relevant settings
eavesdrop_frequency = settings.EAVESDROPPING_RATE if settings.__dict__.has_key('EAVESDROPPING_RATE') else 1
eavesdrop_broadcast_count = settings.EAVESDROPPING_COUNT if settings.__dict__.has_key('EAVESDROPPING_COUNT') else 100
dburi =  settings.DATABASE_URI

def eavesdrop(table = None):
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Eavesdrop on a twitter stream, broadcasting JSON formatted results to the stdout.')
    parser.add_argument('-t', '--table', dest=tablename, type=str, nargs=1,
                        'Eavesdrop on a specific tablename fed from a stream. Defaults to the most recently --created-- table.')
    parsed = parsed.parse_args()

    eavesdrop(table = parser['tablename'])
