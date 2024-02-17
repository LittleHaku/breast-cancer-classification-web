import json
from django.core.management.base import BaseCommand
from classifier_comparison.models import Classifier, Metric
from django.core.files import File


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
                hyperparameters=json.dumps(
                    classifier_data['hyperparameters']),
                # hyperparameters=json.dumps(classifier_data['hyperparameters']),
                ensemble=classifier_data['ensemble']
            )

            classifier.save()

            # Find metrics for the classifier
            for metric_data in metrics:
                if metric_data['classifier_name'] == classifier.name:
                    classifier_name_no_spaces = classifier.name.replace(
                        ' ', '_')
                    confusion_matrix_filename = f'cm_{classifier_name_no_spaces}.png'
                    confusion_matrix_path = f'confusion_matrices/{confusion_matrix_filename}'
                    global_features_plot_filename = f'shap_plots/global/bar_{classifier_name_no_spaces}.png'
                    beeswarm_plot_filename = f'shap_plots/global/beeswarm_{classifier_name_no_spaces}.png'

                    Metric.objects.create(
                        classifier=classifier,
                        f1_score=format(metric_data['f1_score'], '.4f'),
                        recall=format(metric_data['recall'], '.4f'),
                        f2_score=format(metric_data['f2_score'], '.4f'),
                        balanced_accuracy=format(
                            metric_data['balanced_accuracy'], '.4f'),
                        # store the image file name
                        confusion_matrix=confusion_matrix_path,
                        global_features_plot=global_features_plot_filename,
                        beeswarm_plot=beeswarm_plot_filename
                    )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with initial data'))
