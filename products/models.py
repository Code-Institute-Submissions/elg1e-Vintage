from django.db import models


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buyout = models.DecimalField(max_digits=10, decimal_places=2)
    auctionTimer = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images')
    highestBidder = models.CharField(max_length=250)

    def __str__(self):
        return self.name
