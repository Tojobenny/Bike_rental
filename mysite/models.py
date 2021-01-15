from django.db import models

# Create your models here.

class category(models.Model):
    Name = models.TextField()
class item(models.Model):
	itemcat=models.ForeignKey(category,on_delete=models.CASCADE)
	ItemName=models.TextField()

# class Musician(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     instrument = models.CharField(max_length=200)

# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()
