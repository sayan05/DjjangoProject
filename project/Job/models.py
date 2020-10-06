from django.db import models

# Create your models here.
class Job(models.Model):
    Company_Name=models.CharField(max_length=200)
    Expiry_Date=models.DateTimeField('Expiry Date')
    def __str__(self):
        return self.Company_Name

