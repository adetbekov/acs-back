from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=30, blank=False)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

	def __str__(self):
		return str(self.name)


class Tag(models.Model):
	name = models.CharField(max_length=30, blank=False)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Тег"
		verbose_name_plural = "Теги"

	def __str__(self):
		return str(self.name)


class Locale(models.Model):
	code = models.CharField(max_length=2)
	translit = models.CharField(max_length=15)
	original = models.CharField(max_length=20)
	created = models.DateTimeField(default=datetime.now())

	class Meta:
		verbose_name = "Локаль"
		verbose_name_plural = "Локали"

	def __str__(self):
		return str(self.translit)