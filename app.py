from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = 'keysmithsmakekeys'

username = 'admin'
password = 'password'

@app.route('/')                                                                 
def root():
    #return  'GO TO 127.0.0.1:5000/login TO LOG IN'
    if 'user' in session:
        print session
        return redirect('/welcome')
    print session
    return redirect('/login')

@app.route('/login', methods=['POST', 'GET'])
def login():
    print session
    return render_template("template.html")

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    #DEBUGGING, SOMETHING IS WRONG HERE...
    if 'user' in session:
        print "HEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUWYYYYYYYYYYYYYYYYYY"
    else:
        print "OOOOOOOOOOOOOOOOOOOOOHHHHHHHHHHHH NOOOOOOOOOOOOOOO"
    print request.form
    print session
    if request.form['user'] == username and request.form['pass'] == password:
        if 'user' in session:
		    return render_template('welcome.html')
        else:
            session['user'] = 'data'
            return render_template('welcome.html')
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
   return redirect('/login')

if __name__ == '__main__':
    app.debug = True
    app.run()
