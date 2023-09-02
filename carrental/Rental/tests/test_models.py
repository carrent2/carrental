from django.test import TestCase
from Rental.models import Car
from decimal import Decimal

class CarModelTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            brand='Toyota',
            model='Camry',
            year=2022,
            deposit=Decimal('1000.00'),
            price=Decimal('250.00')
        )

    def test_car_creation(self):
        self.assertEqual(self.car.brand, 'Toyota')
        self.assertEqual(self.car.model, 'Camry')
        self.assertEqual(self.car.year, 2022)
        self.assertEqual(self.car.deposit, Decimal('1000.00'))
        self.assertEqual(self.car.price, Decimal('250.00'))

