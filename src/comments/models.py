from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse

# Create your models here.
class Comment(models.Model):
	# user 			= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	content 		= models.TextField()
	timestamp 		= models.DateTimeField(auto_now_add=True)
	content_type 	= models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id 		= models.PositiveIntegerField()
	content_object 	= GenericForeignKey('content_type', 'object_id')
	# parent      	= models.ForeignKey("self", null=True, blank=True)

	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse("comments:detail", kwargs={"id": self.id})