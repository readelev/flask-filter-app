import csv
import requests
from operator import itemgetter

DATA_FNAME = './static/data/wildlife.csv'
CODES_FNAME = './static/data/codes.html'

def get_data():
    # open data file
    # return list of dicts
    with open(DATA_FNAME, 'r') as f:
        c = csv.DictReader(f)
        return list(c)


def filter_by_airline(airline, datarows):
    matches = []
    for c in datarows:
        if airline.lower() in c['operator'].lower():
            matches.append(c)
    return matches

def get_wiki_photo(txt):
    a = search_wiki(txt)
    b = get_wiki_photo_url(a)
    return b

def search_wiki(user_input):
    user_input = user_input.strip().lower().replace(" ", "_")

    temp_url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search={term}&namespace=0&limit=10&suggest=true"
    url = temp_url.format(term=user_input)

    site = requests.get(url)
    return site.json()[1][0]

def get_wiki_photo_url(search_term):
    temp_url = "https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={term}"
    url = temp_url.format(term=search_term)

    response = requests.get(url)

    data = response.json()

    x = list(data['query']['pages'].values())
    photo_url = x[0]['thumbnail']['original']

    return photo_url


def filter_by_species(species, datarows):
    matches = []
    for c in datarows:
        # find all incidents
        # with match in given z['species']
        if species.lower() in c['species'].lower():
             matches.append(c)
    return matches

def filter_by_airport(airport, datarows):
    matches = []
    for c in datarows:
        if airport.lower() in c['airport_id'].lower():
             matches.append(c)
    return matches


def sort_by_criteria(criteria, datarows):
    if criteria == 'species':
        rows = sorted(datarows, key=itemgetter('species'))
    elif criteria == 'oldest':
        rows = sorted(datarows, key=itemgetter('incident_date'))
    else:
       # i.e. 'youngest' or any value...just sort by most recent
        rows = sorted(datarows, key=itemgetter('incident_date'), reverse=True)   
    return rows