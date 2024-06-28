from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.bern_index, name="bern_index"),
]