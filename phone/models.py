from django.db import models
from django.utils import timezone

class Record(models.Model):
	user = models.ForeignKey('auth.User')
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	phonenumber = models.CharField(max_length=11)
	registertime = models.DateTimeField(default=timezone.now)