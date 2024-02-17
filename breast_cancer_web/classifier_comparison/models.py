from django.db import models


class Classifier(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    hyperparameters = models.TextField()
    ensemble = models.BooleanField(default=False)


class Metric(models.Model):
    classifier = models.ForeignKey(Classifier, on_delete=models.CASCADE)
    f1_score = models.FloatField()
    recall = models.FloatField()
    f2_score = models.FloatField()
    balanced_accuracy = models.FloatField()
    confusion_matrix = models.CharField(max_length=255)
    global_features_plot = models.CharField(
        max_length=255)
    beeswarm_plot = models.CharField(max_length=255)
