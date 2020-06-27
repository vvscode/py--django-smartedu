from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from training_sheet.models import Course, CustomUser
from registration.forms import RegistrationFormNoFreeEmail, RegistrationFormUniqueEmail


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class ContactUsForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Your message subject"})
    )
    body = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your message"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.add_input(
            Submit("submit", "Send", css_class="btn btn-primary float-right")
        )


class CustomRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]
