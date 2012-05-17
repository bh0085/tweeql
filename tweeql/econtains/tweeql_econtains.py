import freebase_utils as fbu
import os, pickle
from tweeql.settings_loader import get_settings
settings = get_settings()
econtains_data_root = settings.ECONTAINS_DATADIR if settings.__dict__.has_key('ECONTAINS_DATADIR') else '/data/econtains'
def setAliasesIfNeeded(idstring, data = {}, reset = False):    

    #parse idstring
    type, key = idstring.split(':')[0], ':'.join(idstring.split(':')[1:])
    assert type in ['food', 'band', 'bandcollection', 'person']

    #load the file in which to store information for the type of idstring
    path = os.path.join(econtains_data_root,
                        '{0}.pickle'.format(type))
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    if os.path.isfile(path):
        content = pickle.load(open(path))
    else: 
        content = {}
    
    #use freebase to gather info for idstring only if needed.a
    if (not reset) and content.has_key(key):
        return {'count':len(content[key]),
                'written': False,
                'aliases':content[key]}
    else:
        data.update(dict(name =  key))
        aliases = fbu.fetch_type(type, **data)
        content[key] = aliases
        pickle.dump(content, open(path,'w'))
        return {'count':len(aliases),
                'written':True,
                'aliases':content[key]}

def getAliases(idstring):
    #get aliases stored for idstring
    type, key = idstring.split(':')[0], ':'.join(idstring.split(':')[1:])
    assert type in ['food', 'band', 'bandcollection', 'person']
    path = os.path.join(econtains_data_root,
                        '{0}.pickle'.format(type))
    assert(os.path.isfile(path))
    content = pickle.load(open(path))
    return content[key]


