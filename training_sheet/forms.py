from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from training_sheet.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "tags", "course_teachers")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))
