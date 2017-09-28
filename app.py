from flask import Flask, render_template
from utils import occupy

app = Flask(__name__)

@app.route('/')
def main():
	return "Add '/occupations' and you might find what you're looking for."

@app.route('/occupations')
def display():
    return render_template('template.html', dict = occupy.reader('data/occupations.csv'), random = occupy.choosejob('data/occupations.csv'))
	
if __name__ == '__main__':
    app.run()
