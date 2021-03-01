from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

