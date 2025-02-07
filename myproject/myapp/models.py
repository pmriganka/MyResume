from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    contact = models.CharField(max_length=12, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name