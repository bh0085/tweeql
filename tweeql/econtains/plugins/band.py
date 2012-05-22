'''
Demonstrates a type having a very simple freebase caller.

Takes "name". Searches freebase, returns a list of all aliases
for all bands matching "name".
'''

from apiclient import discovery
from apiclient import model
#from everySNAKE.utils import memo as mem
DEVELOPER_KEY = 'AIzaSyDGJapkaTMy09-nS96huqzdX4ftUCTJxwA'
import json
def getBandAliases(name):
#    name = kwargs.get('name')
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

