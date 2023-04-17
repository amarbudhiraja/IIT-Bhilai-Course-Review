from django import forms
from .models import Course,Professor

class post_form(forms.ModelForm):
    class Meta:
        model=Course
        exclude=["name","short_form_small","short_form_capital","full_name_with_space_lowercase","full_name_with_space_uppercase","full_name_with_space_first_letter_capital_for_all_words"]

