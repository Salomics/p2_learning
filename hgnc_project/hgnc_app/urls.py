from django.urls import path
from hgnc_project.hgnc_app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("search/", search, name="search"),
]