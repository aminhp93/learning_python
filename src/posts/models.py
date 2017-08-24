from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from learning_python.utils import create_slug

from comments.models import Comment

# Create your models here.
class Post(models.Model):

	LANGUAGE_CHOICES = (
			("English", "English"),
			("Vietnamese", "Vietnamese"),
			("Japanese", "Japanese")
		)

	title 		= models.CharField(max_length=120)
	slug 		= models.SlugField(unique=True)
	content		= models.TextField()
	draft		= models.BooleanField(default=False)
	publish		= models.DateTimeField(auto_now=False, auto_now_add=False)
	read_time	= models.IntegerField(default=0)
	language	= models.CharField(
								max_length=120,
								choices=LANGUAGE_CHOICES,
								default="English"
							)
	comments 	= GenericRelation(Comment)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})

def pre_save_book_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_book_receiver, sender=Post)