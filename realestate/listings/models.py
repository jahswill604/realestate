from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1,null=True)
    photo_main = models.ImageField(upload_to='media',null=True)
    photo_birthroom = models.ImageField(upload_to='media',null=True)
    photo_kitchen = models.ImageField(upload_to='media',null=True)
    photo_bedroom = models.ImageField(upload_to='media', null=True)
    # photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # Add more fields as needed

    def __str__(self):
        return self.title
