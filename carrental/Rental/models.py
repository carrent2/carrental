from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils import timezone
from PIL import Image
from decimal import Decimal



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
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField(max_length=1000, default=True, null=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            max_size = (400, 400)  # Maksymalny rozmiar do którego chcesz skalować obrazek
            img.thumbnail(max_size)
            img.save(self.image.path)

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

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f"Komentarz dodany przez {self.user.username if self.user else 'Anonim'} dla {self.car}"



class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    pickup_location = models.CharField(max_length=100)  # Dodaj pole lokalizacji odbioru
    return_location = models.CharField(max_length=100)  # Dodaj pole lokalizacji zwrotu
    additional_info = models.TextField(blank=True, null=True)  # Dodaj pole dodatkowych informacji
    

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, editable=False)

    def calculate_rental_price(self):
        days_rented = (self.end_date - self.start_date).days + 1
        return self.car.price * Decimal(days_rented)

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.calculate_rental_price()
        super().save(*args, **kwargs)

class ContactMessage(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
