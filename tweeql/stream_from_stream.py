from tweeql.exceptions import TweeQLException
#from tweeql.query_runner import QueryRunner
import time
from operators import StatusSource
from status_handlers import DbInsertStatusHandler
from tweepy.models import Status
from sqlalchemy.sql import select
from sqlalchemy import Table, MetaData
from sqlalchemy.engine import reflection
import pdb
from threading import Thread
import logging

'''
note that the input determines what kind of stream query_runner has.  the only function that query_runner calls from its stream is filter/sample/iterate/disconnect.  therefore, i will make a new stream class that implements a 'retrieve' method.
__init__ will take in a reference to the source stream, and register itself with the source stream's status handler.  stream will keep track of whether it is running or not.  once the stream is registered in the source stream's status handler, whenever the status handler is called, it will, for each of its client query_runners's streams, call client_query_runner.add_tweets(status_handler_tweets).  If the stream is running, then it will accept those tweets.  Meanwhile, the stream has a start method that is just running an infinite loop.
'''

class StreamFromStream:
    
    # source is the name of the source
    def __init__(self, listener, source):
        self.listener = listener
        self.source = source
        self.source_handler = StatusSource.get_saved_stream(source)
        self.source_handler.register(self)
        self.running = False

    # allows the stream to start accepting tweets from its source
    # give the option of async even though it doesn't make any sense for 
    def fetch(self, async=False):
        if async:
            t = Thread(target = self._fetch)
            t.daemon = True
            t.start()
        else:
            self._fetch()

    def _fetch(self):
        self.running = True
        while self.running:
            time.sleep(0.1)

    # receives list of tweets from its source and calls on_status on them
    def accept_statuses(self, statuses):
        if self.running:
            for status in statuses:
                self.listener.on_status(status)

    def disconnect(self):
        self.running = False
        StatusSource.get_saved_stream(self.source).unregister(self)

# this stream object needs to read all tuples from a data, convert them to status objects, and run on_status on each of them
class StreamFromDB:

    def __init__(self, listener, table_name):

        self.listener = listener
        self.table_name = table_name

        if not StatusSource.table_exists(table_name):
            raise DbException('table does not exist')
        
#        if StreamFromDB.engine == None:
#            StreamFromDB.engine = DbInsertStatusHandler.engine


        
        
    # read all rows, convert to status, call self.listener.on_status() on them
    def read_from_table(self, async=False):
        if async:
            t = Thread(target = self._read_from_table())
            t.daemon = True
            t.start()
        else:
            self._read_from_table()

    def _read_from_table(self):
        self.running = True
        conn = StatusSource.engine.connect()
        meta = MetaData()
        table = Table(self.table_name, meta, autoload=True, autoload_with=StatusSource.engine)
        cmd = select([table])
        results = conn.execute(cmd)
        for result in results:
            status = Status.parse(None, result)
            self.listener.on_status(status)
            if self.running == False:
                break
    
    # disconnect.  doesn't do much besides stop read_from_table from running
    def disconnect(self):
        self.running = False
        
