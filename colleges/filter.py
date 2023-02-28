import django_filters

from .models import Course


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'department', ]
    # icontains django function for lookup expressions
    course_id = django_filters.CharFilter(lookup_expr='icontains')
    course_name = django_filters.CharFilter(lookup_expr='icontains')

