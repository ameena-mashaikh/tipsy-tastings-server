"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import CocktailStapleIngredient, Cocktail, StapleIngredient

class CocktailStapleIngredientView(ViewSet):
    """Tipsy tastings view"""

    def list(self, request): 
        """Handle GET requests to get cocktail's staple ingredients
        
        Returns:
            Response -- JSON serialized event
        """

        cocktail_staples = CocktailStapleIngredient.objects.all()


        serializer = CocktailStapleIngredientSerializer(cocktail_staples, many = True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized Cocktail Staple Ingredient instance"""
        
        cocktail = Cocktail.objects.get(pk=request.data["cocktail"])
        staple_ingredient = StapleIngredient.objects.get(pk = request.data["staple_ingredient"])
        cocktail_staple = CocktailStapleIngredient.objects.create(
            cocktail=cocktail,
            staple_ingredient = staple_ingredient
            )
        serializer = CocktailStapleIngredientSerializer(cocktail_staple)
        return Response(serializer.data , status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk):
        """Handle GET requests for single cocktail staple ingredient

        Returns:
            Response -- JSON serialized staple ingredient
        """

        cocktail_staple = CocktailStapleIngredient.objects.get(pk=pk)
        serializer = CocktailStapleIngredientSerializer(cocktail_staple)
        return Response(serializer.data)


    def update(self, request, pk):
        """Handle PUT requests for cocktail staple ingredient

        Returns:
            Response -- Empty body with 204 status code
        """

        cocktail_staple_ingredient = CocktailStapleIngredient.objects.get(pk=pk)
        cocktail_staple_ingredient.cocktail = Cocktail.objects.get(pk =request.data["cocktail"])
        cocktail_staple_ingredient.staple_ingredient = StapleIngredient.objects.get(pk =request.data["staple_ingredient"])
        cocktail_staple_ingredient.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        cocktail_staple = CocktailStapleIngredient.objects.get(pk=pk)
        cocktail_staple.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CocktailStaplesForCocktailSerializer(serializers.ModelSerializer):
    """json serializer for a cocktail's staple"""
    class Meta:
        model = Cocktail
        fields = ('id',)


class CocktailStapleIngredientSerializer(serializers.ModelSerializer):
    """JSON serializer for a cocktail's staple ingredients."""
    cocktail = CocktailStaplesForCocktailSerializer(many = False)
    class Meta:
        model=CocktailStapleIngredient
        fields=("id", "cocktail", "staple_ingredient", )
        depth = 1
