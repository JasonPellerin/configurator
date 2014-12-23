from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from customer.models import Customer


TITLE_CHOICES = (
        ('MR', 'MR.'),
        ('MRS', 'MRS.'),
        ('MS', 'MS.'),
        ('DR', 'DR.'),
)

TIME_CHOICES = (
        ('1M', '1 Month'),
        ('3M', '3 Months'),
        ('6M', '6 Months'),
        ('1Y', '1 Year'),
        ('NS', 'Not Sure'),
)





class RegistrationForm(ModelForm):
	first_name	= forms.CharField(label=(u'First Name'))
	last_name       = forms.CharField(label=(u'Last Name'))
        title		= forms.ChoiceField(label=(u'Title'), choices=TITLE_CHOICES)
	company_name	= forms.CharField(label=(u'Company Name'))	
	email           = forms.EmailField(label=(u'Email Address'))
        phone		= forms.CharField(label=(u'Phone Number'))
	time_frame	= forms.ChoiceField(label=(u'Time Frame For Purchase'), choices=TIME_CHOICES)
	password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

        class Meta:
                model = Customer
                exclude = ('user',)
                fields = ('first_name', 'last_name', 'title', 'company_name', 'email', 'phone', 'time_frame')
        def clean_username(self):
                email = self.cleaned_data['email']
                try:
                        User.objects.get(email=email)
                except User.DoesNotExist:
                        return email
                raise forms.ValidationError("That email address is already taken, please choose another.")

        def clean(self):
                if self.cleaned_data['password'] != self.cleaned_data['password1']:
                        raise forms.ValidationError("The passwords did not match.  Please try again.")
                return self.cleaned_data

class LoginForm(forms.Form):
        email	        = forms.EmailField(label=(u'Email Address'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

