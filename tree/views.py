# tree/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Person
from .forms import PersonForm, RelationshipForm
from django.core.serializers.json import DjangoJSONEncoder
import json

def index(request):
    persons = Person.objects.all()
    data = []
    for person in persons:
        data.append({
            'id': person.id,
            'name': person.name,
            'parent_id': person.parent_id,
            'image': person.image.url if person.image else None,
        })
    context = {
        'form': PersonForm(),
        'relationship_form': RelationshipForm(),
        'data': json.dumps(data, cls=DjangoJSONEncoder),
    }
    return render(request, 'index.html', context)

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save()
            return JsonResponse({
                'id': person.id,
                'name': person.name,
                'parent_id': person.parent_id,
                'image': person.image.url if person.image else None,
            })
    return redirect('index')
