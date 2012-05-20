#!/usr/bin/env python

from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner

import settings
import traceback
import readline
import time


def run_cmds_async(cmds):
    runners = [QueryRunner() for i in range(len(cmds))]
    i = 0
    try:
        for cmd in cmds:
            runners[i].run_query(cmd, True)
            i = i + 1
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        for runner in runners:
            runner.stop_query()

def main():
    
    cmds = []
    try:
        while True:
            cmd = raw_input("tweeql> ")
            cmds.append(cmd)
    except KeyboardInterrupt:
        print 'now processing commands'
        run_cmds_async(cmds)
    
    """
    cmds = []
    cmds.append("SELECT text, lang FROM twitter INTO STREAM STREAMGAME WHERE text CONTAINS \'game\'")
    cmds.append("SELECT text, lang FROM STREAMGAME INTO TABLE TABLELAKERS WHERE text CONTAINS \'lakers\'")
    cmds.append("SELECT text, lang FROM STREAMGAME INTO TABLE TABLETHUNDER")
    run_cmds_async(cmds)
    """

if __name__ == '__main__':
    main()
