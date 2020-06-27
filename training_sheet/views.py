from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.views import View
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from training_sheet.forms import CourseForm, ContactUsForm
from training_sheet.jobs.send_contact_us_email import send_contact_us_email
from training_sheet.models import Course


class CoursesListClassView(ListView):
    model = Course
    context_object_name = "courses"
    paginate_by = 5

    queryset = Course.objects.prefetch_related("tags")


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


class SoftRedirectView(TemplateView):
    template_name = "training_sheet/soft_redirect.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"data": self.request.session.get("soft_redirect_data", {})})
        context.update(
            {"timeout": self.request.session.get("soft_redirect_timeout", 3)}
        )
        context.update(
            {"target_url": self.request.session.get("soft_redirect_target_url", "/")}
        )
        context.update(
            {
                "message": self.request.session.get(
                    "soft_redirect_message", "Thanks for you activity"
                )
            }
        )

        return context


class ContactUsView(View):
    def get(self, request):
        return render(
            request, "training_sheet/contact_us.html", context={"form": ContactUsForm()}
        )

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            send_contact_us_email(**form_data)

            request.session["soft_redirect_message"] = "Thanks for your message"
            request.session["soft_redirect_data"] = form_data

            return redirect("trainging_sheet.soft_redirect")

        return render(request, "training_sheet/contact_us.html", context={"form": form})


class AjaxRegistrationView(TemplateView):
    template_name = "training_sheet/ajax-registration.html"
