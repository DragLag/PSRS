from django.db import models
from fileman.models import File

class Cron(models.Model):
    egg = models.ForeignKey(File, on_delete=models.CASCADE)
    cron_string = models.CharField(max_length=200)
    cron_date = models.DateTimeField(auto_now_add=True)