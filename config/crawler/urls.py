from django.urls import path
from . import views

urlpatterns = [
    path('', views.crawl_course_info),
    path('course/vacancy', views.crawl_course_vacancy),
]