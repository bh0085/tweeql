from tweeql.exceptions import TweeQLException
#from tweeql.query_runner import QueryRunner
import time
from operators import StatusSource
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
    def fetch(self):
        self.running = True
        while self.running:
            time.sleep(0.1)

    # receives list of tweets from its source and calls on_status on them
    def accept_statuses(self, statuses):
        print 'ACCEPT!!!!!!!!!!!!!'
        if self.running:
            for status in statuses:
                self.listener.on_status(status)

    def disconnect(self):
        self.running = False
        self.source.unregister(self)

