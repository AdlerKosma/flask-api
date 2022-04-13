# flask-api


# Build Image
$ cd flask-api
$ docker build -t prod/flask-api:0.0 .


# Run container
$ docker run --name prod-flask-api -d -p 5000:5000 prod/flask-api:0.0


# Test API
Go to
http://localhost:5000/
to visit the api

Test the API by appending the iban as input. See example below:
http://localhost:5000/iban?input=BE71096123456769
