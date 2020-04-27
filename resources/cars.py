import models
from flask import Blueprint , request, jsonify
from playhouse.shortcuts import model_to_dict 

cars = Blueprint('cars', 'cars')


@cars.route('/', methods=['POST'])
def create_car():
	payload = request.get_json()
	new_car = models.Car.create(
		model=payload['model'], 
		make=payload['make'],
		year=payload['year'],
		suv=payload['suv']
		)
	car_dict = model_to_dict(new_car)
	return jsonify(
      data=car_dict, 
      message='Successfully created car!',
      status=201
    ), 201

@cars.route('/', methods=['GET'])
def Cars_index():
	result = models.Car
	cars = []
	for car in result:
		Car = model_to_dict(car)
		cars.append(Car)
	return jsonify(
      data=cars, 
      message='Successfully created car!',
      status=200
    ), 200


@cars.route('/<id>', methods=['DELETE'])
def delete_car(id):
	delete_query = models.Car.delete().where(models.Car.id == id)
	delete_query.execute()
		
	return jsonify(
			data={},
			message=f"Successfully Deleted {id}",
			status=200

			), 200






