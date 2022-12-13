"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import CocktailLiqueur, Cocktail, Liqueur

class CocktailLiqueurView(ViewSet):
    """Tipsy tastings view"""

    def list(self, request): 
        """Handle GET requests to get cocktail's liqueur
        
        Returns:
            Response -- JSON serialized event
        """

        cocktail_liqueurs = CocktailLiqueur.objects.all()


        serializer = CocktailLiqueurSerializer(cocktail_liqueurs, many = True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized Cocktail Liqueur instance"""
        
        cocktail = Cocktail.objects.get(pk=request.data["cocktail"])
        liqueur = Liqueur.objects.get(pk = request.data["liqueur"])
        cocktail_liqueur = CocktailLiqueur.objects.create(
            cocktail=cocktail,
            liqueur = liqueur,
        )
        serializer = CocktailLiqueurSerializer(cocktail_liqueur)
        return Response(serializer.data , status=status.HTTP_201_CREATED)


    # def retrieve(self, request, pk):
    #     """Handle GET requests for single game

    #     Returns:
    #         Response -- JSON serialized game 
    #     """

    #     cocktail = Cocktail.objects.get(pk=pk)
    #     serializer = CocktailSerializer(cocktail)
    #     return Response(serializer.data)

class CocktailLiqueurSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    class Meta:
        model=CocktailLiqueur
        fields=("id", "cocktail", "liqueur", )