from flask import Flask, render_template, request, session, redirect, url_for

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
	    return render_template('welcome.html')
	else:
	    return render_template("template.html")

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
	#if session is already in place, go to welcome.html without asking for request
    if 'user' in session:
        print "HEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUWYYYYYYYYYYYYYYYYYY"
        return render_template('welcome.html')
    else:
        print "OOOOOOOOOOOOOOOOOOOOOHHHHHHHHHHHH NOOOOOOOOOOOOOOO"
		
    #if session was not in place, use the info inputted by the user to go to welcome.html
    if request.form['user'] == username and request.form['pass'] == password:
        if 'user' in session:
		    return render_template('welcome.html')
        else:
            session['user'] = 'data'
            return render_template('welcome.html')
			
	#if the username, password, or both were wrong
    else:
        wrong = 'SORRY, BUT YOUR '
        if request.form['user'] != username and request.form['pass'] != password:
            wrong += 'USERNAME AND PASSWORD'
        else:
            if request.form['user'] != username:
                wrong += 'USERNAME'
            else:
                wrong += 'PASSWORD'
        return render_template('badlogin.html', problem = wrong+' IS INCORRECT, PLEASE TRY AGAIN')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
   print session
   session.pop('user')
   return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
