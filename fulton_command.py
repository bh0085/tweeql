#!/usr/bin/env python

from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner

import settings
import traceback
import readline

def main():

    try:
        while True:
            cmd = raw_input("tweeql> ");
            process_command(cmd)
    except KeyboardInterrupt:
        print '\nGoodbye!'

def process_command(cmd):
    runner = QueryRunner()
    try:
        runner.run_query(cmd, False)
    except KeyboardInterrupt:
        runner.stop_query()
    except TweeQLException, e:
        runner.stop_query()
        if settings.DEBUG:
            traceback.print_exc()
        else:
            print e

if __name__ == '__main__':
    main()
