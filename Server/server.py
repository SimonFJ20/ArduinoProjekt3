import os
from flask import Flask,redirect,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/request')
def request():
    return render_template('request.html')
    
@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/uploadrequest/datahandler', methods=['POST', 'GET'])
def uploadrequestdatahandler():
    error = None
    if request.method == 'POST':
        return "bruh"
    return render_template('datahandler.html')

@app.route('/initiate')
def initiate():
    return render_template('js/initiate.js')

@app.route('/datasort')
def datasort():
    return render_template('js/data-sort.js')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
