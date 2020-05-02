from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from training_sheet.forms import CourseForm
from training_sheet.models import Course


class CoursesListClassView(ListView):
    model = Course
    context_object_name = "courses"
    paginate_by = 5


class CourseClassView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    fields = "__all__"
    form = CourseForm

    def get_success_url(self):
        return reverse("training_sheet.course", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit("submit", "Create", css_class="btn-primary"))
        return form


class CourseEditView(UpdateView):
    model = Course
    fields = "__all__"
    form = CourseForm

    def get_success_url(self):
        return reverse("training_sheet.course", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit("submit", "Save", css_class="btn-primary"))
        return form


class CourseDeleteClassView(DeleteView):
    model = Course

    # success_url = reverse("training_sheet.index")
    # Leads to django.core.exceptions.ImproperlyConfigured: The included URLconf 'smartedu.urls' does not appear to have any patterns in it
    def get_success_url(self):
        return reverse("training_sheet.index")
