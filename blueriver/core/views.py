from django.shortcuts import render
from .forms import ContactInformation
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
        cfm = ContactInformation(request.POST, auto_id=True)
        if cfm.is_valid():
            print('This Is POST Method')
            print('Name:', cfm.cleaned_data['name'])
            print('Email:', cfm.cleaned_data['email'])
            print('Contact No:', cfm.cleaned_data['contact'])
            print('Address:', cfm.cleaned_data['address'])
            print('Comment:', cfm.cleaned_data['comment'])
            return HttpResponseRedirect('/success/')
    else:
        cfm = ContactInformation()
        print('This is GET method')    
    return render(request, 'core/contactus/contactus.html', {'form':cfm})
