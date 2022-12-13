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


    # def retrieve(self, request, pk):
    #     """Handle GET requests for single game

    #     Returns:
    #         Response -- JSON serialized game 
    #     """

    #     cocktail = Cocktail.objects.get(pk=pk)
    #     serializer = CocktailSerializer(cocktail)
    #     return Response(serializer.data)

class CocktailLiquorSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    class Meta:
        model=CocktailLiquor
        fields=("id", "cocktail", "liquor", )
        depth = 1