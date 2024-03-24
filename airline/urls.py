from django.urls import path

from . import views
from .views import GetUpdateAirline, AirlineListView,UpdateAirline

urlpatterns = [
    path("", views.CreateAirline.as_view()),
    path('<int:pk>',UpdateAirline.as_view()),
    path("index2", views.index2, name="index2"),
    path('listall', AirlineListView.as_view()),
]

""" TO DO"""