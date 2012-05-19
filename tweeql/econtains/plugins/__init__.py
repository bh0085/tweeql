from person import getPersonNicks
from band import getBandAliases

#not included because I don't package "memo.py" from everySNAKE. Feel free to enable.
#from bandcollection import getBandCollectionAliases, allowedBandCollectionNames

plugins_enabled = {
    'person':{'getter':getPersonNicks,'allowed':None},
    'band':{'getter':getBandAliases,'allowed':None},
    #'bandcollection':{'getter':getBandCollectionAliases,'allowed':allowedBandCollectionNames}
    }
