from django.shortcuts import render
from .forms import ContactInformation, UserRegistrationForm, UserLoginForm
from .models import Contact
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout

  
# views Start from here
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about/about.html')

def thankyou(request):
    return render(request, 'core/contactus/cfm_success.html')

def show_contact_info(request):
    if request.method == 'POST':
        cfm = ContactInformation(request.POST)
        if cfm.is_valid():
            print('This Is POST Method')
            nm   = cfm.cleaned_data['name']
            em   = cfm.cleaned_data['email']
            cont = cfm.cleaned_data['contact']
            add  = cfm.cleaned_data['address']
            cmt  = cfm.cleaned_data['comment']
            con  = Contact(name=nm, email=em, contact=cont, address=add, comment=cmt)
            con.save()
            return HttpResponseRedirect('/success/')
    else:
        cfm = ContactInformation()
        print('This is GET method')    
    return render(request, 'core/contactus/contactus.html', {'form':cfm})

def user_reg(request):
    if request.method == 'POST':
        urfm = UserRegistrationForm(request.POST) 
        if urfm.is_valid():
            urfm.save()
            messages.success(request, 'Account Created Sucessfully...!!!')
            return HttpResponseRedirect('/success/')
    else:
        urfm = UserRegistrationForm()
    return render(request, 'core/registration/registration.html', {'reg_form': urfm})            
 

                    #     login views starts from here..


def user_login(request):
    if request.method == 'POST':
        ulfm = UserLoginForm(request=request, data=request.POST)
        if ulfm.is_valid():
            uname = ulfm.cleaned_data['username']
            upass = ulfm.cleaned_data['password']
            user  = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully...!!!')
                return HttpResponseRedirect('/profile/')
    else:
        ulfm = UserLoginForm()
    return render(request, 'core/registration/login.html', {'logfm': ulfm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

                        # Profile views start from here..!!


class UserProfile(View):
    def get(self, request):
        form =CustomerProfileForm()
        return render(request, 'core/profiles/profile.html', {'form':form, 'active':'btn-primery'})
    def post(self, request):
        form =CustomerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/profiles/profile.html', {'form':form, 'active':'btn-primery'})


