from flask import Flask
import models
from resources.cars import cars
from flask_cors import CORS
# from resources.users import users

DEBUG=True
PORT=8000

app = Flask(__name__)
cors = CORS(cars, origins=['http://localhost:3000'],supports_credentials=True)
# cors = CORS(user, origins=['http://localhost:3000'],supports_credentials=True)
app.register_blueprint(cars, url_prefix='/api/v1/cars')
# app.register_blueprint(users, url_prefix='/api/v1/users')

@app.route('/')
def hello():
	return 'hello world'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)