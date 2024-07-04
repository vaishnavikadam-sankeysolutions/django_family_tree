from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm, RelationshipForm
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    form = PersonForm()
    relationship_form = RelationshipForm()
    persons = Person.objects.all()
    data = json.dumps([{
        'id': p.id,
        'name': p.name,
        'image': p.image.url if p.image else '',
        'parent_id': p.parent_id,
        'children_ids': p.children_ids,
        'spouse_id': p.spouse_id
    } for p in persons], cls=DjangoJSONEncoder)
    return render(request, 'index.html', {'form': form, 'relationship_form': relationship_form, 'data': data})

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        relationship_form = RelationshipForm(request.POST)
        if form.is_valid() and relationship_form.is_valid():
            new_person = form.save()
            relationship = relationship_form.cleaned_data['relationship']
            related_person = relationship_form.cleaned_data['related_person']

            if relationship == 'parent':
                related_person.parent = new_person
                related_person.save()
            elif relationship == 'spouse':
                new_person.spouse = related_person
                new_person.save()
            elif relationship == 'child':
                new_person.parent = related_person
                new_person.save()

            return redirect('index')
    return redirect('index')
