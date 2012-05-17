'''
Functions that use freebase to generate the lists of synonyms that will
be fed into tweeql's ECONTAINS. Also intended to serve as a general purpose 
tool that the webserver can query to summarize the kind of queries that
will be run or given selections.
'''

from apiclient import discovery
from apiclient import model
import json

#note that we may never use band_collectionames
from freebase_lists import bandnames, band_collectionnames, peoplenicks, foodnames
from everySNAKE.utils import memo as mem

DEVELOPER_KEY = 'AIzaSyDGJapkaTMy09-nS96huqzdX4ftUCTJxwA'


def fetch_type(typename, **kwargs):
    if typename == 'band':
        return getBandAliases(**mem.rc(kwargs))
    elif typename == 'person':
        return getPersonNicks(**mem.rc(kwargs))
    elif typename == 'food':
        raise Exception("Type food is meant to be implemented but not done yet")
    else: raise Exception('type {0} not yet implemented'.format(typename))

def allowedBandCollectionNames():
    return band_collectionnames.keys()

def getBandCollectionAliases(**kwargs):
    def setBandCollectionAliases(**kwargs):
        all_aliases = []
	freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
        names_key = kwargs.get('list', 'sample')
        names_list = band_collectionnames[names_key]
        for n in names_list:
            q = [{
                    "name~=":"{0}".format(n),
                    "type":  "/music/musical_group",

                    "/common/topic/alias": [{
                            "value": None
                            }],
                    "/music/musical_group/member": [{
                            "member": {
                                "/common/topic/alias": [{
                                        "value": None
                                        }]
                                }
                            }],
                    }]
            responses = json.loads(freebase.mqlread(query=json.dumps(q)).execute())
            for band in responses['result']:
                member_aliases = [ a['value']  for e in band["/music/musical_group/member"] for a in e['member']["/common/topic/alias"]]
                band_aliases = [a['value'] for a in band["/common/topic/alias"] ]
                all_aliases.extend(member_aliases)
                all_aliases.extend(band_aliases)

        return all_aliases

        
    name = 'demo{0}'.format(kwargs.get('list',''))
    return mem.getOrSet(setBandCollectionAliases, **mem.rc(kwargs,
                                                           name = name))
def getBandAliases(**kwargs):
    name = kwargs.get('name')
    all_aliases = []
    freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)

    q = [{
                    "name~=":"{0}".format(name),
                    "type":  "/music/musical_group",

                    "/common/topic/alias": [{
                            "value": None
                            }],
                    "/music/musical_group/member": [{
                            "member": {
                                "/common/topic/alias": [{
                                        "value": None
                                        }]
                                }
                            }],
                    }]
    responses = json.loads(freebase.mqlread(query=json.dumps(q)).execute())
    for band in responses['result']:
        member_aliases = [ a['value']  for e in band["/music/musical_group/member"] for a in e['member']["/common/topic/alias"]]
        band_aliases = [a['value'] for a in band["/common/topic/alias"] ]
        all_aliases.extend(member_aliases)
        all_aliases.extend(band_aliases)
    return all_aliases

def getPersonNicks(**kwargs):
    freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)

    mid = kwargs.get('mid')
    q = {
        "type":     "/common/topic",
        "ns0:type": "/people/person",
        "alias": [{
                "value": None
                }],
        "mid":  mid
        }
    responses = json.loads(freebase.mqlread(query=json.dumps(q)).execute())
    aliases =[a['value'] for  a in  responses['result']['alias']]
    return aliases

