'''
A collection of scripts and raw lists falling under the categories of:

1. bands
2. people
3. foods

That can be offered as options on the webserer for the 6.830 project 
and may be input to scripts in freebase_utils.

'''

DEVELOPER_KEY = 'AIzaSyDGJapkaTMy09-nS96huqzdX4ftUCTJxwA'


sample_bandnames = [
	'the police',
	'jimi hendrix',
	'mingus', 
	'offspring',
	'the shins'
]
 

bonnaroo_bandnames = ['regeneration - q&a with director philip montgomery and producer matt deross', "[adult swim] presents: things you've never seen", 'afrocubism', 'alabama shakes', 'ali wong', 'alice cooper', 'alo', 'alo: rte interview & performance', 'american splendor - q&a with actor judah friedlander', 'amy schumer', 'andrea bellanger', 'apple butter express', 'art vs. science', 'aziz ansari', 'aziz ansari & rory scovel', 'bad brains', 'bad brains: band in dc', 'battles', 'ben folds five', 'ben howard', 'bethesda', 'bhakti: rte interview & performance', 'bhi bhiman', 'big freedia', 'big gigantic', 'black box revelation', 'black star', 'blind pilot', 'blind pilot: rte interview & performance', 'bluegrass supergroup', 'body language (dj set)', 'bon iver', 'breakdancing', 'brenton duvall', 'brenton duvall', 'brian posehn', 'brian posehn, pete holmes, kyle kinane, & ali wong', 'buster keaton shorts - live score performed by tune-yards and ava mendoza', 'by lightning!', 'caitlin rose', 'cc: stand-up: the bonnaroo experience', 'chad stokes(dispatch), matt wilhelm (calling all crows) rte interview/performance', 'chappo', 'charles bradley and his extraordinaires', 'charles bradley: soul of america - q&a with charles bradley', 'cherub', 'childish gambino', 'chuck mead', 'city and colour', 'clare and the reasons', 'colin hay', "colin hay, garfunkel & oates, mike o'connell", 'cosmic suckerpunch', 'dale earnhardt jr. jr.', 'danny brown', 'danzig legacy - featuring music by danzig, samhain and danzig/doyle performing the misfits', 'danzig legacy \xe2\x80\x93 featuring music by danzig, samhain and danzig/doyle performing the misfits', 'darondo', 'das racist', 'dawes', 'debo band', 'delta spirit', 'dispatch', 'dj equal', 'dj equal / quickie mart', 'dj tablesaw', 'dj xsv', 'dub kartel', 'ema', 'feist', 'finding north - introduction by the civil wars, and lindsay guetschow of participant media', 'fitz & the tantrums', 'flogging molly', 'fly golden eagle', 'flying lotus', 'fort atlantic', 'foster the people', 'fruit bats', 'fun.', 'garfunkel & oates', 'gary clark jr.', 'girl walk // all day', 'glossary', 'god bless america - q&a with director/screenwriter bobcat goldthwait', 'green screens presented by rock the earth: chasing ice - q&a with director jeff orlowski', 'green screens presented by rock the earth: the big fix - introduction by ivan neville of dumpstaphunk; q&a with film producer charles hambleton, and ayn pivonka of gulf restoration network', 'green screens presented by rock the earth: the island president', 'grouplove', 'gza performing "liquid swords" backed by grupo fantasma', 'here we go magic', 'hey rosetta!', 'hey rosetta! rte interview & performance', 'hit and run - q&a with director/screenwriter/actor dax shepard & actor kristen bell', 'honey island swamp band', 'honey island swamp band: rte interview & performance', 'hudost', 'hula hoopers led', "ivan neville's dumpstaphunk", "ivan neville's dumpstaphunk", 'james wallace & the naked light', 'janka nabay & the bubu band', 'janka nabay & the bubu gang', 'janus/criterion present: samurai iii: duel at ganryu island', 'jared dietch', 'jared dietch / quickie mart', 'jared dietch / wyllys', 'jukebox the ghost', 'k-flay', 'k-flay (dj set)', 'kathleen edwards', 'katie herzig', 'katie herzig: rte interview / performance', 'kendrick lamar', 'kenny rogers', 'khaira arby & her band', 'kurt vile & the violators', 'kyle kinane', 'la-33', 'laura marling', "laurel & hardy shorts - live score performed by steven bernstein's mto", 'little dragon', 'lp', 'ludacris', 'mac miller', 'machines are people too', 'major lazer', 'marc maron', 'marc maron, judah friedlander, & amy schumer', 'marc maron, world champion judah friedlander, & amy schumer', 'mariachi el bronx', 'marina orchestra', 'mark foster of foster the people dj set', 'marley', 'matt sucich', 'mawre', 'michael kiwanuka', "mike o'connell", "mike o'connell", 'mimosa', 'mogwai', 'monstro', 'moon taxi', 'nba finals', 'nba finals (if necessary)', 'needtobreathe', 'north mississippi allstars duo', 'oberhofer', 'ogya', 'orgone', 'paladino', 'pedrito martinez group', 'pelican', 'penguin prison (dj set)', 'penguin prison / body language', 'pete holmes', 'phantogram', 'phish', 'pujol', 'punch brothers', 'puscifer', 'quickie mart (dj set)', 'radiohead', 'red baarat', 'red baraat', 'red baraat: rte interview & performance', 'red hot chili peppers', 'reggie watts', 'reggie watts soundcheck', 'rhys darby', 'rhys darby & reggie watts', 'robert ellis', 'robert francis', 'rock the earth', 'rodrigo y gabriela and c.u.b.a', "rollin' in the hay", 'rory scovel', 'rte panel discussion re: nola ivan neville, etc', 'rubblebucket', 'rubblebucket rte interview / performance', 'sam bush', 'sam bush band', 'santigold', 'sara watkins', 'sarah jarosz', 'savages', 'sbtrkt', 'sf sketchfest presents freak dance - q&a with co-director/screenwriter/actor matt besser', 'sf sketchfest presents reggie watts + surprise silent film - live score performed by reggie watts', 'sf sketchfest presents the best of upright citizens brigade comedy hosted by matt besser', 'sf sketchfest presents the doug benson movie interruption: crank: high voltage - doug benson & friends live', 'sf sketchfest presents the doug benson movie interruption: rambo (2008 version) - doug benson & friends live', 'shahidah omar', 'sharon jones and the dap-kings', 'sister sparrow & the dirty birds', 'skrillex', 'soja', 'soja: rte interview / performance', 'spectrum road (cindy blackman santana, jack bruce, john medeski, and vernon reid)', 'st. vincent', 'steven bernstein soundcheck', "steven bernstein's mto plays sly", 'steven wright', 'steven wright & glenn wool', 'strike mto', 'strike reggie watts', 'strike tune-yards', 'superjam', 'tauk', 'temper trap', 'the antlers', 'the avett brothers', 'the beach boys (brian wilson, mike love, al jardine, bruce johnston and david marks)', 'the black lips', 'the carnivalesque cabaret- burlesque, bellydance & sideshow', 'the casey driessen singularity', 'the cave singers', 'the chris gethard show', 'the civil wars', 'the deep dark woods', 'the devil makes three', "the dirty guv'nahs", 'the flavor savers- beard & mustache contest', 'the infamous stringdusters', 'the joy formidable', 'the kooks', 'the lonely forest', 'the main squeeze', 'the roots', 'the shins', 'the silent comedy', 'the soul rebels', 'the staves', 'the temper trap', 'the war on drugs', 'the word (john medeski, robert randolph and north mississippi allstars)', 'the word (john medeski, robert randolph, north mississippi allstars)', "tim and eric's billion dollar movie", 'trampled by turtles', 'trapped in the closet sing-along!', 'trixie whitley', 'tune-yards', 'tune-yards soundcheck', 'two door cinema club', 'umphrey\xe2\x80\x99s mcgee', 'unchained "the mighty van halen tribute"', 'valient thorr', 'war on drugs', 'water knot', 'we are augustines', 'when groucho met alice: duck soup - introduction by alice cooper', 'white denim', 'wild cub', 'world champion judah friedlander', 'wyllys', 'yelawolf', 'young the giant', 'yuna']


