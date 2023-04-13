from django.core.management.base import BaseCommand
from apie import models
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generates sample data for the Book model.'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for i in range(100):
            description = fake.text(max_nb_chars=100)
            name = fake.name()
            price = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
            quantity = random.randint(100, 500)
            created_date = fake.date_between(start_date='-30y', end_date='today')
            updated_date = fake.date_between(start_date="-2y", end_date="today")
            product = models.Product.objects.create(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                created_date=created_date,
                updated_date=updated_date
            )
            product.save()
        self.stdout.write(self.style.SUCCESS('Sample data generated successfully.'))
