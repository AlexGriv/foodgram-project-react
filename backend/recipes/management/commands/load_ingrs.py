import csv

from django.conf import settings
from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Add csv files to Django Models.'

    def handle(self, *args, **kwargs):
        data_path = settings.BASE_DIR
        with open(
            f'{ data_path }/data/ingredients.csv',
            newline='',
            encoding='utf-8'
        ) as file:
            spamreader = csv.reader(file, delimiter=',')
            for row in spamreader:
                Ingredient.objects.update_or_create(name=row[0],
                                                    measurement_unit=row[1])
            self.stdout.write(self.style.SUCCESS(
                              'Все ингредиенты загружены.'))
