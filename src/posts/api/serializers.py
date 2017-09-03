from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField
)

from rest_framework import serializers

from comments.api.serializers import CommentSerializer

from posts.models import Post
from comments.models import Comment

post_detail_url = HyperlinkedIdentityField(view_name='posts-api:detail', lookup_field='slug')

class PostListSerializer(serializers.ModelSerializer):
	# created = serializers.DateTimeField()
	url = post_detail_url
	class Meta:
		model = Post
		fields = [
			'url',
			'title',
			'updated',
			'timestamp'
		]

class PostCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
			'publish',
			'image',
		]


	def validate_content(self, data):
		print('clean contnet')
		print(self, data) 
		if len(data) < 4:
			raise serializers.ValidationError("Content is too short. Should be more than 4 characters")
		return data


class PostDetailSerializer(serializers.ModelSerializer):
	comments = SerializerMethodField()
	image = SerializerMethodField()
	url = post_detail_url
	class Meta:
		model = Post
		fields = [
			'url',
			'title',
			'content',
			'updated',
			'timestamp',
			'comments',
			'image',
		]

	def get_comments(self, obj):
		c_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(c_qs, many=True).data
		return comments

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image