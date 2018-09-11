from rest_framework import serializers
from webcampus.models import *
from rest_framework.response import Response

from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User

# Store filter
class SubjectSerializer(serializers.ModelSerializer):
	count = serializers.SerializerMethodField()

	class Meta:
		model = Subject
		fields = ['name', 'icon_name', 'color', 'created', 'count']

	def get_count(self, obj):
		return obj.course_subjects.count()

# Course information
class CourseSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Course
		fields = ['name', 'created']


# Short Step title
class StepShortSerializer(serializers.ModelSerializer):
	# done = serializers.SerializerMethodField()

	class Meta:
		model = Step
		fields = ['title', 'slug', 'done', 'created']

	# def get_done(self, obj):
	# 	user = self.context['request'].user
	# 	print(user)
	# 	return user in obj.done.all()

# Short Chapter title
class ChapterShortSerializer(serializers.ModelSerializer):
	steps = StepShortSerializer(many=True, read_only=True)

	class Meta:
		model = Chapter
		fields = ['name', 'slug', 'created', 'steps']

# Syllabus list
class SyllabusSerializer(serializers.ModelSerializer):
	chapters = ChapterShortSerializer(many=True, read_only=True)

	class Meta:
		model = Course
		fields = ['name', 'slug', 'chapters']

# Full Step in Chapter 
class StepFullSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Step
		fields = ['title', 'slug', 'created']


class TextSerializer(serializers.ModelSerializer):

	class Meta:
		model = Text
		fields = [ 'content', 'created' ]


class HTMLBlockSerializer(serializers.ModelSerializer):

	class Meta:
		model = HtmlBlock
		fields = [ 'content', 'created' ]

class VideoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Video
		fields = [ 'uri', 'duration', 'created' ]

