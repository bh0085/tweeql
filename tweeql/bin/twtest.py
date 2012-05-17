#!/usr/bin/env python
from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner

import settings
import traceback
import readline

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def main():

    args = sys.argv[1:]
    runner = QueryRunner()
    cmd = "SELECT text FROM twitter WHERE text ECONTAINS 'person:Barack Obama';"
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
