from __future__ import print_function
import sys
from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

#PRINTS STUFF!!!!
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return

@app.route('/')                                                                 
def root():
    key = 'Y2Fj9o8eCYnHgVCYuMvKtSi8q7Kgufqgc09mJRIR'
    url = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(key)
    data = urllib2.urlopen(url).read()
    d = json.loads(data)
    #debugging
    '''
    for i in d:
        eprint('TITLE: %s'%i)
        eprint("")
        eprint('ENTRY: %s'%d[i])
        eprint("")
    '''
    return render_template('index.html', d = d)

if __name__ == '__main__':
    app.debug = True
    app.run()
