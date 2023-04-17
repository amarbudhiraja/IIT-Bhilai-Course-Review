from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import post_form

# Create your views here.

from .models import Course,Professor,Available_Courses

def index_page(request):
    courses=Course.objects.all()
    return render(request,"reviews/index_page.html",{
        "courses":courses
    })

def post_review_page(request):
    available_courses=Available_Courses.objects.all()
    return render(request,"reviews/post_review_page.html",{
        "post_form":post_form,
        "available_courses":available_courses
    })

def combining_average(prev_avg,no,cur_no):
    sum=prev_avg*no
    sum+=cur_no
    ans=sum/(no+1)
    return ans

def submit_post(request,slug):
    form=post_form(request.POST)
    # print(request.POST)
    course_name=slug
    # a=Course.objects.filter(name=course_name)
    # print(a[0])
    try:
        a=Course.objects.filter(name=course_name)
        course_row=a[0]
        if (form.is_valid()):
            course_row.informative=combining_average(course_row.informative,course_row.no_of_people_reviewed,int(request.POST["informative"]))
            course_row.need_to_go_to_class=combining_average(course_row.need_to_go_to_class,course_row.no_of_people_reviewed,int(request.POST["need_to_go_to_class"]))
            course_row.difficulty=combining_average(course_row.difficulty,course_row.no_of_people_reviewed,int(request.POST["difficulty"]))
            course_row.grade=combining_average(course_row.grade,course_row.no_of_people_reviewed,int(request.POST["grade"]))
            
            course_row.save()
            return render(request,"reviews/post_success_page.html")
        return render(request,"reviews/single_course_review_page.html")
        
    except:
        if (form.is_valid()):
            
            req=form.save()
            req.name=course_name
            req.save()
            
            return render(request,"reviews/post_success_page.html")
        return render(request,"reviews/single_course_review_page.html")


def single_course_review_page(request,course_name_slug):
    return render(request,"reviews/single_course_review_page.html",{
        "course_name_slug":course_name_slug,
        "post_form":post_form
    })



def review_of_single_course(request):
    searched_name=request.POST["course"]
    course_row=-1

    if len(Course.objects.filter(short_form_small=searched_name))>0:
        course_row=Course.objects.filter(short_form_small=searched_name)[0]
    elif len(Course.objects.filter(short_form_capital=searched_name))>0:
        course_row=Course.objects.filter(short_form_capital=searched_name)[0]
    elif len(Course.objects.filter(full_name_with_space_lowercase=searched_name))>0:
        course_row=Course.objects.filter(full_name_with_space_lowercase=searched_name)[0]
    elif len(Course.objects.filter(full_name_with_space_uppercase=searched_name))>0:
        course_row=Course.objects.filter(full_name_with_space_uppercase=searched_name)[0]
    elif len(Course.objects.filter(full_name_with_space_first_letter_capital_for_all_words=searched_name))>0:
        course_row=Course.objects.filter(full_name_with_space_first_letter_capital_for_all_words=searched_name)[0]
    
    if course_row==-1:
        return HttpResponse("Sorry! This Course doesn't exist. Please enter a valid course name.")
    # print(course_row.name)
    return render(request,"reviews/review_of_single_course.html",{
        "course_row":course_row
    })