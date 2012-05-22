
from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner
import sys
import time
import threading
import pdb
from tweeql.operators import StatusSource
from tweeql.locks import locks

commands = []
qrunners = []

while True:
    try:
        cmd = raw_input("tweeql> ")
        commands.append(cmd)
        qrunners.append(QueryRunner())
    except KeyboardInterrupt:
        break

for i in range(len(commands)):
    qrunners[i].run_query(commands[i], False)

    
