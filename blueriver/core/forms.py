from django import forms
from phone_field import PhoneField
    
# contact us form starts from here..

class ContactInformation(forms.Form):
    name = forms.CharField(label_suffix=" ",widget=forms.TextInput(attrs={"class":"form-control border-info is-valid ","placeholder":"Name"}))
    email = forms.EmailField(label_suffix=" ",widget=forms.EmailInput(attrs={'class':'form-control border-info is-valid', 'placeholder':'Email'}))
    contact = forms.IntegerField(label_suffix=" ", widget=forms.NumberInput(attrs={"class":"form-control border-info is-valid", "placeholder":"Mobile No"}))
    comment = forms.CharField(label_suffix=" ", widget=forms.Textarea(attrs={"class":"form-control border-info is-valid", "placeholder":"Your Question"}), max_length=200)
    address = forms.CharField(label_suffix=" ", widget = forms.TextInput(attrs={'class':'form-control border-info is-valid', 'placeholder':'flat no floor apartment house'}))        
    
