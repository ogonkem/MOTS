from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Testimony
from .forms import TestimonyForm
from django.contrib import messages

# Create your views here.
class TestimonyView(View):
    template_name = "testimony/testimonies.html"

    def get(self, request, *args, **kwargs):
        form = TestimonyForm()
        testimonies = Testimony.objects.filter(verified=True)[:3].values(
            'first_name',
            'last_name',
            'title',
            'description'
        )

        context = {
            'form': form,
            'testimonies': testimonies,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = TestimonyForm(request.POST)
        if form.is_valid():
            data = Testimony()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.City = form.cleaned_data['City']
            data.State = form.cleaned_data['State']
            data.country = form.cleaned_data['country']
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            data.photo = form.cleaned_data['photo']
            data.save()
            messages.success(request, 'Thank you! Your testimony has been submitted.')
            return redirect("testimonies")
