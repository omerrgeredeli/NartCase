from django.urls import path

from . import views
from .views import AirlineViewSet, AirLineGenericView

urlpatterns = [

    path("", views.AirlineViewSet.as_view( {"get": "retrieve", "post": "save_airline"} )),
    path(r'<int:pk>', AirLineGenericView.as_view()),



]
