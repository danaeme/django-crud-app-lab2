from django.shortcuts import render, redirect
from .models import Recipe, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db import models



def home(request):
    return render(request, 'home.html', {'user': request.user})

def about(request):
    return render(request, 'about.html')

@login_required
def recipe_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id, user=request.user)  
    return render(request, 'recipes/detail.html', {'recipe': recipe})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_index.html', {'categories': categories})

@login_required
def recipes_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipes/recipes_by_category.html', {'category': category, 'recipes': recipes})

@login_required
def add_recipe_to_category(request, category_id, recipe_id):
    category = Category.objects.get(id=category_id)
    recipe = Recipe.objects.get(id=recipe_id)
    category.recipes.add(recipe)  
    return redirect('recipes-by-category', category_id=category_id)

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time', 'cook_time']
    success_url = '/recipes/'  
    template_name = 'recipes/recipe_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'ingredients', 'instructions', 'prep_time', 'cook_time']
    template_name = 'recipes/recipe_form.html'  
    success_url = '/recipes/' 

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'  
    success_url = '/recipes/'  

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'categories/category_form.html'

    def form_valid(self, form):
        form.save() 
        return redirect('/categories/')

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = '/categories/'

class CustomLoginView(LoginView):
    template_name = 'login.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe-index')  
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})