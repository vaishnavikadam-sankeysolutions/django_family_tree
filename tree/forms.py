# tree/forms.py

from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'image']

class RelationshipForm(forms.Form):
    RELATIONSHIP_CHOICES = [
        ('parent', 'Parent'),
        ('spouse', 'Spouse'),
        ('child', 'Child'),
    ]
    relationship = forms.ChoiceField(choices=RELATIONSHIP_CHOICES)
    related_person = forms.ModelChoiceField(queryset=Person.objects.all(), empty_label="Select a person")