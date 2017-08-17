from rest_framework import serializers

from books.models import Book

class BookListSerializer(serializers.ModelSerializer):
	# created = serializers.DateTimeField()

	class Meta:
		model = Book
		fields = [
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
	class Meta:
		model = Book
		fields = [
			'title',
			'review',
			'updated',
			'timestamp'
		]

		