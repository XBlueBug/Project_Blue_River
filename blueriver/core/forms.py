from django import forms
    
# contact us form starts from here..

class ContactInformation(forms.Form):
    name = forms.CharField(max_length=70, required=True, label_suffix=":")
    email = forms.EmailField(max_length=100, required=False)
    contact_no = forms.IntegerField(required=True)
    comment = forms.CharField(widget=forms.Textarea, max_length=500, required=False,)
    
