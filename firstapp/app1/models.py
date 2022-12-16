from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    price = models.FloatField()
    image_url = models.URLField(
        default='https://static.freeimages.com/images/home/filetypes/photo.png')

    def __str__(self):
        return self.title
