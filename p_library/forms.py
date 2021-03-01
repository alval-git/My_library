from django import forms  
from p_library.models import author   
class AuthorForm(forms.ModelForm):  
    class Meta:  
        model = author  
        fields = '__all__'

