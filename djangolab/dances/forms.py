from django import forms

from .models import Dancer, Dance

class DancerForm(forms.ModelForm):
    class Meta:
        model = Dancer
        fields = ['name', 'surname', 'contact']

class DanceForm(forms.ModelForm):
    class Meta:
        model = Dance
        fields=['type','comment']