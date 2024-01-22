from flask import Flask, render_template, redirect
import os
import sys
import requests

app = Flask(__name__)

@app.route('/')
def automation():
    return render_template('index.html', title='ORCiD - Invenio RDM')

@app.route('/loginout')
def loginout():
    redirect_url = 'https://orcid-u4sp7ks5ea-uc.a.run.app'
    client_id = 'APP-H3UJXZYQA04CJ3FU'
    oauth_url = 'https://orcid.org/oauth/authorize?client_id=%s&response_type=code&scope=/read-limited&redirect_uri=%s' % (client_id, redirect_url)
    response = requests.get(oauth_url)
    results = response.json()
    return redirect('/')


@app.route('/build', methods=['GET', 'POST'])
def build():
    try:
        build_file = open('static/build.txt')
        build_stamp = build_file.readlines()[0]
        build_file.close()
    except FileNotFoundError:
        from datetime import date
        build_stamp = generate_build_stamp()
    results = 'Running %s %s.\nBuild %s.\nPython %s.' % (sys.argv[0], app.name, build_stamp, sys.version)
    return results

def generate_build_stamp():
    from datetime import date
    return 'Development build - %s' % date.today().strftime("%m/%d/%y")

print('Starting %s %s' % (sys.argv[0], app.name))
print('Python: ' + sys.version)

try:
    build_file = open('static/build.txt')
    build_stamp = build_file.readlines()[0]
    build_file.close()
except FileNotFoundError:
    from datetime import date
    build_stamp = generate_build_stamp()
print('Running build: %s' % build_stamp)
print('\nEnvironment Variables:')
for key in os.environ.keys():
    print('%s: \t\t%s' % (key, os.environ[key]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))



