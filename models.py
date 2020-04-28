from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('cars.sqlite')


class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	class Meta:
		database = DATABASE

class Car(Model):
	user = ForeignKeyField(User, backref='cars')
	model = CharField()
	make = CharField()
	year = BitField()
	suv = BooleanField() 
	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Car], safe=True)
	print('connected and create_tables')
	DATABASE.close()