#use the billboard top 10 for 2011
billboard_bandnames = ['adele', 'lady gaga', 'michael buble', 'bruno mars', 'rihanna', 'mumford & sons', 'katy perry', 'beyonce']

#or the current billboard top 100
def getBillBoardArtists():
    from pyquery import PyQuery as pq
    '''
    crawl the billboard top 100... 
    I don't know why you'd ever want to do that
    '''
    all_artists = []
    for i in range(10):
        begin = i * 10 + 1
        url = 'http://www.billboard.com/charts/billboard-200#/charts/hot-100?begin={0}&order=position'.format(begin)
        page = pq(url)
        h3 = page.find('#chart-list').children('.chart-item-wrapper').find('.module-middle').children('.chart-item').children('div').filter('.item-artist')
        artistnames = [pq(e).text() for e in h3 ]
        all_artists.extend([a.lower() for a  in  artistnames])
    return all_artists

recent_bandnames = []
def getRecentArtists():
    from apiclient import discovery
    freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
    q = json.dumps([{
                "type":"/music/artist",
                "active_start>=": "2011",
                "name": None,
                "limit":10
                }])
    responses = json.loads(freebase.mqlread(q).execute())
    recent_artists = [a['name'] for a in responses['result']]
    


band_collectionnames = {
    'recent':recent_bandnames,
    'bonnaroo':bonnaroo_bandnames,
    'billboard':billboard_bandnames,
    'sample':sample_bandnames
    }

bandnames = {
}



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



foodnames = [
'pasta',
'meat',
'fish',
'poultry',
'vegetable'
]

