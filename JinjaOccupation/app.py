from flask import Flask, render_template
from occupy import reader, choosejob

app = Flask(__name__)

@app.route('/')
def main():
	return "Add '/occupations' and you might find what you're looking for."

@app.route('/occupations')
def display():
    return render_template('template.html', dict = reader('occupations.csv'), random = choosejob('occupations.csv'))

if __name__ == '__main__':
    app.run()
