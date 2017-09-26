from flask import Flask, render_template
from occupy import reader, choosejob()

app = Flask(__name__)

@app.route('/occupations')
def display():
    return render_template('template.html')

if __name__ == '__main__':
    app.run()
