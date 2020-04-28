import models
from flask import Blueprint , request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

cars = Blueprint('cars', 'cars')


@cars.route('/', methods=['POST'])
@login_required
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
@login_required
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
@login_required
def delete_car(id):
	dogs = models.Dog.select()
	for dog in dogs:
		dog = model_to_dict(dog)
	if current_user.id == dog['owner']['id']:
		delete_query = models.Car.delete().where(models.Car.id == id)
		delete_query.execute()
			
		return jsonify(
					data={},
					message=f"Successfully Deleted {id}",
					status=200

				), 200
	else:
		return jsonify(
					data={},
					message=f"you must be signed in to delete",
					status=401

				), 401

@cars.route('/<id>', methods=['PUT'])
def update_car(id):
	payload = request.get_json()
	update_car = models.Car.update(
		model=payload['model'],
		make=payload['make'],
		year=payload['year'],
		suv=payload['suv'],

	).where(models.Car.id == id)
	update_car.execute()
	updated_car = models.Car.get_by_id(id) 
	updated_car_dict = model_to_dict(updated_car)

	return jsonify(
		data=updated_car_dict,
		message=f"Successfully updated {id}",
		status=200

		), 200






