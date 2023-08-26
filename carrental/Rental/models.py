from datetime import timezone

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class Car(BaseModel):

    brand = models.CharField(max_length=64, null=False)    
    model = models.CharField(max_length=64, null=False)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2023)], null=False)
    deposit = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'


class UserProfile(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def __str__(self):
        return {self.user.username}


class Rental(BaseModel):

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.car} {self.user} {self.start_date} {self.end_date}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.price = self.car.price * (self.end_date - self.start_date).days

        super(Rental, self).save(*args, **kwargs)