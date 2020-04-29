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
		user=current_user.id,
		model=payload['model'], 
		make=payload['make'],
		year=payload['year'],
		suv=payload['suv']
		)
	car_dict = model_to_dict(new_car)
	car_dict['user'].pop('password')
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
	car_to_delete = models.Car.get_by_id(id)
	if current_user.id == car_to_delete.user.id:
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
@login_required
def update_car(id):
	payload = request.get_json()
	car_to_update = models.Car.get_by_id(id)
	if current_user.id == car_to_update.user.id:

		if 'model' in payload:
			car_to_update.model=payload['model'],
		if 'make' in payload:
			car_to_update.make=payload['make'],
		if 'year' in payload:
			car_to_update.year=payload['year'],
		if 'suv' in payload:
			car_to_update.suv=payload['suv'],

		car_to_update.save()
		updated_car_dict = model_to_dict(car_to_update)
		updated_car_dict['user'].pop('password')
		

		return jsonify(
			data=updated_car_dict,
			message=f"Successfully updated {id}",
			status=200

			), 200
	else: 
		return jsonify(
			data={},
			message=f"you must be logged in to update",
			status=200

		), 200







