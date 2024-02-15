"""
URL configuration for breast_cancer_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from classifier_comparison.views import home, compare_classifiers, classifier_list, classifier_detail

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path('', home, name='home'),
    path('compare/', compare_classifiers, name='compare_classifiers'),
    path('classifiers/', classifier_list, name='classifier_list'),
    path('classifiers/<int:pk>/', classifier_detail,
         name='classifier_detail'),  # Add this line


]
