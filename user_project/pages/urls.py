from django.urls import path
from . import views

urlpatterns = [
    path("about/new_page/", views.about_view, name="new_page"),
]