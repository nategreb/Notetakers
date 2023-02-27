from django.db import models

from colleges.models import Course


class Notetaker(models.Model):
    email = models.EmailField(unique=True)
    notes_example = models.URLField(null=True, blank=True)
    study_guide_example = models.URLField(null=True, blank=True)
    cheat_sheet_example = models.URLField(null=True, blank=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.email


    # TODO: track the number of hits.
    # https://stackoverflow.com/questions/1603340/track-the-number-of-page-views-or-hits-of-an-object
