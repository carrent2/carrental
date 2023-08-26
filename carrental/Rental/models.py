from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models

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
    deposit = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        """Return name of car"""
        return f'{self.brand} {self.model} {self.year}'


class UserProfile(BaseModel):
    """UserProfile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

    def __str__(self):
        return {self.user.username}


from django.core.exceptions import ValidationError
from django.db import models

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        conflicting_rentals = Rental.objects.filter(
            car=self.car,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date
        ).exclude(pk=self.pk)  # wykluczenie aktualnego wypozyczenia przy aktualizacji

        if conflicting_rentals.exists():
             raise ValidationError('Auto jest niedostępne w tym terminie, proszę wybrać inny termin.')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.clean()  # przeprowadz walidacje przed przekalkulowaniem ceny.
            self.price = self.car.price * (self.end_date - self.start_date).days
        super().save(*args, **kwargs)

    