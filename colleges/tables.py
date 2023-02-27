import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from django_tables2.utils import A
from .models import Course


class CourseTable(tables.Table):
    class Meta:
        model = Course
        template_name = "Table.html"
        fields = ("course_id", "course_name", "department", )

    course_id = tables.Column(linkify=lambda record: record.get_absolute_url())
    course_name = tables.Column(linkify=lambda record: record.get_absolute_url())
    department = tables.Column(linkify=lambda record: record.get_absolute_url())
