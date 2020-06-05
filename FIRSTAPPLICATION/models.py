from django.db import models

# Create your models here.
class Personal_information(models.Model):
    id_info=models.CharField(max_length=10)
    Name=models.CharField(max_length=30)
    Contact=models.CharField(max_length=15)
    Address=models.CharField(max_length=100)

    def __str__(self):
        return self.Name