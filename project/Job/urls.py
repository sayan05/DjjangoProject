from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='View Page'),
    path('Jobs/',views.JobList.as_view())
]
