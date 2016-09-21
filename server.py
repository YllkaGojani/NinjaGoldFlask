from flask import Flask,render_template,request,redirect,session,flash
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	session['gold']
	return render_template("index.html",gold = session['gold'])

@app.route('/process_money',methods=['POST'])
def findGold():
	session['numberFarm'] = random.randrange(10,21)
	session['numberCave'] = random.randrange(5,11)
	session['numberHouse'] = random.randrange(2,6)
	session['numberCasino']	= random.randrange(-50,51) 
	if(request.form['building'] == 'farm'): 
		flash('Earned ' + str(session['numberFarm']) +' from the farm!')
		session['gold'] += session['numberFarm']
		session['color'] = 'green'
	elif(request.form['building'] == 'cave'):
		flash('Earned '	+ str(session['numberCave']) + ' from the cave!')
		session['gold'] += session['numberCave']
		session['color'] = 'green'
	elif(request.form['building'] == 'house'):
		flash('Earned ' + str(session['numberHouse']) + ' from the house!')
		session['gold'] += session['numberHouse']
		session['color'] = 'green'
	elif(request.form['building'] == 'casino'):
		if(session['numberCasino'] < 0):
			flash('Lost ' + str(session['numberCasino']) + ' from the casino! Ouch...')
			session['gold'] += session['numberCasino']
			session['color'] = 'red'
		elif(session['numberCasino'] >= 0):
			flash('Earned ' + str(session['numberCasino']) + ' from the casino!')
			session['gold'] += session['numberCasino']
			session['color'] = 'green'
	return redirect('/')
					
app.run(debug=True)	