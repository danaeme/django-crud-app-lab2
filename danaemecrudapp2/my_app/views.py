from django.shortcuts import render, redirect
from .models import Recipe, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)  
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_index.html', {'categories': categories})

def recipes_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipes/recipes_by_category.html', {'category': category, 'recipes': recipes})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time', 'cook_time']
    success_url = '/recipes/'  
    template_name = 'recipes/recipe_form.html'

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time', 'cook_time']
    template_name = 'recipes/recipe_form.html'  
    success_url = '/recipes/' 

class RecipeDelete(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'  
    success_url = '/recipes/'  

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = '/categories/'