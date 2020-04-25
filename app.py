from flask import Flask
import models
from resources.cars import cars

DEBUG=True
PORT=8000

app = Flask(__name__)
app.register_blueprint(cars, url_prefix='/api/v1/cars')

@app.route('/')
def hello():
	return 'hello world'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)