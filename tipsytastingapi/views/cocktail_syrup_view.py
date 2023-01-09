"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import CocktailSyrup, Cocktail, Syrup

class CocktailSyrupView(ViewSet):
    """Tipsy tastings view"""

    def list(self, request): 
        """Handle GET requests to get cocktail's syrups
        
        Returns:
            Response -- JSON serialized event
        """

        cocktail_syrups = CocktailSyrup.objects.all()


        serializer = CocktailSyrupSerializer(cocktail_syrups, many = True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized Cocktail Syrup instance"""
        
        cocktail = Cocktail.objects.get(pk=request.data["cocktail"])
        syrup = Syrup.objects.get(pk = request.data["syrup"])
        cocktail_syrup = CocktailSyrup.objects.create(
            cocktail=cocktail,
            syrup = syrup
            )
        serializer = CocktailSyrupSerializer(cocktail_syrup)
        return Response(serializer.data , status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk):
        """Handle GET requests for single cocktail syrup

        Returns:
            Response -- JSON serialized staple ingredient
        """

        cocktail_syrup = CocktailSyrup.objects.get(pk=pk)
        serializer = CocktailSyrupSerializer(cocktail_syrup)
        return Response(serializer.data)


    def update(self, request, pk):
        """Handle PUT requests for cocktail syrup

        Returns:
            Response -- Empty body with 204 status code
        """

        cocktail_syrup = CocktailSyrup.objects.get(pk=pk)
        cocktail_syrup.cocktail = Cocktail.objects.get(pk =request.data["cocktail"])
        cocktail_syrup.syrup = Syrup.objects.get(pk =request.data["syrup"])
        cocktail_syrup.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        cocktail_syrup = CocktailSyrup.objects.get(pk=pk)
        cocktail_syrup.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CocktailSyrupsForCocktailSerializer(serializers.ModelSerializer):
    """json serializer for a cocktail's syrup"""
    class Meta:
        model = Cocktail
        fields = ('id',)


class CocktailSyrupSerializer(serializers.ModelSerializer):
    """JSON serializer for a cocktail's staple ingredients."""
    cocktail = CocktailSyrupsForCocktailSerializer(many = False)
    class Meta:
        model=CocktailSyrup
        fields=("id", "cocktail", "syrup", )
        depth = 1
