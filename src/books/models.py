from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from learning_python.utils import create_slug

from comments.models import Comment

# Create your models here.
class Book(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title 		= models.CharField(max_length=120)
	review		= models.TextField()
	slug 		= models.SlugField(unique=True)
	comments 	= GenericRelation(Comment)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("books:detail", kwargs={"slug": self.slug})

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

def pre_save_book_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_book_receiver, sender=Book)