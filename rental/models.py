from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class Tool(models.Model):
    current_status = (
        ("A", "Available"),  # Tool available to rent
        ("R", "Rented"),  # Tool is already rented
        ("N", "Not-Available")  # Tool can't be rented
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=2551)
    status = models.CharField(choices=current_status, default="A", max_length=1)
    added_at = models.DateTimeField(auto_now_add=True)
    last_rental = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    image_url = models.URLField(blank=True,null=True)
    price = models.IntegerField()
    def __str__(self):
        return self.name


class RentalDetails(models.Model):
    rental_choices = (
        ("D", "Done"),  # The rental time is finished
        ("C", "Canceled"),  # The renter canceled
        ("A", "Active")  # The tool is still rented
    )
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    status = models.CharField(choices=rental_choices, max_length=1, default="A")

    def __str__(self):
        return self.tool.name + "," + self.renter.username
