from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save

from learning_python.utils import create_slug

# Create your models here.
class Book(models.Model):
	title 		= models.CharField(max_length=120)
	review		= models.TextField()
	slug 		= models.SlugField(unique=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("books:detail", kwargs={"slug": self.slug})

def pre_save_book_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
		print(instance.slug)

pre_save.connect(pre_save_book_receiver, sender=Book)