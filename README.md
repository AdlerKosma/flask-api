# flask-api


# Build Image

$ docker build -t demo/flask-api:0.0 .


# Run container

$ docker run --name demo-flask-api -d -p 5000:5000 demo/flask-api:0.0


Go to
http://localhost:5000/
to visit the api

Test the API by appending the iban as input. See example below:
http://localhost:5000/iban?input=BE71096123456769
