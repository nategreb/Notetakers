"""
    get all classes for the college
"""
from django.shortcuts import render, get_object_or_404

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from colleges.models.courses import Course
from .tables import CourseTable
from .filter import CourseFilter


def home(request):
    # as of now, all umass courses
    courses = Course.objects.all()
    return render(request, 'MVP.html', {'courses': courses})


class FilterCourseView(SingleTableMixin, FilterView):
    table_class = CourseTable
    model = Course
    template_name = "MVP.html"

    filterset_class = CourseFilter
    paginate_by = 12


def view_course(request, course_id, course_slug):
    # get notetakers in this speciifc class
    course = get_object_or_404(Course, pk=course_id)
    notetakers = course.notetaker_set.all()
    return render(request, 'courses/CourseProfile.html', {'course': course, 'notetakers': notetakers})
