from django.urls import path
from . import views

# urlpatterns=[
#     path("",views.index,name="all-meetups"),
#     path("<slug:meetup_slug>/success",views.confirm_registration,name="confirm-registration"),
#     path("<slug:meetup_slug>",views.meetup_details,name="meetup-detail")
    
# ]

urlpatterns = [
    path("reviews/",views.index_page,name="index_page"),
    path("reviews/post_review_page",views.post_review_page,name="post_review_page"),
    path("reviews/submit_post/<slug:slug>",views.submit_post,name="submit_post"),
    path("reviews/single_course_review_page/<slug:course_name_slug>",views.single_course_review_page,name="single_course_review_page"),
    path("reviews/review_of_single_course",views.review_of_single_course,name="review_of_single_course")
]
