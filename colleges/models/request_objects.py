from django.db import models
from colleges.models import College, Department


class RequestCourse(models.Model):
    # Stores user requests to add specific courses
    class Meta:
        # can have same course at different levels
        constraints = [
            models.UniqueConstraint(fields=['college', 'course_id'],
                                    name='secondary_course_id_key_request_course')
        ]

    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        # don't allow deletion of department if referenced
    )
    course_id = models.CharField(
        max_length=15,
        verbose_name='unique ID of the course'
    )
    course_name = models.CharField(
        max_length=90,
        verbose_name='name of course'
    )

    def __str__(self):
        return f'{self.course_name} - {self.college} - {self.department}'
