from django.db import models
from django.urls import reverse
# Create your models here.
class Tag(models.Model):
	tag		= models.SlugField(unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tag

	def get_absolute_url(self):
		return reverse("tags:related", kwargs={"slug": self.tag})

	