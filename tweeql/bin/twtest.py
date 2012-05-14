#!/usr/bin/env python

from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner

import settings
import traceback
import readline

def main():
    runner = QueryRunner()
    cmd = "SELECT text FROM twitter_sample WHERE text ECONTAINS 'hey' OR text ECONTAINS 'hello'"
    process_command(runner, cmd)
    

def process_command(runner, cmd):
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
