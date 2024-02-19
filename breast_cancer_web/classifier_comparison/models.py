from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import ManyToManyField


class Classifier(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    hyperparameters = models.TextField()
    ensemble = models.BooleanField(default=False)
    malignant_instances = ManyToManyField(
        'Instance', related_name='malignant_metrics')
    benign_instances = ManyToManyField(
        'Instance', related_name='benign_metrics')
    missclassified_instances = ManyToManyField(
        'Instance', related_name='missclassified_metrics')
    closest_instances = ManyToManyField(
        'Instance', related_name='closest_metrics')


class Metric(models.Model):
    classifier = models.ForeignKey(Classifier, on_delete=models.CASCADE)
    f1_score = models.FloatField()
    recall = models.FloatField()
    f2_score = models.FloatField()
    balanced_accuracy = models.FloatField()
    confusion_matrix = models.CharField(max_length=255)
    global_features_plot = models.CharField(max_length=255)
    beeswarm_plot = models.CharField(max_length=255)
    features = ManyToManyField('Feature')


class Feature(models.Model):
    name = models.CharField(max_length=100)
    worst_path = models.CharField(max_length=255)
    error_path = models.CharField(max_length=255)
    mean_path = models.CharField(max_length=255)


class Instance(models.Model):
    name = models.CharField(max_length=100)
    idx = models.IntegerField()
    path = models.CharField(max_length=255)
