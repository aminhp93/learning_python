from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)

from comments.models import Comment

comment_detail_url = HyperlinkedIdentityField(
        view_name='comments-api:detail', lookup_field='pk')

class CommentSerializer(ModelSerializer):
	# url = comment_detail_url
	class Meta:
		model = Comment
		fields = [
			# 'url',
			'id',
			'content_type',
			'object_id',
			'parent',
			'content',
			'timestamp',
		]
	
class CommentListSerializer(ModelSerializer):
	url = comment_detail_url
	class Meta:
		model = Comment
		fields = [
			'url',
			'id',
			'content',
			'timestamp'
		]

class CommentDetailSerializer(ModelSerializer):
	url = comment_detail_url
	replies = SerializerMethodField()
	class Meta:
		model = Comment
		fields = [
			'url',
			'id',
			'content_type',
			'object_id',
			'parent',
			'content',
			'timestamp',
			'replies',
		]

	def get_replies(self, obj):
		if obj.is_parent:
			return CommentChildSerializer(obj.children(), many=True).data
		return None


class CommentChildSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = [
			'id',
			'content_type',
			'object_id',
			'parent',
			'content',
			'timestamp',
		]
	