from django.db import models
from managing.models import Locale
from datetime import datetime


STATUS_CHOICE = {
  ('A', 'Archive'),
	('O', 'Own'),
	('P', 'Public'),
}

class Rightnow(models.Model):
  content = models.TextField(max_length=100)
  mood = models.CharField(max_length=15, null=True, blank=True)
  status = models.CharField(max_length=3, choices=STATUS_CHOICE, default="P")
  language = models.ForeignKey(Locale, null=True, blank=True, on_delete=models.DO_NOTHING)
  created = models.DateTimeField(default=datetime.now())