import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Tool(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=2551)
    added_at = models.DateTimeField(auto_now_add=True)
    last_rental = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    price = models.IntegerField()

    def rent(self, user, number_of_days)->bool:
        """Rent current tool, return true if the rent process is successful otherwise false"""
        if user == self.owner or not self.is_available:
            return False

        todayDate = datetime.datetime.today().date()
        rental_details = RentalDetails(tool=self, renter=user, start_date=todayDate,
                                       end_date=todayDate + datetime.timedelta(days=number_of_days + 1),
                                       total_price=self.price * number_of_days)
        rental_details.save()
        return True

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        """check if is tool is rented """
        history = RentalDetails.objects.filter(tool=self)
        return not any(s.is_active for s in history)



class RentalDetails(models.Model):
    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(null=True, auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    total_price = models.IntegerField()
    canceled = models.BooleanField(default=False)

    @property
    def is_active(self):
        """check if tool is still rented , return false if either canceled ir finished"""
        if self.canceled or timezone.now() >= self.end_date:
            return False
        return True

    def __str__(self):
        return self.tool.name + "," + self.renter.username
