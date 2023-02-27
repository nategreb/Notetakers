from django import forms

from colleges.models import RequestCourse
# from templates.django.forms.fields import DatalistField
# from templates.django.forms.widgets import CustomDataList
#
#
# class SearchForm(forms.Form):
#     search = DatalistField(widget=CustomDataList(attrs={'class': 'autoComplete'}))


class RequestCourseForm(forms.ModelForm):
    class Meta:
        model = RequestCourse
        fields = ['college', 'department', 'course_id', 'course_name']

    def clean(self):
        cleaned_data = super(RequestCourseForm, self).clean()
        # string cleanup
        cleaned_data['course_id'] = cleaned_data['course_id'].upper()
        cleaned_data['course_name'] = cleaned_data['course_name'].lower()
        return cleaned_data

