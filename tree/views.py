from django.shortcuts import render, redirect
from .models import Person, Relationship
from .forms import PersonForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

def add_initial_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonForm()
    return render(request, 'add_initial_person.html', {'form': form})

def home(request):
    print('test')
    persons = Person.objects.all()
    relationships = Relationship.objects.all()
    print(persons)
    return render(request, 'home.html', context={'persons': persons, 'relationships': relationships})

@csrf_exempt
def add_person_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        birth_date = data.get('birth_date')
        image_url = data.get('image')
        relationship_type = data.get('relationshipType')
        from_person_id = data.get('fromPersonId')

        if name and relationship_type and from_person_id:
            first_name, *last_name = name.split()
            last_name = " ".join(last_name) if last_name else ""
            from_person = Person.objects.get(id=from_person_id)
            new_person = Person.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date)
            if image_url:
                new_person.image = image_url
                new_person.save()
            Relationship.objects.create(
                from_person=from_person,
                to_person=new_person,
                relationship_type=relationship_type
            )
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid data'}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

def home(request):
    persons = Person.objects.all()
    relationships = Relationship.objects.all()

    # Serialize QuerySets to JSON format
    persons_data = serialize('json', persons)
    relationships_data = serialize('json', relationships)
    print(type(persons_data))
    return render(request, 'home.html', {
        'persons_data': persons_data,
        'relationships_data': relationships_data
    })