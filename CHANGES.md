#Ben's Changes#

##tweeql/*##

Made a few modifications that added the econtains operator and allowed database update speedup.

*operators.py*: Mostly just added ECONTAINS.
*query_status.py*: No changes besides adding a settings key to allow the database rewrites to occur a bit faster. For sparse results, I see no obvious reason to not allow more frequent commits from sqlalchemy - Adam, am I missing something here?

##tweeql/econtains/*##

Added python scripts to query freebasea and to enable the econtains operator.

*freebase_lists.py*
*freebase_utils.py*

##tweeql/econtains/plugin_examples/*##

*foods.py* An example of how a user might choose to implement a custom type for econtains from a simple dict of values.
*movies.py* A slightly smarter example: how a user might implement a custom type that crawled freebase to find aliases for a movie and participant actors and/or its directors.

##tweeql/bin/*##

*twtest.py*: Sorry, this is just a test. I'll get rid of it.
*tweeql-eavesdrop.py*: A script to run to eavesdrop on tweeql streams as they are written to a database table. Synql launches this with Popen() and then reads stdout in JSON format to update tweets. Arguably, this should be implemented via a socket/rpc with the server but this way seems a bit simpler.



