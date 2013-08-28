# TODO:
# Tests (pull out GPIO access into a class I can easily test and get rid of the test model)
# P2 Take X readings and average them to prevent issues (can repro if update time is 0.1)
# Validate form data
# Make names consistent (push frequency, frequency)

from flask import *
import json
import model, photocell

DEBUG = True
PHOTOCELL_PIN = 18

# Initialize flask app
app = Flask(__name__)
app.config.from_object(__name__)

photocell = photocell.PhotoCell(PHOTOCELL_PIN)
model = model.RiceCookerModel(photocell)

# Turn stream of raw data into JSON results in server sent data format.
def statusJSON(stream):
	for status, reading in stream:
		yield 'data: %s\n\n' % json.dumps({'status': status, 'raw': reading })

# Define views
@app.route('/')
def main():
	return render_template('main.html', model=model)

@app.route('/status')
def streamStatus():
	return Response(statusJSON(model.streamStatus()), mimetype='text/event-stream')

@app.route('/settings', methods=['POST'])
def updateSettings():
	model.setFrequency(float(request.form['frequency']))
	model.setThreshold(int(request.form['threshold']))
	return redirect(url_for('main'))

# Start running the flask app
if __name__ == '__main__':
	app.run(host='0.0.0.0')