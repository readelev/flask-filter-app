import csv
from flask import Flask, render_template, request
from foo import get_data
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

    if not _airline and not _species:
        return """
        <h1>Error</h1>
            <p>Must have either an airline or bird species value</p>
            <p>Go <a href="{url}">back</a></p>
        """.format(url=request.referrer)

    elif requests.args.get('airline'):
        search_type = 'airline'
        search_val = request.args.get('airline')
        kills = splat_splat(species=search_val, sortby=_sortby)
    elif requests.args.get('species'):
        search_type = 'species'
        search_val = requests.args.get('species')
        kills = splat_splat(species=search_val, sortby=_sortby)

    html = render_template('results.html', incidents=kills, sortby=_sortby, 
        search_type=search_type, search_val=search_val)

    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)