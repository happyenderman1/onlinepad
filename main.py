from flask import Flask 
from flask import request 
from flask import render_template as readht
try:
  from lightdb import LightDB
except:
  import os
  os.system('pip install lightdb')
  from lightdb import LightDB

import random,string
db = LightDB('db.json')
app = Flask('OnlinePad')

@app.route('/')
def home():
    return readht('./index.html')
@app.route('/script.js')
def script():
    return readht('./script.js') 
@app.route('/style.css')
def style():
    return readht('./style.css')
@app.route('/api/v1/publish',methods=['POST'])
def publish():
    text = request.args.get('text')
    name = request.args.get('name')
    key = ""
    for n in range(8):
        key += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    db.set(key,{"name": name,"text": text})
    return {"key": key}

@app.route('/view')
def vie():
    key = request.args.get('key')
    for n in range(1):
        info = db.get(key)
        if info is not None:
            name = info['name']
            value = info['text']
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <title>Online pad</title>
            <link href="style.css" rel="stylesheet" type="text/css" />
            <script
            src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
            <link rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
            <script
            src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <meta content="OnlinePad" property="og:title" />
            <meta content="OnlinePad is a online notepad,You can use it to create save,download,copy, files contents! " property="og:description" />
            <meta content="https://OnlinePad.happyenderyt.repl.co" property="og:url" />
            <meta content="https://cdn-icons-png.flaticon.com/512/588/588395.png" property="og:image" />
            <meta content="#43B581" data-react-helmet="true" name="theme-color" />
	        </head>
            <body style="background-color: darkgoldenrod;">
		    <br>
		    <center>
		    <h1 style="color: black" class="title">Online Pad</h1>
            <p style="color:gray">{name}</p>
		    </div>
	        <br>
	        <br>
	        <textarea  id="e" style="width: 589px; height: 183px;" class="form-control mr-sm-2" placeholder="" disabled="true">{value}</textarea>
	        <br>
            <script src="script.js"></script>		 
	        </center>

            </body>
            </html>
            """
        if info is None:
            return """
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <title>Online pad</title>
            <link href="style.css" rel="stylesheet" type="text/css" />
            <script
            src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
            <link rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
            <script
            src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <meta content="OnlinePad" property="og:title" />
            <meta content="OnlinePad is a online notepad,You can use it to create save,download,copy, files contents! " property="og:description" />
            <meta content="https://OnlinePad.happyenderyt.repl.co" property="og:url" />
            <meta content="https://cdn-icons-png.flaticon.com/512/588/588395.png" property="og:image" />
            <meta content="#43B581" data-react-helmet="true" name="theme-color" />
	        </head>
            <body style="background-color: darkgoldenrod;">
		    <br>
		    <center>
		    <h1 style="color: black" class="title">Online Pad</h1>
            <p style="color:red">Error,Document not found!</p>
		    </div>
	        <br>
	        <br>
	        <textarea  id="e" style="width: 589px; height: 183px;" class="form-control mr-sm-2" placeholder="" disabled="true">Document not found!</textarea>
	        <br>
            <script src="script.js"></script>		 
	        </center>

            </body>
            </html>
            """
app.run(port=80)   