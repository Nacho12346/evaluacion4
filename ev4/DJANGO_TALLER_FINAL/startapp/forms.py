from django import forms
from startapp.models import Inscritos

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = '__all__'