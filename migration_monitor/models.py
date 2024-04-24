from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)

class User(models.Model):
    first_name = models.CharField(max_length=35)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True, blank=True
    )
