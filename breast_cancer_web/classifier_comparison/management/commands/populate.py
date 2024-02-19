import json
from django.core.management.base import BaseCommand
from classifier_comparison.models import Classifier, Metric, Feature, Instance
from django.core.files import File
import os


class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        # Load classifiers from JSON file
        with open('classifiers.json', 'r') as f:
            classifiers = json.load(f)

        # Load metrics from JSON file
        with open('metrics.json', 'r') as f:
            metrics = json.load(f)

        categories = ["radius", "texture", "perimeter", "area", "smoothness",
                      "compactness", "concavity", "concave_points", "symmetry", "fractal_dimension"]
        variants = ["mean", "error", "worst"]

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

            classifier_name_no_spaces = classifier.name.replace(' ', '_')

            base_path = f'static/shap_plots/local_analysis/{classifier_name_no_spaces}'

            types = ['benign', 'malignant',
                     'missclassified', 'closest_to_boundary']

            for t in types:
                path = f'{base_path}/{t}'
                imgs = [i for i in os.listdir(path)]
                for img in imgs:
                    img_path = f'{path}/{img}'
                    img_path_no_static = img_path.split('static/')[1]
                    # get the index of the image between _ and .png
                    img_num = int(img.split('_')[1].split('.')[0])
                    instance = Instance.objects.create(
                        name=img,
                        idx=img_num,
                        path=img_path_no_static
                    )
                    instance.save()
                    if t == 'benign':
                        classifier.benign_instances.add(instance)
                    elif t == 'malignant':
                        classifier.malignant_instances.add(instance)
                    elif t == 'missclassified':
                        classifier.missclassified_instances.add(instance)
                    elif t == 'closest_to_boundary':
                        classifier.closest_instances.add(instance)

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

                    metric = Metric.objects.create(
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

                    for category in categories:
                        feature_name = category
                        paths = {}
                        for variant in variants:
                            path = f'shap_plots/single_features/{classifier_name_no_spaces}_{category}_{variant}.png'
                            paths[variant] = path
                        feature = Feature.objects.create(
                            name=feature_name,
                            worst_path=paths['worst'],
                            error_path=paths['error'],
                            mean_path=paths['mean']
                        )
                        feature.save()
                        metric.features.add(feature)

                    # print(f'benign instances: {img_num}')
                    metric.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with initial data'))
