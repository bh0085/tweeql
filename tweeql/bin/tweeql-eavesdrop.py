#!/usr/bin/env python
'''
Asynchronous eavesdropping on a database generated by Tweeql.

This script is written to allow an app such as synql to simply fetch blocks of tweets from the database located at settings.DATABASE_URI without messing around with sqlalchemy. Called from the command line, it dumps the ${EAVESDROPPING_COUNT} most recent tweets to STDOUT or to a file specified in json format.

For command line usage, call:
  tweeql-eavesdrop.py --help.
'''

import argparse, json, time
import sqlsoup
from sqlalchemy import Table
from sqlalchemy.exc import NoSuchTableError

from tweeql.settings_loader import get_settings
settings = get_settings()

#load relevant settings
eavesdrop_broadcast_count = settings.EAVESDROPPING_COUNT if settings.__dict__.has_key('EAVESDROPPING_COUNT') else 100
eavesdrop_broadcast_delay = settings.EAVESDROPPING_DELAY if settings.__dict__.has_key('EAVESDROPPING_DELAY') else 1
dburi =  settings.DATABASE_URI

def eavesdrop(table = None, output = None, recurs = False):
    '''
    Dump tweets in "table" to STDOUT of "file"
    '''

#    print dir(db)
#    return

    while 1:
       try:
           db = sqlsoup.SQLSoup(dburi)
           if table == None:
               last_created = (-1, None)
           #fix an apparent SQLSoup bug - sqlite_master lacks a primary key :(
               sqm_table = Table("sqlite_master", db._metadata, autoload=True)
           #read sqlite_master with tablename as the primary
               for record in db.map(sqm_table, primary_key=[sqm_table.c.name]).all():
                   if record.rootpage > last_created[0] and record.type == 'table':
                       last_created = (record.rootpage, record.name)  
               if last_created[1] == None: raise NoSuchTableError()
               eavesdrop_table = db.entity(last_created[1])
           else:
               eavesdrop_table = db.entity(table)
       
           break
       except NoSuchTableError, e:
           print 'waiting for table to be initialized'
           print table
           print e
           time.sleep(1)
    
        
    while 1:
        content = json.dumps([
                dict([(k,row.__getattribute__(k)) 
                      for k in row.c.keys()])
                for row in eavesdrop_table.all()[-eavesdrop_broadcast_count:]])
        if output == None:
            print content
        else:
            with open(output, 'w') as f: f.write(content)
        if not recurs: break
        else: time.sleep(eavesdrop_broadcast_delay)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Eavesdrop on a twitter stream, broadcasting JSON formatted results to the stdout.')
    parser.add_argument('-t','--table', dest='tablename', type=str, nargs='?',
                       help =  'Eavesdrop on a specific tablename fed from a stream. Defaults to the most recently created table.')
    parser.add_argument('-o','--output', dest='outfile', type=str, nargs='?',
                        help = 'Update a file with eavesdropped content. Defaults to stdout.')
    parser.add_argument('-r','--recurring', dest='recurring', action='store_const',
                        default = False, const = True,
                        help = 'Create a recurring eavesdropper - will keep reading until terminated')
    parsed = parser.parse_args()


    eavesdrop(table = parsed.tablename, output = parsed.outfile, recurs = parsed.recurring)
