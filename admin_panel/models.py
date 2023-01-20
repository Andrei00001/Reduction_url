from django.db import models


# Create your models here.

class URL(models.Model):
    class Meta:
        db_table = 'url'

    url = models.CharField(max_length=2048)
    reduction_url = models.CharField(max_length=2048,unique=True)
    expired_at = models.DateField(null=True)
