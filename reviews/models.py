from django.db import models

# Create your models here.
class Professor(models.Model):
    name=models.CharField(max_length=100)

class Course(models.Model):
    name=models.CharField(max_length=100)
    professor=models.ManyToManyField(Professor,blank=True,null=True)
    informative=models.IntegerField()
    need_to_go_to_class=models.IntegerField()
    difficulty=models.IntegerField()
    grade=models.IntegerField()
    no_of_people_reviewed=models.IntegerField(null=True,blank=True)
    short_form_small=models.CharField(max_length=100,null=True,blank=True)
    short_form_capital=models.CharField(max_length=100,null=True,blank=True)
    full_name_with_space_lowercase=models.CharField(max_length=100,null=True,blank=True)
    full_name_with_space_uppercase=models.CharField(max_length=100,null=True,blank=True)
    full_name_with_space_first_letter_capital_for_all_words=models.CharField(max_length=100,null=True,blank=True)

    def save(self, *args, **kwargs):
        naam=self.name
        if "-" in naam:
            lst=naam.split("-")
        else:
            lst=naam.split(" ")
        if not self.short_form_small:
            ele=""
            for h in lst:
                if h!="":
                    ele+=h[0].lower()
            self.short_form_small = ele
        
        if not self.short_form_capital:

            ele=""
            for h in lst:
                if h!="":
                    ele+=h[0].upper()
            self.short_form_capital = ele
        
        if not self.full_name_with_space_lowercase:

            ele=""
            for h in lst:
                ele+=h.lower()
                ele+=" "
            self.full_name_with_space_lowercase = ele[:len(ele)-1]
        
        if not self.full_name_with_space_uppercase:

            ele=""
            for h in lst:
                ele+=h.upper()
                ele+=" "
            self.full_name_with_space_uppercase = ele[:len(ele)-1]
        
        if not self.full_name_with_space_first_letter_capital_for_all_words:

            ele=""
            for h in lst:
                if h!="":
                    ele+=h[0].upper()
                    ele+=h[1:]
                    ele+=" "
            self.full_name_with_space_first_letter_capital_for_all_words = ele[:len(ele)-1]
        
        super(Course, self).save(*args, **kwargs)


class Available_Courses(models.Model):
    name=models.CharField(max_length=100)
    name_slug=models.SlugField(null=True)