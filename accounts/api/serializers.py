from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	username = serializers.CharField(max_length=100)
	first_name = serializers.CharField(max_length=100)
	last_name = serializers.CharField(max_length=100)