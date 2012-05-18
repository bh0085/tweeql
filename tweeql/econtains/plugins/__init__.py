from person import getPersonNicks
from band import getBandAliases
from bandcollection import getBandCollectionAliases, allowedBandCollectionNames

plugins_enabled = {
    'person':{getter:getPersonNicks,'allowed':None}
    'band':{'getter':getBandAliases,'allowed':None}
    'bandcollection':{'getter':getBandCollectionAliases,'allowed':allowedBandCollectionNames}
