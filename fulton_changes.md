status_handlers.py
- DbInsertStatusHandler
  - engine is now a static member of operators.StatusSource.  This is because another class (StreamFromDB) will also access the engine, so it makes sense to store the engine in a central location
- ToStreamStatusHandler
  - takes incoming statuses, and creates a stream with them
  - more precisely, it knows who it is broadcasting to - when a downstream client stream is created that feeds from it, the client registers itself with the parent stream as a listener
  - then when the parent broadcasts, it knows what streams to broadcast to

query_runner.py
- sources can now be streams and databases, so run_built_query now has to choose from among those sources.  currently the parsing is not in final form, so you can't say FROM TABLE FOO or FROM STREAM FOO.  Instead, you have to say FROM STREAMFOO or FROM TABLEFOO.  If the name starts with STREAM that's how it is identified as a STREAM.  Also, there can only be alphanumerics in table/stream names
- in __init__ of QueryRunner, set the database engine in StatusSource.  So might end up doing this more than once in a session but that is ok

query_builder.py
- now 'STREAM' can also be a source, so you could also say INTO STREAM FOO
- _get_handler reflects this, allowing ToStreamStatusHandler to be a possible handler
- batchsize is now 10 if handler is not a DB handler
- _get_source() looks at prefix of source to determine if it is stream or database or twitter

stream_from_stream.py
- StreamFromStream
  - mimics the Stream class, so it has a fetch method that is the equivalent of sample etc.  This class receives its statuses from a stream that is broadcasting.  When the stream decides to broadcast, it calls StreamFromStream.accept_statuses which will then call the StreamFromStream.listener on the newly arrived tuples, provided the StreamFromStream is running
  - the fetch/sample etc methods, if asynchronous, are now implemented as DAEMONS.  this is because we want the keyboard interrupt to kill the main thread, which will then stop all the running queries.  if these query threads were not daemons then keyboard interrupt would not cause the program to exit
  - when the StreamFromStream is initialized, it has to register itself with the parent stream so that the parent knows where to broadcast its statuses
  - likewise, when the StreamFromStream is disconnected, it has to unregister itself with the parent stream
- StreamFromDB
  - another imitation of the Stream class
  - reads from sqlalchemy table. 
  - just like all other streams, the fetcher/sampler runs as daemon

operators.py
- i made StatusSource into the do it all static class that keeps track of what tables and sources are available.