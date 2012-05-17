from apiclient import discovery
from apiclient import model
import json

from freebase_lists import peoplenicks as people_aliases, bandnames as bands

DEVELOPER_KEY = 'AIzaSyDGJapkaTMy09-nS96huqzdX4ftUCTJxwA'

#model.JsonModel.alt_param = ""
#freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
#q_planets  = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]
#
#
#query = [{"type":"/music/artist","name":"The Police","album":[]}]
#
#
#response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
#for planet in response['result']:
#	print planet


def test_people():
	freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
	for pa in people_aliases:
		q = [{
				"type": "/people/person",
				"id":  None,
				"name":None,
				"a:/common/topic/alias": [{
						"value": "{0}".format(pa)
						}],
				"b:/common/topic/alias": [{
						"value":None
						}]
				}]
		#q = json.dumps(q).format(pa)

		responses = json.loads(freebase.mqlread(query=json.dumps(q)).execute())
		aliases = [ e['value'] for r in responses['result'] for e in r["b:/common/topic/alias"]]
		print u'''{0}:\n {1}\n\n'''.format(pa, ', '.join(aliases))

def test_band():
	freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
	for pa in bands:
		q =[{
				"name~=": "{0}".format(pa),
				"type": "/music/musical_group",
				"name": None,
				"/music/musical_group/member" : [{ "member" : None }]
				}]
		#q = json.dumps(q).format(pa)

		responses = json.loads(freebase.mqlread(query=json.dumps(q)).execute())
		aliases = [ e['member'] for r in responses['result'] for e in r["/music/musical_group/member"]]
		print u'''{0}:\n {1}\n\n'''.format(pa, ', '.join(aliases))	
