from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from training_sheet.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "tags", "course_teachers")


class ContactUsForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Your message subject", "value": "111"}
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message", "value": "2222"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "value": "asdf@asdf.ru"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Send", css_class="btn btn-primary"))
