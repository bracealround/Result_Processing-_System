from django.urls import path
from . import views


# URLconf
urlpatterns = [
    path("", views.home_view, name="home"),
    path("students/", views.students_view, name="students"),
    path("teachers/", views.teachers_view, name="teachers"),
    path("results/", views.results_view, name="result"),
    path("results/edit", views.edit_results_view, name="edit-results"),
]
