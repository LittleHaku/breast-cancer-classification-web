from .models import Classifier, Metric
from django.shortcuts import render, get_object_or_404
import ast
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Classifier


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

        context = {
            'classifier1': classifier1,
            'classifier2': classifier2,
            'metrics': metrics,
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

    return render(request, 'classifier_detail.html', {'classifier': classifier, 'metrics': metrics})
