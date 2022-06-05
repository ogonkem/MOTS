from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Enquiry
from .forms import EnquiryForm
from django.contrib import messages

# Create your views here.
class EnquiryView(View):
    template_name = "communications/contact_us.html"

    def get(self, request, *args, **kwargs):
        form = EnquiryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = EnquiryForm(request.POST)
        if form.is_valid():
            data = Enquiry()
            data.full_name = form.cleaned_data['full_name']
            data.email = form.cleaned_data['email']
            data.phone_number = form.cleaned_data['phone_number']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.channel = form.cleaned_data['channel']
            data.save()
            messages.success(request, 'Thank you! Your enquiry has been submitted.')
            return redirect("contact_us")