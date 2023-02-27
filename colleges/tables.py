import django_tables2 as tables
from .models import Course


class CourseTable(tables.Table):
    class Meta:
        model = Course
        template_name = "Table.html"
        fields = ("course_id", "course_name", "department", )

