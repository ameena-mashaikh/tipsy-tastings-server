"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import Cocktail, CocktailLiquor, CocktailLiqueur, CocktailStapleIngredient, Category, Mixologist

class CocktailView(ViewSet):
    """Tipsy tastings view"""

    def list(self, request): 
        """Handle GET requests to get cocktails
        
        Returns:
            Response -- JSON serialized event
        """

        cocktails = Cocktail.objects.all()

        if "mycocktails" in request.query_params:
            cocktails = Cocktail.objects.filter(created_by_mixologist = self.request.user.id)

        serializer = CocktailSerializer(cocktails, many = True)
        return Response(serializer.data)





    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game 
        """

        cocktail = Cocktail.objects.get(pk=pk)
        serializer = CocktailSerializer(cocktail)
        return Response(serializer.data)





    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized Cocktail Liquor instance"""
        category = Category.objects.get(pk =request.data["category"])
        mixologist = Mixologist.objects.get(user=request.auth.user)
        

        cocktail = Cocktail.objects.create(
            name = request.data["name"],
            category = category,
            recipe = request.data["recipe"],
            image = request.data["image"],
            created_by_mixologist = mixologist

        )
        serializer = CocktailSerializer(cocktail)
        return Response(serializer.data , status=status.HTTP_201_CREATED)



    def update(self, request, pk):
        """Handle PUT requests for a cocktail

        Returns:
            Response -- Empty body with 204 status code
        """

        cocktail = Cocktail.objects.get(pk=pk)
        cocktail.category = Category.objects.get(pk =request.data["category"])
        #cocktail.created_by_mixologist = Mixologist.objects.get(user=request.auth.user)
        cocktail.name = request.data["name"]
        cocktail.recipe = request.data["recipe"]
        cocktail.image = request.data["image"]
        cocktail.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CocktailSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    class Meta:
        model=Cocktail
        fields=("id", "name", "category", "recipe", "image", "created_by_mixologist", "liquors", "liqueurs", "staple_ingredients", "post_cocktail" )
        depth = 2   