"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from tipsytastingapi.models import Syrup

class SyrupView(ViewSet):
    """Tipsy tastings Syrups view"""

    def list(self, request): 
        """Handle GET requests to get syrups
        
        Returns:
            Response -- JSON serialized event
        """

        syrups = Syrup.objects.all()


        serializer = SyrupSerializer(syrups, many = True)
        return Response(serializer.data)



class SyrupSerializer(serializers.ModelSerializer):
    """JSON serializer for syrups."""
    class Meta:
        model=Syrup
        fields=("id", "name", )