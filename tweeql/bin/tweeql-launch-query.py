#!/usr/bin/env python
'''
Script allowing the webserver to launch a tweeql process with a query. 
'''

from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner
import settings, traceback, readline, inspect, signal
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def runECONTAINS(cmd):
    runner = QueryRunner()
    process_command(runner, cmd)

def process_command(runner, cmd):
    try:
        runner.run_query(cmd, False)
    except KeyboardInterrupt:
        runner.stop_query()
        print 'quitting!'
    except TweeQLException, e:
        runner.stop_query()
        if settings.DEBUG:
            traceback.print_exc()
        else:
            print e

if __name__ == '__main__':
    args = sys.argv[1:]
    assert len(args) == 1
    runECONTAINS(args[0])
