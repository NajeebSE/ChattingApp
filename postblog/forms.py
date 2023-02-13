from django import forms
from . models import user_post



class editForm(forms.ModelForm):
    class Meta:
        model = user_post
        fields = ['title', 'dsc']