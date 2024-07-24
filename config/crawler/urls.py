from django.urls import path
from . import views

urlpatterns = [
    path('', views.crawl_course_info),
]