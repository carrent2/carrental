from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    """Base model."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""

        abstract = True


class Car(BaseModel):
    """Car model"""

    brand = models.CharField(max_length=64, null=False)
    model = models.CharField(max_length=64, null=False)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2023)], null=False)
    fuel_type = models.CharField(max_length=32, null=False)
    average_fuel_consumption = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    number_of_seats = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    boot_capacity = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    deposit = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        """Return name of car"""
        return f'{self.brand} {self.model} {self.year}'


class UserProfile(BaseModel):
    """UserProfile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)

    def __str__(self):
        """Return name of UserProfile"""
        return f'{self.user} {self.address} {self.phone}'


class Rental(BaseModel):
    """Rental model"""

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        """Return name of rental"""
        return f"{self.car} {self.user} {self.start_date} {self.end_date}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.car.price * (self.end_date - self.start_date).days

        super(Rental, self).save(*args, **kwargs)

