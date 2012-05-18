#Ben's Changes#

##tweeql/*##

Made a few modifications that added the econtains operator and allowed database update speedup.

`operators.py`: 
	Mostly just added ECONTAINS.

`query_status.py`: 
	No changes besides adding a settings key to allow the database rewrites to occur a bit faster. For sparse results, I see no obvious reason to not allow more frequent commits from sqlalchemy - Adam, am I missing something here?

##tweeql/econtains/*##

Added python scripts to query freebasea and to enable the econtains operator.

`tweeql_econtains.py`: 
	functions called directly by the econtains opertor. SetAliases() and GetAliases().

`freebase_utils.py`: 
	generic wrapper of ECONTAINs plugins to allow write, rewrite and access of econtains (type:key) pairs.

`plugins`: See below.

##tweeql/econtains/plugins/*##

`band.py`: 
	A simple econtains plugin. Takes the name of a band, performs a fuzzy match on freebase band names, finds its group members and then emits a list of "band aliases" consisting of the union of member aliases and band name aliases. If multiple bands are fuzzily matched, it returns the union over all matched bands and members.

`person.py`: 
	Another simple econtains plugin. Can be given either a freebase "mid" uniquely specifying a node of type "people/person" or the name of a freebase "people/person. In either case, returns a list of the aliases for the person. If more than one person is found, it arbitrarily chooses the first one returned.

`bandcollection.py`: 
	Allows the user to select a collection of bands from a preset list of options, bonnaroo, top100, etc. For each member of the list, generates a list f aliases (the same way as `band.py`, above), yields the union of all such lists over the collection.

**note** for "bandcollection" to work, there is a dependency on memo.py, a script that I keep in _github.com/bh0085/everySNAKE_. I should put everySNAKE on pip but its not there yet (and mostly useless); by default I don't include bandcollection in the set of enabled plugins for this reason.  

**TODO**

`movies.py`: 
	A slightly smarter example: how a user might implement a custom type that crawled freebase to find aliases for a movie and participant actors and/or its directors.

##tweeql/bin/*##

`twtest.py`: 
	Sorry, this is just a test. I'll get rid of it.

`tweeql-eavesdrop.py`:
	A script to run to eavesdrop on tweeql streams as they are written to a database table. Synql launches this with Popen() and then reads stdout in JSON format to update tweets. Arguably, this should be implemented via a socket/rpc with the server but this way seems a bit simpler.

Also, this could be built into tweeql but the idea is for it to be an asynchronous process from the tweet streaming itself - the webserver should be able to launch it choosing an output file, kill it, relaunch it etc without messing with an ongoing stream.

`tweeql-utils.py`:

Includes:

1. --make-metanym: Shell script allows the user to create an econtains type/key combination. Calls tweeql_econstains.setAliasesIfNeeded(). Note that operators.ECONTAINS will call this automatically so this script is only around for testing purposes.

2. --get-metanym: Shell script allows the user to check the aliases stored for a metanym (type:key) pair. Returns a list of aliases.


##settings.py##

**EAVESDROPPING_COUNT** Controls batchsize of tweets broadcast to the stdout or a file.

**EAVESDROPPING_DELAY** Repeat delay betwen batch broadcasts.

**ECONTAINS_DATADIR** Directory to save ECONTAINS alias dictionaries to. Must be writable.

**ECONTAINS_TYPE_EXTENSIONS** Allows user provided extensions to ECONTAINS semantics.

**DATABASE_BATCHSIZE** Control size of tweet batches written to the database.

