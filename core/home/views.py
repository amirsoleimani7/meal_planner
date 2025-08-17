from django.shortcuts import render , redirect
# from .models import Recipe
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# @login_required(login_url='/login/')
# def recipes(request):
#     if request.method == 'POST' :
#         data = request.POST
#         day = data.get('day')
#         name = data.get('name')
#         description = data.get('description')
#         Recipe.objects.create(
#             day = day , 
#             name = name , 
#             description = description
#         )
#         return redirect('/')

#     query_set = Recipe.objects.all()
#     if request.GET.GET('search'):
#         query_set = query_set.filter(
#             day__icontains=request.GET.get('search'))
        

#     context = {
#         'recipes' : query_set
#     }

#     return render(request , 'home/recipe.html' , context)






