from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    try:
        session['gold']
    except:
        session['gold'] = 0
    try:
        session['comments']
    except:
        session['comments'] = [{'style': 'white', 'comment': 'Welcome to ninja gold'}]
    return render_template('index.html')

@app.route('/process_gold', methods = ['POST'])
def generate_gold():
    mylam = lambda x,y:random.randrange(x,y)
    data = {'cave':mylam(5,11), 'farm':mylam(10,21), 'casino':mylam(-50,51), 'house':mylam(2,6)}
    try:
        request.form['building']
        session['gold'] += data[request.form['building']]
        if data[request.form['building']] > 0:
            style = 'green'
        else:
            style = 'red'
        session['comments'].append({'style':style, 'comment':"You entered the {} and {} {} gold.\n".format(request.form['building'], style, data[request.form['building']])})
    except:
        print 'fail'
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('comments')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)