import csv
from foo import go_incidents
from helpers import get_wiki_photo
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():
    html = render_template('homepage.html')
    return html

@app.route("/results")
def results():
    reqargs = request.args
    _sortby = reqargs.get('sortby')
    _airline = reqargs.get('airline')
    _species = reqargs.get('species')
    _airport = "SFO"
    #_airport = reqargs.get('airport')

    if not _airline and not _species:
        return """
        <h1>Error</h1>
            <p>Must have either an airline or bird species value</p>
            <p>Go <a href="{url}">back</a></p>
        """.format(url=request.referrer)

    elif request.args.get('airline'):
        search_type = 'airline'
        search_val = request.args.get('airline')
        photo_url = get_wiki_photo(search_val)
        kills = go_incidents(airline=search_val, sortby=_sortby)
    
    elif request.args.get('species'):
        search_type = 'species'
        search_val = request.args.get('species')
        photo_url = get_wiki_photo(search_val)
        kills = go_incidents(species=search_val, sortby=_sortby)

    elif request.args.get('airport'):
        search_type = 'airport'
        search_val = request.values.get('airport')
        photo_url = get_wiki_photo(search_val)
        kills = go_incidents(airport=search_val, sortby=_sortby)

    html = render_template('results.html', incidents=kills, sortby=_sortby, 
        search_type=search_type, search_val=search_val, photo_url=photo_url)

    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)