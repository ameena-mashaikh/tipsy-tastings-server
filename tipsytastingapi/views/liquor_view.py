"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import Liquor

class LiquorView(ViewSet):
    """Tipsy tastings view"""

    def list(self, request): 
        """Handle GET requests to get cocktails
        
        Returns:
            Response -- JSON serialized event
        """

        liquors = Liquor.objects.all()


        serializer = LiquorSerializer(liquors, many = True)
        return Response(serializer.data)


    # def retrieve(self, request, pk):
    #     """Handle GET requests for single game

    #     Returns:
    #         Response -- JSON serialized game 
    #     """

    #     cocktail = Cocktail.objects.get(pk=pk)
    #     serializer = CocktailSerializer(cocktail)
    #     return Response(serializer.data)

class LiquorSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    class Meta:
        model=Liquor
        fields=("id", "name", )