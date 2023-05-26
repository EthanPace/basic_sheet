from django.db import models

class Sheet(models.Model):
	name = models.CharField(max_length=200)
	career = models.CharField(max_length=200)
	strength = models.IntegerField(default=0)
	dexterity = models.IntegerField(default=0)
	constitution = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	wisdom = models.IntegerField(default=0)
	charisma = models.IntegerField(default=0)
	armor_class = models.IntegerField(default=0)
	speed = models.IntegerField(default=0)
	hit_points = models.IntegerField(default=0)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'career': self.career,
			'strength': self.strength,
			'dexterity': self.dexterity,
			'constitution': self.constitution,
			'intelligence': self.intelligence,
			'wisdom': self.wisdom,
			'charisma': self.charisma,
			'armor_class': self.armor_class,
			'speed': self.speed,
			'hit_points': self.hit_points,
		}

	def make(self, body):
		self.name = body['name']
		self.career = body['career']
		self.strength = body['strength']
		self.dexterity = body['dexterity']
		self.constitution = body['constitution']
		self.intelligence = body['intelligence']
		self.wisdom = body['wisdom']
		self.charisma = body['charisma']
		self.armor_class = body['armor_class']
		self.speed = body['speed']
		self.hit_points = body['hit_points']