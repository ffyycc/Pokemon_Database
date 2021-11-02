"""cs411 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import pokemon.views
import training.views
import public_info.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types/all', pokemon.views.get_types),
    path('types/statistics', pokemon.views.get_type_statistics),
    path('pokemon/all', pokemon.views.get_pokemons),
    path('pokemon/search', pokemon.views.search_pokemon_by_id),
    path('pokemon/create', pokemon.views.create_pokemon),
    path('pokemon/update', pokemon.views.update_pokemon),
    path('pokemon/delete', pokemon.views.delete_pokemon),

    path('pokemon/adopt', training.views.adopt_pokemon),
    
    path('advanced_query', training.views.advanced_query),
    path('training/search', training.views.search_training_by_id),
    path('training/update', training.views.update_training),
    path('training/delete', training.views.delete_training),
    path('training/user/<userId>', training.views.get_trainings),
    path('training/all', training.views.all_trainings),

    path('public_info/all', public_info.views.get_Publicinfo),
    path('public_info/statistics', public_info.views.get_Public_statistics),
    path('public_info/search', public_info.views.search_public_by_id),
    path('public_info/create', public_info.views.create_public),
    path('public_info/update', public_info.views.update_public),
    path('public_info/delete', public_info.views.delete_public),

    path('pokemon/highattr', user.views.advance),
    path('user/front10', user.views.get_user),
    path('user/search', user.views.search_user_by_id),
    path('user/create', user.views.create_user),
    path('user/update', user.views.update_user),
    path('user/delete', user.views.delete_user),
    path('user/exists', user.views.user_exists),
    path('user/login', user.views.login),
    path('user/register', user.views.register),
]
