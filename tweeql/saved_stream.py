from tweeql.operators import StatusSource

class SavedStream():

    def __init__(self, listener, dump_name):
        self.listener = listener
        self.status_dump = StatusSource.get_saved_stream(dump_name)

    def iterate(self):
        for status in self.status_dump:
            self.listener.on_status(status)

    def disconnect(self):
        print 'disconnecting'
