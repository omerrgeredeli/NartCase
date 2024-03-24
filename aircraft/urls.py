from django.urls import path

from .views import CreateAirCraft, GenericAirCraftView

urlpatterns = [

    path("", CreateAirCraft.as_view()),
    path(r'<int:pk>', GenericAirCraftView.as_view()),


]
