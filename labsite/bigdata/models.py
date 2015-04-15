from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=30)
    identity = models.CharField(max_length=30)
    homepage = models.URLField(null=True)
    def __str__(self):
        return self.name