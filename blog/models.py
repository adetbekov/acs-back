from django.db import models
from datetime import datetime
from django.utils.text import slugify
from unidecode import unidecode
from django.contrib.auth.models import User

from managing.models import Category, Tag, Locale


STATUS_CHOICE = {
	('D', 'Draft'),
	('O', 'Own'),
	('S', 'Secret'),
	('P', 'Public'),
}


def upload_location(instance,filename):
	return "blog/%s" %(filename)


class Post(models.Model):
	title = models.CharField(max_length=225, blank=False)
	title_slug = models.SlugField(max_length=225, unique=True, null=True, blank=True)
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
	author = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
	language = models.ForeignKey(Locale, null=True, blank=True, on_delete=models.DO_NOTHING)
	image = models.ImageField(null=True, blank=True, upload_to=upload_location)
	content = models.TextField()
	status = models.CharField(max_length=3, choices=STATUS_CHOICE, default="D")
	tags = models.ManyToManyField(Tag, related_name="blog_tags", blank=True)
	password = models.CharField(max_length=30, null=True, blank=True)
	permission_text = models.TextField(null=True, blank=True)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Пост"
		verbose_name_plural = "Посты"

	def __str__(self):
		return str(self.title)
	
	def slug(self):
		return slugify(unidecode(self.title))

	def save(self, *args, **kwargs):
		self.title_slug = self.slug()
		super(Post, self).save(*args, **kwargs)
