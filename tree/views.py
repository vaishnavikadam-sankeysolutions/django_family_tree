from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    form = PersonForm()
    persons = Person.objects.all()
    data = json.dumps([{
        'id': p.id,
        'name': p.name,
        'image': p.image.url if p.image else '',
        'parent_id': p.parent_id
    } for p in persons], cls=DjangoJSONEncoder)
    return render(request, 'index.html', {'form': form, 'data': data})

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return redirect('index')
