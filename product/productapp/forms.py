from django import forms
from .models import customer_details
 
 

class customer_detailsForm(forms.ModelForm):
 
    
    class Meta:
        model = customer_details
 
       
        fields = [
            "name",
            "location",
            "email",
            "phonenumber",
            "status",
        ]