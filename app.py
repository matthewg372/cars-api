from flask import Flask
import models
from resources.cars import cars
from flask_cors import CORS
from resources.users import users
from flask_login import LoginManager

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = "SDKFJHSIKFHSHFDHJKLSJDHKFJFJSLDJKFLSJLFK;LSDKFSFD"
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	try:
		return models.User.get_by_id(user_id)
	except models.DoesNotExist:
		return None



cors = CORS(cars, origins=['http://localhost:3000'],supports_credentials=True)
cors = CORS(users, origins=['http://localhost:3000'],supports_credentials=True)

app.register_blueprint(cars, url_prefix='/api/v1/cars')
app.register_blueprint(users, url_prefix='/api/v1/users')

@app.route('/')
def hello():
	return 'hello world'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)