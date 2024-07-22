from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('/course/all', views.get_all_course, name="all_course"),
    path('/course/search', views.search_course, name="search_course"),
]