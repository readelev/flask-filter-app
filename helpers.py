from operator import itemgetter
import csv

DATA_FNAME = './static/data/wildlife.csv'

def get_data():
    # open data file
    # return list of dicts
    with open(DATA_FNAME, 'r') as f:
        c = csv.DictReader(f, fieldnames=['airportcode', 'date', 'airline', 'species', 'damage'])
        return list(c)


def filter_by_airline(airline, datarows):
    matches = []
    for c in datarows:
        # find all incidents
        # that match given z['airline']
        if airline.upper() == c['operator']:
            matches.append(c)
    return matches


def filter_by_species(species, datarows):
    matches = []
    for c in datarows:
        # find all incidents
        # that match given z['species']
        if species.upper() == c['species'].upper():
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