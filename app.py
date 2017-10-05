from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = 'keysmithsmakekeys'

username = 'admin'
password = 'this isnt a password'

@app.route('/')                                                                 
def root():
    #return  'GO TO 127.0.0.1:5000/login TO LOG IN'
    if 'user' in session:
        return redirect('/welcome')
    return redirect('/login')

@app.route('/login')
def login():
    return render_template("template.html")

@app.route('/welcome', methods=['POST'])
def welcome():
    #DEBUGGING, SOMETHING IS WRONG HERE...
    if 'user' in session:
        print "HEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUWYYYYYYYYYYYYYYYYYY"
    else:
        print "OOOOOOOOOOOOOOOOOOOOOHHHHHHHHHHHH NOOOOOOOOOOOOOOO"
        #return render_template('welcome.html')
    if request.form['user'] == username and request.form['pass'] == password:
        session['user'] = 'user'
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

@app.route('/logout')
def logout():
   session.pop('user')
   return redirect('/login')

if __name__ == '__main__':
    app.debug = True
    app.run()
