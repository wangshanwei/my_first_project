from django.db import models

# Create your models here.
class Post(models.Model):
	name = models.CharField(max_length = 25)
	email = models.EmailField()
	phone = models.CharField(max_length = 25)
	comments = models.CharField(max_length = 20)

	def __str__(self):
		return self.name

