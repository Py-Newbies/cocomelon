from django.core.management.base import BaseCommand
from apie.models import Book
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generates sample data for the Book model.'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for i in range(10):
            title = fake.text(max_nb_chars=50)
            author = fake.name()
            publication_date = fake.date_between(start_date='-30y', end_date='today')
            pages = random.randint(100, 500)
            book = Book.objects.create(
                title=title,
                author=author,
                publication_date=publication_date,
                pages=pages
            )
            book.save()
        self.stdout.write(self.style.SUCCESS('Sample data generated successfully.'))
