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
                    <a href="http://localhost:5000/iban?input=BE71096123456769"></a>
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
    letter_dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
              "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31,
              "W": 32, "X": 33, "Y": 34, "Z": 35,
              "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    letters = {ord(k): str(v) for k, v in letter_dic.items()}

    my_iban = request.args['input']

    if chech_validation_chars_iban(my_iban, letters) == int(my_iban[2:4]):
        if validate_iban(my_iban, letters) == 1:
            iban = 'valid!\n'
        else:
            iban = 'false!\n'
    else:
        iban = 'false!\n'

    return json.dumps({"IBAN" : iban})


def chech_validation_chars_iban(iban, letters):
    zeros_iban = iban[:2] + '00' + iban[4:]
    iban_inverted = zeros_iban[4:] + zeros_iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    verification_chars = 98 - (int(iban_numbered) % 97)

    if verification_chars < 10:
        verification_chars = '{:02}'.format(int(verification_chars))
    return verification_chars


def validate_iban(iban, letters):
    iban_inverted = iban[4:] + iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    return int(iban_numbered) % 97

if __name__ == "__main__":
	# for debugging locally
	# app.run(debug=True, host='0.0.0.0',port=5000)

	# for production
	app.run(host='0.0.0.0', port=5000)
