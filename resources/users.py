import models
from flask import Blueprint, request, jsonify

users = Blueprint('users', 'users')


@users.route('/', methods=['GET'])
def user_resource():
	return "connected"