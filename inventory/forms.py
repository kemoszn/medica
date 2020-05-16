from django import forms 
from .models import State, Hospital

class StateCreationForm(forms.ModelForm):
        class Meta:
                model = State
                fields = ('name',)

class HospitalCreationForm(forms.ModelForm):
        class Meta:
                model = Hospital
                fields = ('name','owner','state',)