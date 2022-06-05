from django import forms
from .models import Testimony

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'City',
            'State',
            'country',
            'title',
            'description',
            'photo'
         ]
    def __init__(self, *args, **kwargs):
        super(TestimonyForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone No'
        self.fields['City'].widget.attrs['placeholder'] = 'Enter City'
        self.fields['State'].widget.attrs['placeholder'] = 'Enter State'
        self.fields['country'].widget.attrs['placeholder'] = 'Enter country'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Testimony Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe Testimony'
        self.fields['photo'].widget.attrs['placeholder'] = 'Upload Image'

        for field in ('first_name', 'last_name', 'email', 'phone','City','State','country','title','description','photo'):
            self.fields[field].widget.attrs['class'] = 'form-control'
