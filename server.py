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
	# I would advise against relying this heavily on session. Session should ideally only contain information that is
	# relevant to a user or this particular session. In this case, keeping track of the gold is a great use of session.
	# Additionally, you use 'extra' space/time computing every value every time as opposed to just computing what you need to.
	session['numberFarm'] = random.randrange(10,21)
	session['numberCave'] = random.randrange(5,11)
	session['numberHouse'] = random.randrange(2,6)
	session['numberCasino']	= random.randrange(-50,51) 
	# The use of flashed messages is okay, but i would suggest maybe creating a more persistent structure to keep track of
	# all the events/messages your user has done during each gold session. having a session['activity_messages'] to keep track
	# of or push messages to and display in your front-end would be one alternative. You can also experiment with keeping a 
	# variable on the backend to do that. Of course, with that comes a different approach to coloring your messages. 
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
		# this is a 'lot' of repeated code. what if you only changed the color based on gold < 0 as opposed to the whole method?
		# maybe something along the lines of if gold > 0, message.color
		elif(session['numberCasino'] >= 0):
			flash('Earned ' + str(session['numberCasino']) + ' from the casino!')
			session['gold'] += session['numberCasino']
			session['color'] = 'green'
	return redirect('/')
					
app.run(debug=True)	
