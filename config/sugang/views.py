from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import *

def main(request):
    course_list = Course.objects.all()

    template = loader.get_template("main.html")
    context = {
        "course_list": course_list,
    }
    return HttpResponse(template.render(context, request))

def get_all_major(request):
    return Major.objects.all()

def get_all_course(request):
    return Course.objects.all()

def search_course(request):
    course_name = request.GET.get('course_name')
    course_code = request.GET.get('course_code')
    if course_name:
        return get_all_course_by_name(request, course_name)
    if course_code:
        return get_all_course_by_code(request, course_code)

    return Major.objects.all()

def get_all_course_by_major(request, major):
    major,_ = Major.objects.get_or_create(name = major)
    course_queryset = Course.objects.filter(major.id)
    template = loader.get_template("main.html")
    context = {
        "course_list": course_queryset
    }
    return HttpResponse(template.render(context, request))

def get_all_course_by_name(request, course_name):
    course_queryset =  Course.objects.filter(name = course_name)
    template = loader.get_template("main.html")
    context = {
        "course_list": course_queryset
    }
    return HttpResponse(template.render(context, request))

def get_all_course_by_code(request, course_code):
    course_queryset = Course.objects.filter(code = course_code)
    template = loader.get_template("main.html")
    context = {
        "course_list": course_queryset
    }
    return HttpResponse(template.render(context, request))
