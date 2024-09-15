from django.shortcuts import render, redirect
from .models import Recipe
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)  # Fetch the recipe using its ID
    return render(request, 'recipes/detail.html', {'recipe': recipe})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time', 'cook_time']
    success_url = '/recipes/'  # Redirect to the index page after creation
    template_name = 'recipes/recipe_form.html'

# view for editing recipes
class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time', 'cook_time']
    template_name = 'recipes/recipe_form.html'  
    success_url = '/recipes/'  # Redirect after updating

# View for deleting recipes
class RecipeDelete(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'  
    success_url = '/recipes/'  