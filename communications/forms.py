from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            'full_name',
            'email',
            'phone_number',
            'subject',
            'message',
            'channel'
         ]
    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = 'Enter Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone No'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter Message'
        self.fields['subject'].widget.attrs['placeholder'] = 'Enter Subject'

        for field in ('full_name', 'email', 'phone_number', 'subject', 'message', 'channel'):
            self.fields[field].widget.attrs['class'] = 'form-control'
