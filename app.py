from flask import Flask, render_template, request, session

app = Flask(__name__)

username = 'asdf'
password = 'this isnt a password'

@app.route('/')                                                                 
def login():
    return render_template("template.html")

@app.route('/login')
def next():
    if request.form['user'] == username and request.form['pass']== password:
        app.secret_key=username
        session[username]='appsession'
        if 'log' in request.args:
            session.pop(username)
        return render_template('welcome.html')
    else:
        if request.form['user'] != username and not request.form['pass']== password:
            wrong = 'USERNAME AND PASSWORD'
        else:
            if +
        return render_template('badlogin.html', wrong)
    
if __name__ == '__main__':
    app.debug = True
    app.run()
