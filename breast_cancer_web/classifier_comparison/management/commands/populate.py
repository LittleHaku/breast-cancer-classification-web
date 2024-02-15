import json
from django.core.management.base import BaseCommand
from classifier_comparison.models import Classifier, Metric


class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        # Load classifiers from JSON file
        with open('classifiers.json', 'r') as f:
            classifiers = json.load(f)

        # Load metrics from JSON file
        with open('metrics.json', 'r') as f:
            metrics = json.load(f)

        # Create Classifier objects and save them to the database
        for classifier_data in classifiers:
            classifier = Classifier.objects.create(
                name=classifier_data['name'],
                short_description=classifier_data['short_description'],
                # hyperparameters=classifier_data['hyperparameters'],
                hyperparameters=json.dumps(classifier_data['hyperparameters']),
                ensemble=classifier_data['ensemble']
            )

            classifier.save()

            # Find metrics for the classifier
            for metric_data in metrics:
                if metric_data['classifier_name'] == classifier.name:
                    Metric.objects.create(
                        classifier=classifier,
                        f1_score=metric_data['f1_score'],
                        recall=metric_data['recall'],
                        f2_score=metric_data['f2_score'],
                        balanced_accuracy=metric_data['balanced_accuracy']
                    )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with initial data'))
