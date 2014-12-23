
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from customer.forms import RegistrationForm, LoginForm
from customer.models import Customer
from django.contrib.auth import authenticate, login, logout

def CustomerRegistration(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        user = User.objects.create_user( username= form.cleaned_data['email'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
                        user.save()
                        customer = Customer(user=user, first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], title=form.cleaned_data['title'], phone=form.cleaned_data['phone'], time_frame=form.cleaned_data['time_frame'])
                        customer.save()
                        return HttpResponseRedirect('/profile/')
                else:
                        return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form}
                return render_to_response('register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        email = form.cleaned_data['email']
                        password = form.cleaned_data['password']
                        customer = authenticate(email=email, password=password)
                        if customer is not None:
                                login(request, customer)
                                return HttpResponseRedirect('/profile/')
                        else:
                                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/')

@login_required
def UserProfile(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')
        customer 	= request.user.profile.email
        first_name 	= request.user.profile.first_name
        last_name	= request.user.profile.last_name
	title		= request.user.profile.title
#	company_name	= request.user.profile.company_name
	email		= request.user.profile.email
	phone		= request.user.profile.phone
	time_frame	= request.user.profile.time_frame
        context 	= {'customer': customer}
        return render_to_response('profile.html', context, context_instance=RequestContext(request))

