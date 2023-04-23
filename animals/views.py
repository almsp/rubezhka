from django.shortcuts import render, redirect, get_object_or_404
from animals.models import Animals, Pay, AnimalsCategory
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from volunteers.models import Volunteers
def animals(request):
    animals = Animals.objects.all()
    return render(request, "animals.html", context={"animals": animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animals, pk=animal_id)
    context = {
        'animal': animal,
    }
    return render(request, 'animal_detail.html', context)

def buy_animal(request, animal_id):
    animal = get_object_or_404(Animals, pk=animal_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        number = request.POST.get('number')
        if not email or not number:
            messages.error(request, 'Please enter both email and number')
        else:
            pay = Pay(user=request.user, email=email, number=number)
            pay.save()
            messages.success(request, 'Payment successfully processed!')
            return redirect("fine")
    context = {
        'animal': animal,
    }
    return render(request, 'buy_animal.html', context)


def fine(request):
    return render(request, "fine.html")


def delete_animal(request, animal_id):
    animal = get_object_or_404(Animals, pk=animal_id)
    if request.method == 'POST':
        # Handle delete request
        animal.delete()
        messages.success(request, 'Animal deleted successfully!')
        return redirect('animals')
    else:
        return render(request, 'delete_animal.html', {'animal': animal})


@login_required
def create_animal(request):
    if request.method == 'POST':
       
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        category_id = request.POST.get('category')
        category = AnimalsCategory.objects.get(id=category_id) if category_id else None
        price = int(request.POST.get('price')) if request.POST.get('price') else None
        age = int(request.POST.get('age')) if request.POST.get('age') else None
        description = request.POST.get('description')
        image = request.FILES.get('image')
        colour = request.POST.get('colour')
        
        animal = Animals.objects.create(
            name=name,
            breed=breed,
            category=category,
            price=price,
            age=age,
            description=description,
            image=image,
            colour=colour
        )

        return redirect('animal_detail', animal.id)
        
    categories = AnimalsCategory.objects.all()
    
    context = {
        'categories': categories,
    }
    
    return render(request, 'create_animal.html', context)