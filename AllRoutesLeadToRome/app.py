from flask import Flask

app = Flask(__name__)

@app.route('/')
def display00():
    return 'Heya! </br> This is the first page! </br> Others are at: /01 /02'

@app.route('/01')
def display01():
    return 'And now: The second page!'

@app.route('/02')
def display02():
    return 'Woah! The last page!'

if __name__ == '__main__':
    app.run()
