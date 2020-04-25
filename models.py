from peewee import *

DATABASE = SqliteDatabase('cars.sqlite')


class Car(Model):
	model = CharField()
	make = CharField()
	year = BitField()
	suv = BooleanField() 
	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Car], safe=True)
	print('connected and create_tables')
	DATABASE.close()
