from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255, null=True)
    no_of_guests = models.IntegerField(default=6)
    bookingdate = models.DateTimeField(auto_created=True, null=True)

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.title
