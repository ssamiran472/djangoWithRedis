from django.core.management.base import BaseCommand
from mainApp.models import Musician  # Replace 'yourapp' and 'YourModel' with your app and model names
from faker import Faker
fake = Faker()

class Command(BaseCommand):
    help = 'Add some data to the database'

    def handle(self, *args, **options):
        # Your code to add data goes here
        i=0
        while i < 10000:
            item = {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "instrument": fake.last_name(),
            }
            Musician.objects.create(**item)
            i = i+1
        self.stdout.write(self.style.SUCCESS('Data added successfully'))
