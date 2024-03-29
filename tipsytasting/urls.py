"""tipsytasting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from tipsytastingapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from tipsytastingapi.views import CocktailView, LiquorView, LiqueurView, StapleIngredientView, CategoryView, CocktailPostView, SyrupView
from tipsytastingapi.views import CocktailLiquorView, CocktailLiqueurView, CocktailStapleIngredientView, CocktailSyrupView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cocktails', CocktailView, 'cocktail')
router.register(r'liquors', LiquorView, 'liquor')
router.register(r'liqueurs', LiqueurView, 'liqueur')
router.register(r'stapleingredients', StapleIngredientView, 'stapleingredient')
router.register(r'syrups', SyrupView, 'syrup')
router.register(r'categories', CategoryView, 'category')
router.register(r'cocktailposts', CocktailPostView, 'cocktailpost')
router.register(r'cocktailliqueurs', CocktailLiqueurView, 'cocktailliqueur')
router.register(r'cocktailliquors', CocktailLiquorView, 'cocktailliquor')
router.register(r'cocktailstapleingredients', CocktailStapleIngredientView, 'cocktailstapleingredient')
router.register(r'cocktailsyrups', CocktailSyrupView, 'cocktailsyrup')











urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]