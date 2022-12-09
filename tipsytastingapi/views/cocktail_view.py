"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import Cocktail

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

class CocktailSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    class Meta:
        model=Cocktail
        fields=("id", "name", "category", "recipe", "image", "created_by_mixologist", "liquors", "liqueurs", "staple_ingredients", )
        depth = 1