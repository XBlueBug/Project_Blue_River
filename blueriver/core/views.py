from django.shortcuts import render
from .forms import ContactInformation
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def show_contact_info(request):
    cfm = ContactInformation(auto_id='customer_%s', label_suffix=" ")
    return render(request, 'core/contactus.html',{'form':cfm})
