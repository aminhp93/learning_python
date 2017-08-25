from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField
	)

from rest_framework import serializers

from comments.api.serializers import CommentSerializer

from books.models import Book
from comments.models import Comment

book_detail_url = HyperlinkedIdentityField(view_name='books-api:detail', lookup_field='slug')

class BookListSerializer(serializers.ModelSerializer):
	# created = serializers.DateTimeField()
	url = book_detail_url
	class Meta:
		model = Book
		fields = [
			'url',
			'title',
			'review',
			'updated',
			'timestamp'
		]

class BookCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = [
			'title',
			'review'
		]

class BookDetailSerializer(serializers.ModelSerializer):
	comments = SerializerMethodField()
	url = book_detail_url
	class Meta:
		model = Book
		fields = [
			'url',
			'title',
			'review',
			'updated',
			'timestamp',
			'comments',
		]

	def get_comments(self, obj):
		c_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(c_qs, many=True).data
		return comments

		