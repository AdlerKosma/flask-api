# flask-app.py
from flask import Flask, request
import json

# create a Flask instance
app = Flask(__name__)

# a simple description of the API written in html.
# Flask can print and return raw text to the browser.
# This enables html, json, etc.

description =   """
                <!DOCTYPE html>
                <head>
                <title>API Landing</title>
                </head>
                <body>
                    <h3>A simple API to verify IBAN numbers</h3>
                    <a href="http://localhost:5000/iban?input=BE71096123456769">sample request</a>
                </body>
                """

# Routes refer to url'
# our root url '/' will show our html description
@app.route('/', methods=['GET'])
def hello_world():
    # return a html format string that is rendered in the browser
	return description

# our '/iban' url
# Sample: http://localhost:5000/iban?input=SK0809000000000123123123
@app.route('/iban', methods=['GET'])
def check_iban():
    countries = ["SK", "SE", "CH", "ES", "BE", "BR", "FR", "IE", "DE", "GR", "MU", "PK", "PL", "RO", "LC", "SA", "GB"]
    inp = request.args['input']
    if inp[:2] in countries:
        if inp[2:4].isdigit():
            return json.dumps({"IBAN" : "Correct"})


    return json.dumps({"IBAN" : "False"})

if __name__ == "__main__":
	# for debugging locally
	# app.run(debug=True, host='0.0.0.0',port=5000)

	# for production
	app.run(host='0.0.0.0', port=5000)
