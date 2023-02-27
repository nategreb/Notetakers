import django_filters

from .models import Course


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['course_name', 'department', 'course_id']
