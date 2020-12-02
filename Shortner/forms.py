from django import forms
from django.forms import fields
from django.forms.widgets import TextInput
from .models import Input_URL,User
from django.forms import widgets
# class URL_Form(forms.Form):
#     input_form = forms.URLField(label="Enter URL Here", required=True)

class URL_Form(forms.ModelForm):
    name = forms.CharField(required=True,min_length=4,max_length=50 ,label="Name: ", widget=forms.TextInput(attrs={"placeholder":"Enter Your Name Here! "}))
    email = forms.EmailField(required=True,min_length=10,max_length=255, label="Email: ", widget=forms.TextInput(attrs={"placeholder":"Enter Your Email Here!"}))

    class Meta:
        model = Input_URL
        fields = ['name', 'email', 'input_url']
        labels = {'input_url' : "ENTER URL HERE: "}
        widgets = {
            'input_url' : forms.TextInput(attrs={ 'id' : 'input', 'placeholder':'Enter the Greater URL Here!'}),
            
        }
        
    
    

