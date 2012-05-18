'''
Functions that use freebase to generate the lists of synonyms that will
be fed into tweeql's ECONTAINS. Also intended to serve as a general purpose 
tool that the webserver can query to summarize the kind of queries that
will be run or given selections.
'''

import json

#note that we may never use band_collectionames
from everySNAKE.utils import memo as mem

DEVELOPER_KEY = 'AIzaSyDGJapkaTMy09-nS96huqzdX4ftUCTJxwA'

#scan plugins
import plugins
reload(plugins)
type_function_mapper = {}
type_function_mapper.update(plugins.plugins_enabled)


def fetch_type(typename, **kwargs):
    assert typename in type_function_mapper.keys()
    return type_function_mapper[typename]['getter'](**mem.rc(kwargs))
