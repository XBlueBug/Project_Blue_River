from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
# from .models import Customer

# contact us form starts from here..

class ContactInformation(forms.Form):
    name = forms.CharField(label_suffix=" ", widget=forms.TextInput(attrs={"class":"form-control border-info is-valid ","placeholder":"Name"}))
    email = forms.EmailField(label_suffix=" ", widget=forms.EmailInput(attrs={'class':'form-control border-info is-valid', 'placeholder':'Email'}))
    contact = PhoneNumberField(label_suffix=" ", widget=forms.NumberInput(attrs={"class":"form-control border-info is-valid", "placeholder":"Mobile No eg +923001234567"}))
    comment = forms.CharField(label_suffix=" ", widget=forms.Textarea(attrs={"class":"form-control border-info is-valid", "placeholder":"Your Question"}), max_length=200)
    address = forms.CharField(label_suffix=" ", widget = forms.TextInput(attrs={'class':'form-control border-info is-valid blackText', 'placeholder':'flat no floor apartment house'}))        
    
    # def clean(Self): 
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     valcontact = self.cleaned_data['contact']
    #     valcomment = self.cleaned_data['comment']
    #     valaddress = self.cleaned_data['address']

    #     if len(valname) < 4:
    #         raise forms.ValidationError('Name should be more then or equal to 4')

    #     if len(valemail) < 7:
    #         raise forms.ValidationError('Email should be in proper manner')
        

    #     if len(valcontact) < 13:
    #         raise forms.ValidationError('Number should writen in this patren +92 xxx xxxxxxx')

    #     if len(valaddress) < 8:
    #         raise forms.ValidationError(' Please Enter Address in detail')
      

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', label_suffix=" ", widget=forms.PasswordInput(attrs={"class":"form-control border-info is-valid ",'placeholder':'Password'}),)
    password2 = forms.CharField(label='Confirm Password',label_suffix=" ", widget=forms.PasswordInput(attrs={"class":"form-control border-info is-valid ",'placeholder':'Password(again)'}),)
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets={
            'first_name':forms.TextInput(attrs={"class":"form-control border-info is-valid ","placeholder":"First Name"}),
            'last_name' :forms.TextInput(attrs={"class":"form-control border-info is-valid ","placeholder":"Last Name"}),
            'username'  :forms.TextInput(attrs={"class":"form-control border-info is-valid ","placeholder":"@Username"}),
            'email'     :forms.EmailInput(attrs={"class":"form-control border-info is-valid", "placeholder":"Email Address"}),
            }    


class UserLoginForm(AuthenticationForm):
    username    = UsernameField(widget=forms.TextInput(attrs={'autofoucus':True, "class":"form-control border-info is-valid ",'placeholder':'Username'}),)
    password = forms.CharField(label_suffix=" ", label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', "class":"form-control border-info is-valid ",'placeholder':'Password'}),)


# class CustomerProfileForm(forms.ModelForm): 
#     class Meta:
#         model = Customer
#         fields = ['name', 'address', 'area' 'city']
#         widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 
#         'address':forms.TextInput(attrs={'class':'form-control'}), 
#         'area':forms.TextInput(attrs={'class':'form-control'}), 
#         'city':forms.TextInput(attrs={'class':'form-control'})}

       
