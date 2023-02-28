from django.db import models
from slugify import slugify
from django.urls import reverse

from .departments import Department
from .colleges import College

"""
    One to Many relation of Colleges to Courses
"""


class Course(models.Model):
    class Meta:
        # can have same course at different levels
        constraints = [
            models.UniqueConstraint(fields=['college', 'course_id'],
                                    name='secondary_course_id_key')

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
    )
    course_id = models.CharField(
        max_length=15,
        verbose_name='Course ID'
    )
    course_name = models.CharField(
        max_length=90,
        verbose_name='Course Name'
    )
    slug = models.SlugField(max_length=90, blank=True, null=False)

    def __str__(self):
        return f'{self.course_id} {self.course_name}'

    # add slug by converting white spaces to hyphens
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.course_name}')
        # call full clean to validate
        self.full_clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('colleges:course', kwargs={'course_id': self.id, 'course_slug': self.slug})
