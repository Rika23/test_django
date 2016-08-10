from django.contrib.postgres.fields import JSONField
from django.db import models

class Form(models.Model):
    data = JSONField()
