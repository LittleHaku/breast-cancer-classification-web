from django.shortcuts import render, get_object_or_404
import ast
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Classifier, Feature, Metric, Instance


def home(request):
    return render(request, 'home.html')


def compare_classifiers(request):
    if request.method == 'POST':
        # Form submission handling
        classifier1_id = request.POST.get('classifier1')
        classifier2_id = request.POST.get('classifier2')

        classifier1 = Classifier.objects.get(id=classifier1_id)
        classifier2 = Classifier.objects.get(id=classifier2_id)

        metrics1 = Metric.objects.filter(classifier=classifier1)
        metrics2 = Metric.objects.filter(classifier=classifier2)

        # Pair up the metrics for the two classifiers
        metrics = zip(metrics1, metrics2)

        # Pair up features too
        features1 = Feature.objects.filter(metric__classifier=classifier1)
        features2 = Feature.objects.filter(metric__classifier=classifier2)
        features = zip(features1, features2)

        context = {
            'classifier1': classifier1,
            'classifier2': classifier2,
            'metrics': metrics,
            'features': features
        }

        return render(request, 'classifier_comparison_results.html', context)

    else:
        # Fetch all classifiers from the database
        classifiers = Classifier.objects.all()
        return render(request, 'compare_classifiers.html', {'classifiers': classifiers})


def classifier_list(request):
    classifiers = Classifier.objects.all()

    # Separate classifiers into two lists based on whether they are ensemble classifiers or base classifiers
    ensemble_classifiers = classifiers.filter(ensemble=True)
    base_classifiers = classifiers.filter(ensemble=False)

    return render(request, 'classifier_list.html', {'ensemble_classifiers': ensemble_classifiers, 'base_classifiers': base_classifiers})


def classifier_detail(request, pk):
    classifier = get_object_or_404(Classifier, pk=pk)
    # Convert the string representation of hyperparameters into a dictionary
    classifier.hyperparameters = json.loads(classifier.hyperparameters)
    # Get the metrics associated with the classifier
    metrics = Metric.objects.filter(classifier=classifier)
    # Get the features associated with the classifier
    features = Feature.objects.filter(metric__classifier=classifier)

    # Get benign, malignant, missclassified and closest_to_boundary instances for the classifier
    benign_instances = classifier.benign_instances.all()
    malignant_instances = classifier.malignant_instances.all()
    missclassified_instances = classifier.missclassified_instances.all()
    closest_instances = classifier.closest_instances.all()

    context = {
        'classifier': classifier,
        'metrics': metrics,
        'features': features,
        'benign_instances': benign_instances,
        'malignant_instances': malignant_instances,
        'missclassified_instances': missclassified_instances,
        'closest_instances': closest_instances
    }

    for inst in malignant_instances:
        print(inst)

    return render(request, 'classifier_detail.html', context)
