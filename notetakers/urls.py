from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from colleges.views import home, FilterCourseView

urlpatterns = [
    path('', FilterCourseView.as_view(), name='home'),
    path('apply/', TemplateView.as_view(template_name='Apply.html'), name='apply'),
    path('admin/', admin.site.urls),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
]
