'''
goes from *any* type to a set of words. 
steps for input x:
1. use query, list=search, srsearch=x, srnamespace=(Main) to get a list of possible titles for pages
2. for the top page _title, retrieve the wikipedia links on the page using query, prop=links, plnamespace=(Main), titles=_title
3. for every link, generate a list of words to search frequency of.  after searching, combine the set of frequencies obtained for a link to obtain a score for the link
4. for the highest scoring k links, return for each link a list of the words that should be added
'''

import string
import urllib2
import simplejson
import re
import pdb

service = 'http://en.wikipedia.org/w/api.php?'

#dictionary of key to param or list of params
def params_to_response(params):
    temps = []
    for key in params.keys():
        if params[key].__class__.__name__ == 'dict':
            temps.append(key + '=' + string.join(params[key],sep='|'))
        else:
            temps.append(key + '=' + params[key])
    ans = string.join(temps,sep='&')
    f = urllib2.urlopen(service + ans)
    response = simplejson.load(f)
    return response

def string_change_sep(s, i=' ', o='%20'):
    return string.join(string.split(s,sep=i),sep='_')

def get_titles(query):
    params = {}
    params['action'] = 'query'
    params['list'] = 'search'
    params['srnamespace'] = '0'
    params['srsearch'] = string_change_sep(query)
    params['format'] = 'json'
    response = params_to_response(params)
    results = response['query']['search']
    return [result['title'] for result in results]

def get_links(query):
    params = {}
    params['action'] = 'query'
    params['prop'] = 'links'
    params['format'] = 'json'
    params['plnamespace'] = '0'
    params['pllimit'] = '500'
    params['titles'] = string_change_sep(query)
    response = params_to_response(params)
    pid = response['query']['pages'].keys()[0]
    links = response['query']['pages'][pid]['links']
    return [link['title'] for link in links]

def get_categories(query):
    params = {}
    params['action'] = 'query'
    params['titles'] = string_change_sep(query)
    params['prop'] = 'categories'
    params['format'] = 'json'
    params['cllimit'] = '500'
    response = params_to_response(params)
    pid = response['query']['pages'].keys()[0]
    categories = response['query']['pages'][pid]['categories']
    return [category['title'] for category in categories]

def is_person(query):
    return False
    try:
        categories = get_categories(query)
    except:
        return False
    num_birth = 0
    num_death = 0
    num_people = 0
    birth_expr = re.compile('births')
    death_expr = re.compile('deaths')
    people_expr = re.compile('people')
    for category in categories:
        if birth_expr.match(category) != None:
            num_birth = num_birth + 1
        if death_expr.match(category) != None:
            num_death = num_death + 1
        if people_expr.match(category) != None:
            num_people = num_people + 1
    if num_birth > 0 or num_death > 0:
        return True
    else:
        return False

# input is the raw unprocessed link names.  
def get_occurrence_terms(link_title):
    ans = []
    no_paren = string.split(link_title,sep='(')[0].strip()
    ans.append(no_paren)
    # if title is a person, add their last name
    if is_person(link_title):
        ans.append(no_paren.split()[-1])
   # print ans
    return ans

def get_query_terms(link_title):
    no_paren = string.split(link_title,sep='(')[0].strip()
    return [no_paren]

def get_text(page_title):
    params = {}
    params['action'] = 'query'
    params['prop'] = 'extracts'
    params['format'] = 'json'
    params['exchars'] = '100000'
    params['exlimit'] = '1'
    params['titles'] = string_change_sep(page_title)
    response = params_to_response(params)
    pid = response['query']['pages'].keys()[0]
    text = response['query']['pages'][pid]['extract']
    return text

def get_count(s, q):
    expr = re.compile(q)
    return len(expr.findall(s))

def unique(stuff, f):
    seen = set()
    results = []
    for x in stuff:
        if f(x) not in seen:
            seen.add(f(x))
            results.append(x)
    return results

def converter(x):
    return [y[0][0] for y in x]

def run(query, num_to_return = 20):
    titles = get_titles(query)
    title = titles[0]
    link_titles = get_links(title)
    search_terms = [get_occurrence_terms(link_title) for link_title in link_titles]
    num_links = len(link_titles)
    text = get_text(title)
    counts = [0 for i in range(num_links)]
    link_count_tuples = [0 for i in range(num_links)]
    for i in range(num_links):
        link_counts = [get_count(text, s) for s in search_terms[i]]
        counts[i] = max(link_counts)
        link_count_tuples[i] = (get_query_terms(link_titles[i]), counts[i])
    sorted_link_count_tuples = sorted(link_count_tuples, key = lambda x: x[1])
    return converter(unique(sorted_link_count_tuples, lambda x: x[0][0]))[-1*num_to_return:]
