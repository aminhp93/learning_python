from django.db import models

# Create your models here.
class Tag(models.Model):
	tag		= models.SlugField(unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tag

	