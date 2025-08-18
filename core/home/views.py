from django.shortcuts import render , redirect
from .models import Recipe
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST' :
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')
        Recipe.objects.create(
            day = day , 
            name = name , 
            description = description
        )
        return redirect('/')

    query_set = Recipe.objects.all()
    if request.GET.get('search'):
        query_set = query_set.filter(
            day__icontains=request.GET.get('search'))
        

    context = {
        'recipes' : query_set
    }

    return render(request , 'home/recipe.html' , context)



# update the recipes data
@login_required(login_url='/login/')
def update_recipe(request ,id):
    query_set = Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')

        query_set.day = day
        query_set.name = name
        query_set.description = description
        query_set.save()

        return redirect('/')
    
    context ={
        'recipe' : query_set
    }

    return render(request , 'update_recipe.html' , context)



@login_required(login_url='/login/')
def delete_recipe(request , id):
    query_set = Recipe.objects.get(id = id)
    query_set.delete()
    return redirect('/')


