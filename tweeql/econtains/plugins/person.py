'''
Demonstrates a freebase type having a freebase crawler with 
a bit of flexibility in its arguments: 

to find nicknames for a person, the user may provide a name 
(in which case we'll search for the first match on that name) 
or an explicit mid.
'''


from apiclient import discovery
from apiclient import model
from everySNAKE.utils import memo as mem
DEVELOPER_KEY = 'AIzaSyDGJapkaTMy09-nS96huqzdX4ftUCTJxwA'

def getPersonNicks(mid = None, name = None, **kwargs):
    #load the api.
    freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)

    #if freebase "mid" is given, use that.
    if mid != None:
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
    #otherwise, use name.
    elif name != None:
        q = [{
            "type":     "/common/topic",
            "ns0:type": "/people/person",
            "alias": [{
                    "value": None
                    }],
            "name": name
            }]
        responses = json.loads(freebase.mqlread(query=json.dumps(q)).execute())
        aliases =[a['value'] for  a in  responses['result'][0]['alias']]
    #if no information is provided, cough up an exception.
    else:
        raise Exception('not enough information provided!')

    #return a list of strings.
    return aliases


#extra stuff - I don't think its used.
sample_peoplenicks = [
    'barack', 
    'potus',
    'the king',
    'elvis', 
    'sting', 
    'sean combs',
    'puff daddy',
    'weird al', 
    'yankovic'
 ]

politics_peoplenicks = [
        "al gore",
        "obama",
        "dubya",
        "romney",
        "hillary clinton",
        "bill clinton",
        "limbaugh"
]


peoplenicks = {
    'politics': politics_peoplenicks,
    'sample':sample_peoplenicks
    }

