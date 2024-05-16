from django.shortcuts import render
from .models import *

def get_all_major(request):
    return Major.objects.all()

def get_all_course_by_major(request, major):
    major,_ = Major.objects.get_or_create(name = major)
    course_queryset = Course.objects.filter(major.id)
    return course_queryset

def get_all_course_by_evaluation_method(request, evaluation_method):
    return Course.objects.filter(evaluation_method = evaluation_method)

def get_all_course_by_course_time(request, day_of_weeks, period):
    return Course.objects.filter(day_of_weeks = day_of_weeks, period = period)
