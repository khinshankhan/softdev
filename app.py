from flask import Flask, render_template, request

app = Flask(__name__)
'''
@app.route('/')
def main():
    if 'data' in request.args:
        return render_template('template.html', entered_name=request.args['data'])
    else:
        return render_template('template.html')
'''
@app.route('/')                                                                 
def root():
    return render_template("template.html", entered_name='', method=request.method)

@app.route('/welcome', methods=['POST'])

def welcome():
    return render_template('template.html', entered_name='Heya, '+request.form['data']+'!',method=request.method)




if __name__ == '__main__':
    app.debug = True
    app.run()
