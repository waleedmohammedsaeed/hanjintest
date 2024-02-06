from django.db import models
# from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=50)

    def __str__(self):
        return self.branch_name

class Category(models.Model):
    catName = models.CharField(max_length=60)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.catName

class Services(models.Model):
    serName = models.CharField(max_length=50)
    desc = models.TextField()
    categeory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.serName


