from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from .views import CustomLoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='home.html'), name='home'),  
    path('about/', views.about, name='about'),
    path('recipes/', views.recipe_index, name='recipe-index'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe-delete'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('categories/', views.category_list, name='categories-index'),
    path('categories/<int:category_id>/', views.recipes_by_category, name='recipes-by-category'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
]