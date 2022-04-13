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
                    <h2>A simple API to verify IBAN numbers</h2>
                    <h3>Here are some IBAN numbers to test:</h3>
                    <br><a href="http://localhost:5000/iban?input=BE71096123456769">BE71096123456769</a>
                    <br><a href="http://localhost:5000/iban?input=BE71096123456770">BE71096123456770</a>
                    <br><a href="http://localhost:5000/iban?input=GB82WEST12345698765433">GB82WEST12345698765433</a>
                    <br><a href="http://localhost:5000/iban?input=GB82WEST12345698765432">GB82WEST12345698765432</a>
                    <br><a href="http://localhost:5000/iban?input=BE-1096123456769">BE-1096123456769</a>                
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
    """
    Main function for iban verification
    Calls function make_check_digit and validate_iban
    Returns json with 'valid' or 'false'
    """
    letter_dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
              "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31,
              "W": 32, "X": 33, "Y": 34, "Z": 35,
              "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    letters = {ord(k): str(v) for k, v in letter_dic.items()}

    my_iban = request.args['input'].upper() #make sure letters are uppercase

    if len(my_iban) <= 34: # less than 34 char
        try: 
            if make_check_digit(my_iban, letters) == int(my_iban[2:4]): #verify check digit
                if validate_iban(my_iban, letters) == 1: 
                    iban = 'valid'
                else:
                    iban = 'false'
            else:
                iban = 'false'
        except ValueError: #Picks upp special characters and non-english letters
            iban = 'false' 
    else:
        iban = 'false'

    return json.dumps({"IBAN" : iban})


def make_check_digit(iban, letters):
    """
    Make check digit in 4 or 5 steps:
    1.We replace check digits with two zeros
    2.Move 4 first characters to the end
    3.Replace letters with numbers according to dictionary letters
    4.Subtract mod 97 from 98, this needs to be >7
    5.Pad digit with 0 if <10
    """
    zeros_iban = iban[:2] + '00' + iban[4:]
    iban_inverted = zeros_iban[4:] + zeros_iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    verification_chars = 98 - (int(iban_numbered) % 97)

    if verification_chars < 10: #pad check digit with '0' if <10
        verification_chars = '{:02}'.format(int(verification_chars))
    return verification_chars


def validate_iban(iban, letters):
    """
    Validate iban in 3 steps:
    1.Move 4 first characters to back
    2.Replace letters to digits according to dictionary letters
    3.Return mod 97
    """
    iban_inverted = iban[4:] + iban[:4]
    iban_numbered = iban_inverted.translate(letters)

    return int(iban_numbered) % 97

if __name__ == "__main__":
	# for production
	app.run(host='0.0.0.0', port=5000)
