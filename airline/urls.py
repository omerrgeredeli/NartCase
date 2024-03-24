from django.urls import path

from . import views
from .views import ListAirlineView, AirLineGenericView

urlpatterns = [

    path("", views.CreateAirlineView.as_view(http_method_names=["post"]), name="airline-create"),
    path("list/", views.ListAirlineView.as_view(http_method_names=["get"]), name="airline-listall"),
    path(r'<int:pk>', AirLineGenericView.as_view()),



]
