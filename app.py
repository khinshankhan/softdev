from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = 'keysmithsmakekeys'

username = 'admin'
password = 'password'

@app.route('/')                                                                 
def root():
    #return  'GO TO 127.0.0.1:5000/login TO LOG IN'
    if 'user' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
	#if session is already in place, go to welcome.html right away
	#otherwise, go to login page
	if 'user' in session:
	    return redirect(url_for('welcome'))
	else:
	    return render_template("template.html")

#checks
#will say what's wrong
def authenticate(user, passw):
    if username == user:
        if password == passw:
            return 'good'
        else:
            return 'password'
    else:
        if password == passw:
            return 'username'
        else:
            return 'username and password'

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    if 'user' not in session:
        print 'NOT LOGGED IN'
        if request.args != []:
            #print request.args
            print 'REQUESTS MADE'
            user = request.form['user']
            passw = request.form['pass']
        
            result = authenticate(user, passw)
        
            if result == 'good':
                session['user'] = user
            else:
                flash ('Sorry, but your '+ result + ' is wrong. Please try again')
        print 'FINALE!'
        return redirect(url_for('login'))

    else:
        return render_template('welcome.html', name = session['user'])

@app.route('/logout', methods=['POST', 'GET'])
def logout():
   print session
   session.pop('user')
   return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
