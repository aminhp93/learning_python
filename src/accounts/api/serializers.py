from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField
)
from rest_framework import serializers
from accounts.models import MyUser

class UserListSerializer(serializers.ModelSerializer):
	url = HyperlinkedIdentityField(view_name='users-api:detail', lookup_field='pk')

	class Meta:
		model = MyUser
		fields = [
			'url',
			'id',
			'email',
			'username',
			'first_name',
			'last_name',
		]


class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser
		fields = [
			'username'
		]