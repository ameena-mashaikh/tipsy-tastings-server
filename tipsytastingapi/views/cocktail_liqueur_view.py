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
        if "cocktail" in request.query_params:
            query_value = request.query_params["cocktail"]
            cocktail_liqueurs = cocktail_liqueurs.filter(cocktail = query_value)


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


    def retrieve(self, request, pk):
        """Handle GET requests for single cocktail liqueur

        Returns:
            Response -- JSON serialized liqueur 
        """

        cocktail_liqueur = CocktailLiqueur.objects.get(pk=pk)
        serializer = CocktailLiqueurSerializer(cocktail_liqueur)
        return Response(serializer.data)


    def update(self, request, pk):
        """Handle PUT requests for cocktail liqueur

        Returns:
            Response -- Empty body with 204 status code
        """

        cocktail_liqueur = CocktailLiqueur.objects.get(pk=pk)
        cocktail_liqueur.cocktail = Cocktail.objects.get(pk =request.data["cocktail"])
        cocktail_liqueur.liqueur = Liqueur.objects.get(pk =request.data["liqueur"])
        cocktail_liqueur.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        cocktail_liqueur = CocktailLiqueur.objects.get(pk=pk)
        cocktail_liqueur.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CocktailLiqueurForCocktailSerializer(serializers.ModelSerializer):
    """json serializer for a cocktail's liquor"""
    class Meta:
        model = Cocktail
        fields = ('id',)

class CocktailLiqueurSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    cocktail = CocktailLiqueurForCocktailSerializer(many = False)
    class Meta:
        model=CocktailLiqueur
        fields=("id", "cocktail", "liqueur", )
        depth = 1
