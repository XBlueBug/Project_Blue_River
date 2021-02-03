from django import forms
from phonenumber_field.formfields import PhoneNumberField
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
      
        



class User_Registration_Form(forms.Form):
    first_name = forms.CharField(max_length=20, label_suffix=" ", widget=forms.TextInput(attrs={"class":"form-control border-info is-valid ","placeholder":"First Name"}))
    last_name  = forms.CharField(max_length=20, label_suffix=" ", widget=forms.TextInput(attrs={"class":"form-control border-info is-valid ","placeholder":"Last Name"}))
    email      = forms.EmailField(max_length=100, label_suffix=" ", widget=forms.EmailInput(attrs={"class":"form-control border-info is-valid", "placeholder":"Email Address"}))
    address    = forms.CharField(max_length=200, label_suffix=" ", widget = forms.TextInput(attrs={'class':'form-control border-info is-valid blackText', 'placeholder':'Flat/House no Floor/Street Area'}))
    contact    = PhoneNumberField(label_suffix=" ", widget = forms.NumberInput(attrs={'class':'form-control border-info is-valid blackText', 'placeholder':'Mobile No eg +923001234567'}))
    password   = forms.CharField(max_length=14, label_suffix=" ", widget = forms.PasswordInput(attrs={'class':'form-control border-info is-valid blackText', 'placeholder':'Password'}))    
    re_enter_password = forms.CharField(max_length=14, label_suffix=" ", widget = forms.PasswordInput(attrs={'class':'form-control border-info is-valid blackText', 'placeholder':'Password'}))
