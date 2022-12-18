"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import CocktailLiquor, Cocktail, Liquor

class CocktailLiquorView(ViewSet):
    """Tipsy tastings view"""

    def list(self, request): 
        """Handle GET requests to get cocktail's liquor
        
        Returns:
            Response -- JSON serialized event
        """

        cocktail_liquors = CocktailLiquor.objects.all()
        if "cocktail" in request.query_params:
            query_value = request.query_params["cocktail"]
            cocktail_liquors = cocktail_liquors.filter(cocktail = query_value)

        serializer = CocktailLiquorSerializer(cocktail_liquors, many = True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized Cocktail Liquor instance""" 
        
        cocktail = Cocktail.objects.get(pk=request.data["cocktail"])
        liquor = Liquor.objects.get(pk = request.data["liquor"])
        cocktail_liquor = CocktailLiquor.objects.create(
            cocktail=cocktail,
            liquor = liquor,
        )
        serializer = CocktailLiquorSerializer(cocktail_liquor)
        return Response(serializer.data , status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        """Handle PUT requests for cocktail liquor

        Returns:
            Response -- Empty body with 204 status code
        """

        cocktail_liquor = CocktailLiquor.objects.get(pk=pk)
        cocktail_liquor.cocktail = Cocktail.objects.get(pk =request.data["cocktail"])
        cocktail_liquor.liquor = Liquor.objects.get(pk =request.data["liquor"])
        cocktail_liquor.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk):
        """Handle GET requests for single cocktail liquor

        Returns:
            Response -- JSON serialized liquor 
        """

        cocktail_liquor = CocktailLiquor.objects.get(pk=pk)
        serializer = CocktailLiquorSerializer(cocktail_liquor)
        return Response(serializer.data)


    def destroy(self, request, pk):
        cocktail_liquor = CocktailLiquor.objects.get(pk=pk)
        cocktail_liquor.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CocktailLiquorForCocktailSerializer(serializers.ModelSerializer):
    """json serializer for a cocktail's liquor"""
    class Meta:
        model = Cocktail
        fields = ('id',)


class CocktailLiquorSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    cocktail = CocktailLiquorForCocktailSerializer(many = False)
    class Meta:
        model=CocktailLiquor
        fields=("id", "cocktail", "liquor", )
        depth = 1