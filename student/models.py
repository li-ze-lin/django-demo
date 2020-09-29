from django.db import models

# Create your models here.
class StudentMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)

    def __str__(self):
        return self.id