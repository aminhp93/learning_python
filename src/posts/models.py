from markdownx.utils import markdownify

from markdownx.models import MarkdownxField

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe

from learning_python.utils import create_slug, get_read_time

from comments.models import Comment
from tags.models import Tag

# Create your models here.
class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
	PostModel = instance.__class__

	new_id = PostModel.objects.order_by('id').last().id + 1
   
	return "%s/%s" %(new_id, filename)
	return filename

class Post(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title 		= models.CharField(max_length=120)
	slug 		= models.SlugField(unique=True)
	content		= MarkdownxField()
	draft		= models.BooleanField(default=False)
	publish		= models.DateField(auto_now=False, auto_now_add=False)
	image		= models.ImageField(
								upload_to=upload_location,
								null=True,
								blank=True,
								width_field='width_field',
								height_field='height_field'
							)
	width_field = models.IntegerField(default=0)
	height_field= models.IntegerField(default=0)
	read_time	= models.IntegerField(default=0)
	comments 	= GenericRelation(Comment)
	tag			= models.ManyToManyField(Tag)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects = PostManager()

	class Meta:
		ordering = ["-timestamp", "-updated"]

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})

	# def get_markdown(self):
	# 	content = self.content
	# 	result = mark_safe(content)
	# 	print(result)
	# 	return result


	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

	@property
	def formatted_markdown(self):
		return markdownify(self.content)

def pre_save_book_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

	# if instance.content:
	# 	html_string = instance.get_markdown()
	# 	read_time_var = get_read_time(html_string)
	# 	instance.read_time = read_time_var

pre_save.connect(pre_save_book_receiver, sender=Post)