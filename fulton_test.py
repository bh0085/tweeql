from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner
import sys
import time
import threading
import pdb
from tweeql.operators import StatusSource
from tweeql.locks import locks
import logging

# before running a query that sends into a stream, need to specify the name of the into_stream, and create a flag corresponding to it
# if a query reads from a stream, then in build_query need to wait for the flag to be true

class QueryThread(threading.Thread):
    def set_query(self, q, async):
        self.runner = QueryRunner()
        self.q = q
        self.async = async
    def run(self):
        self.runner.run_query(self.q, self.async)
    
def run_query(q, to_stream, from_stream):
    print q, 1, to_stream
    if to_stream != False:
        locks.locks[to_stream] = threading.Event()
    print q, 2, from_stream
    if from_stream != False:
        locks.locks[from_stream].wait()
    print q, 3
    qt = QueryThread()
    qt.set_query(q, False)
    qt.start()
    print q, 4

try:
    query1 = "SELECT text FROM twitter INTO STREAM STREAMONE WHERE text CONTAINS \"game\""
    #query1 = "SELECT text FROM twitter WHERE text CONTAINS \"game\""
    qr1 = QueryRunner()
    qr1.run_query(query1, True)

    query2 = "SELECT text FROM STREAMONE INTO STREAM STREAMTWO WHERE text CONTAINS \"the\""
    qr2 = QueryRunner()
    qr2.run_query(query2, True)
    print 'FINISHED TWOTWOTWOTWOTWO'
    query3 = "SELECT text FROM STREAMTWO"
    print 'RUNNING THRETHRETHREHTEHRHETHERHETHERHETHEHREHR'
    qr3 = QueryRunner()
    qr3.run_query(query3, True)

except KeyboardInterrupt:
    qr1.stop_query()
    qr2.stop_query()
    qr3.stop_query()

"""

to_stream1 = 'ASDF'
from_stream1 = False

#query1 = "SELECT text FROM twitter WHERE text CONTAINS \"the\""
#to_stream1 = 'ASDF'
#from_stream1 = False

query2 = "SELECT text FROM ASDF WHERE text CONTAINS \"them\""
to_stream2 = False
from_stream2 = 'ASDF'

run_query(query1, to_stream1, from_stream1)
run_query(query2, to_stream2, from_stream2)
"""

#QT1 = QueryThread()
#QT1.set_query(query1, False)
#QT1.start()
#print uyr
#print '11111111'
#time.sleep(5)

#print '2222222222'
#locks.lock1.wait()

#print '333333333333'

#print 'EEEEEEEEEEEEEEEE ', StatusSource.get_saved_stream('ASDF')

#QT2 = QueryThread()
#QT2.set_query(query2, False)
#QT2.start()




"""
try:
    #query1 = "SELECT text FROM twitter WHERE text CONTAINS \"the\""
    #runner = QueryRunner()
    #runner.run_query(query1, True)
    while 1:
        print 'ZZZZZZZZZZZZZZ'
        time.sleep(0.1)
except KeyboardInterrupt:  
    
    while 1:
        print 'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG'
        time.sleep(0.1)
else:
    while 1:
        print 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'
        time.sleep(0.1)
    #sys.exit(1)

while 1:
    print 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
    time.sleep(0.1)

#sys.exit(1)
"""
