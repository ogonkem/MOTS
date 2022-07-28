from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Enquiry
from .forms import EnquiryForm
from django.contrib import messages

# Admin Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

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
            messages.success(request, 'Thank you! Your enquiry would be attended to shortly.')

            # Admin EMAIL
            current_site = get_current_site(request)
            mail_subject = f'{data.full_name} contacted you on {current_site} '
            message = render_to_string('communications/communication_email.html', {
                'name': data.full_name,
                'email': data.email,
                'phone': data.phone_number,
                'subject': data.subject,
                'message': data.message,
                'domain': current_site
            })
            to_email = 'evangelistopn@gmail.com'
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            return redirect("contact_us")