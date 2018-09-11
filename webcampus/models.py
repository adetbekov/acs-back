from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from datetime import datetime
from django.contrib.auth.models import User

from managing.models import Category, Tag, Locale


STATUS_CHOICE = {
	('H', 'Hidden'),
	('V', 'Visible'),
	('A', 'Archive')
}

DEGREE_CHOICE = {
	('0', 'Beginner'),
	('1', 'Elementary'),
	('2', 'Intermediate'),
	('3', 'Advanced'),
}


def upload_location(instance,filename):
	return "webcampus/%s" %(filename)


class Subject(models.Model):
	name = models.CharField(max_length=30, blank=False)
	icon_name = models.CharField(max_length=30, default="")
	color = models.CharField(max_length=30, default="#34495e")
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Субъект"
		verbose_name_plural = "Субъекты"

	def __str__(self):
		return str(self.name)

class Trajectory(models.Model):
	name = models.CharField(max_length=30, blank=False)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Траектория"
		verbose_name_plural = "Траектории"

	def __str__(self):
		return str(self.name)

class Course(models.Model):
	name = models.CharField(max_length=30, blank=False)
	name_slug = models.SlugField(unique=True, null=True, blank=True)
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
	trajectory = models.ForeignKey(Trajectory, null=True, blank=True, on_delete=models.DO_NOTHING)
	subjects = models.ManyToManyField(Subject, related_name="course_subjects", blank=True)
	degree = models.CharField(max_length=3, choices=DEGREE_CHOICE, default="0")
	description = models.TextField()
	author = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
	language = models.ForeignKey(Locale, null=True, blank=True, on_delete=models.DO_NOTHING)
	image = models.ImageField(null=True, blank=True, upload_to=upload_location)
	content = models.TextField()
	status = models.CharField(max_length=3, choices=STATUS_CHOICE, default="H")
	tags = models.ManyToManyField(Tag, related_name="course_tags", blank=True)
	students = models.ManyToManyField(User, related_name="course_students", blank=True)
	price = models.IntegerField(default=0)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Курс"
		verbose_name_plural = "Курсы"

	def __str__(self):
		return str(self.name)

	def slug(self):
		return slugify(unidecode(self.name))

	def save(self, *args, **kwargs):
		self.name_slug = self.slug()
		super(Course, self).save(*args, **kwargs)

class Chapter(models.Model):
	name = models.CharField(max_length=30, blank=False)
	name_slug = models.SlugField(unique=True, null=True, blank=True)
	course = models.ForeignKey(Course, related_name="chapters", on_delete=models.CASCADE)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Глава"
		verbose_name_plural = "Главы"

	def __str__(self):
		return str(self.name)

	def slug(self):
		return slugify(unidecode(self.name))

	def save(self, *args, **kwargs):
		self.name_slug = self.slug()
		super(Chapter, self).save(*args, **kwargs)

class Step(models.Model):
	title = models.CharField(max_length=30, blank=False)
	title_slug = models.SlugField(unique=True, null=True, blank=True)
	chapter = models.ForeignKey(Chapter, related_name="steps", on_delete=models.CASCADE)
	done = models.ManyToManyField(User, blank=True)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Шаг"
		verbose_name_plural = "Шаги"

	def __str__(self):
		return str(self.title)

	def slug(self):
		return slugify(unidecode(self.title))

	def save(self, *args, **kwargs):
		self.title_slug = self.slug()
		super(Step, self).save(*args, **kwargs)

class Text(models.Model):
	step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name="texts")
	content = models.TextField()
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Текст"
		verbose_name_plural = "Тексты"

	def __str__(self):
		return str(self.step.title) + "_text"

class HtmlBlock(models.Model):
	step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name="htmlblocks")
	content = models.TextField()
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Html блок"
		verbose_name_plural = "Html блоки"

	def __str__(self):
		return str(self.step.title) + "_html"

class Video(models.Model):
	step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name="videos")
	uri = models.CharField(max_length=255)
	visible = models.BooleanField(default=True)
	duration = models.IntegerField()

	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Видео"
		verbose_name_plural = "Видео"

	def __str__(self):
		return str(self.step.title) + "_video"
