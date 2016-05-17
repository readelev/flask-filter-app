from helpers import get_data
from helpers import filter_by_airline, filter_by_species, sort_by_criteria

# store the datarows in memory
incidents = get_data()

# this function is the only one that app.py needs to know about
def get_data(species="", airline="", sortby="alpha"):
    matched_rows = []
    datarows = incidents
    # first, filter
    if airline:
        filteredrows = filter_by_airline(airline, incidents)
    else:
        # by default, search by species
        filteredrows = filter_by_species(species, incidents)
    # then, sort and return the result
    # remember to pass in filteredrows, not incidents
    return sort_by_criteria(sortby, filteredrows)


def print_record_count():
    print("There are", len(incidents), 'rows.')