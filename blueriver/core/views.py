from django.shortcuts import render
from .forms import ContactInformation, User_Registration_Form 
from .models import User_Registration, Contact
from django.http import HttpResponseRedirect
# Create your views here.
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
        urfm = User_Registration_Form(request.POST) 
        if urfm.is_valid():
            print('This Is POST Method')
            fnm  = urfm.cleaned_data['first_name']
            l_nm = urfm.cleaned_data['last_name']
            em   = urfm.cleaned_data['email']
            add  = urfm.cleaned_data['address']
            con  = urfm.cleaned_data['contact']
            pwd  = urfm.cleaned_data['password']
            r_pwd= urfm.cleaned_data['re_enter_password']
            user = User_Registration(first_name=fnm, last_name=l_nm, email=em, address=add, contact=con, password=pwd, re_enter_password=r_pwd)
            user.save()
            return HttpResponseRedirect('/success/')
    else:
        urfm = User_Registration_Form()
    return render(request, 'core/registration/registration.html', {'reg_form': urfm})            
