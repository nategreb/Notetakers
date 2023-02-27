"""
    get all classes for the college
"""
from django.http import HttpResponse


# from django.contrib import messages
# from django.core.paginator import Paginator
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse
#
#
# def college_course(request, college_id, course_id, college_slug=None, course_slug=None):
#     """
#         get the profile for a given class
#     """
#     try:
#         course = CollegeCourse.objects.get(id=course_id)
#         professors = course.professor_set.all()
#         reviews = get_reviews(course)
#         paginate = Paginator(reviews, 15)  # show 15 reviews per page
#         page_number = request.GET.get('page')
#         page_obj = paginate.get_page(page_number)
#     except CollegeCourse.DoesNotExist:
#         # add a one-time notification of the cause of failure
#         messages.add_message(
#             request, messages.ERROR,
#             'This specific course doesn\'t exist'
#         )
#         raise ImmediateHttpResponse(HttpResponseRedirect(reverse('colleges:courses')))
#     return render(
#         request, 'courses/CourseProfile.html',
#         {
#             'college_id': college_id,
#             'college_slug': college_slug,
#             'course': course,
#             'page_obj': page_obj,
#             'professors': professors
#         }
#     )

def home(request):
    return HttpResponse('test')
