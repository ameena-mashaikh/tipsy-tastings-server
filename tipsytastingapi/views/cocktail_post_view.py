"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import Cocktail, CocktailPost

class CocktailPostView(ViewSet):
    """Tipsy tastings view"""

    def list(self, request): 
        """Handle GET requests to get cocktail posts
        
        Returns:
            Response -- JSON serialized event
        """

        cocktail_post = CocktailPost.objects.all()


        serializer = CocktailPostSerializer(cocktail_post, many = True)
        return Response(serializer.data)





    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game 
        """

        cocktail = Cocktail.objects.get(pk=pk)
        serializer = CocktailPostSerializer(cocktail)
        return Response(serializer.data)





    def create(self, request):
        """Handle POST operations

        Returns:
        Response -- JSON serialized Cocktail Liquor instance"""
        cocktail = Cocktail.objects.get(pk =request.data["cocktailId"])
        

        cocktail = Cocktail.objects.create(
            cocktail = cocktail,
            caption = request.data['caption']
        )
        serializer = CocktailPostSerializer(cocktail)
        return Response(serializer.data , status=status.HTTP_201_CREATED)




class CocktailPostSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails."""
    class Meta:
        model=CocktailPost
        fields=("id", "cocktail", "caption" )
        depth = 2   