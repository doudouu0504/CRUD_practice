from django.urls import path
from .views import home, new, show, edit, delete

app_name = "resumes"

urlpatterns = [
    path("", home, name="home"),
    path("new", new, name="new"),
    path("<int:id>", show, name="show"),
    path("<int:id>/edit", edit, name="edit"),
    path("<int:id>/delete", delete, name="delete"),
]
