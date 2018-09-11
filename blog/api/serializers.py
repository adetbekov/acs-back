from rest_framework import serializers
# from messenger.models import Message
from blog.models import Post, Tag, Category
from django.db.models import Q
from rest_framework.response import Response
from django.conf import settings

from django.contrib.auth.models import User

# class UserSerializer(serializers.Serializer):
# 	id = serializers.IntegerField()
# 	username = serializers.CharField(max_length=100)
# 	first_name = serializers.CharField(max_length=100)
# 	last_name = serializers.CharField(max_length=100)
# 	# class Meta:
# 	# 	model = User
# 	# 	fields = ('id', 'username', 'first_name')


# class MessageSerializer(serializers.ModelSerializer):
# 	user_from = UserSerializer(many=False, read_only=True)
# 	user_to = UserSerializer(many=False, read_only=True)

# 	class Meta:
# 		model = Message
# 		fields = '__all__'

# class ChatMessageSerializer(serializers.ModelSerializer):
# 	# unread_count = serializers.IntegerField()
# 	user_from = UserSerializer(many=False, read_only=True)
# 	user_to = UserSerializer(many=False, read_only=True)
# 	unviewed_count = serializers.SerializerMethodField()

# 	def get_unviewed_count(self, obj):
# 		if 'request' in self.context:
# 			user_to = self.context['request'].user
# 			user_from = obj.user_from
# 		else: 
# 			user_to = self.context['user_to']
# 			user_from = self.context['user_from']
# 		return Message.objects.filter(~Q(user_from=user_to), 
# user_from=user_from, user_to=user_to, viewed__isnull=True).count()

# 	class Meta:
# 		model = Message
# 		fields = '__all__'

# class UserMessagesSerializer(serializers.ModelSerializer):
# 	companion = UserSerializer(many=False, read_only=True)

# 	class Meta:
# 		model = Message
# 		fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['name',]


class TagSerializer(serializers.ModelSerializer):
	categories = serializers.SerializerMethodField() #CategorySerializer(many=True, read_only=True)
	count = serializers.SerializerMethodField()

	class Meta:
		model = Tag
		fields = ['name', 'count', 'categories']

	def get_categories(self, obj):
		categories = []
		posts = Post.objects.filter(tags__name=obj.name)
		for post in posts:
			categories.append(post.category.name)
		return categories

	def get_count(self, obj):
		return Post.objects.filter(tags__name=obj.name).count()

class ShortPostSerializer(serializers.ModelSerializer):
	tags = TagSerializer(many=True, read_only=True)
	category = CategorySerializer(read_only=True)
	
	class Meta:
		model = Post
		fields = ['title_slug', 'title', 'created', 'category', 'tags']

class PostSerializer(serializers.ModelSerializer):
	tags = TagSerializer(many=True, read_only=True)
	image_url = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = ['title_slug', 'title', 'category', 'content', 'author', 'tags', 'status', 'permission_text', 'created', 'image_url' ]

	def get_image_url(self, obj):
		if obj.image:
			return "{0}{1}".format(settings.BASE_URL, obj.image.url)
		else:
			return None



