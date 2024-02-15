import json
from django.core.management.base import BaseCommand
from classifier_comparison.models import Classifier


class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        # Load classifiers from JSON file
        with open('classifiers.json', 'r') as f:
            classifiers = json.load(f)

        # Create Classifier objects and save them to the database
        for classifier_data in classifiers:
            classifier = Classifier(**classifier_data)
            classifier.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with initial data'))
