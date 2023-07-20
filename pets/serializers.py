from rest_framework import serializers
from django.db import models
from groups.serializers import GroupSerializer
from pets.models import PetSex
from traits.serializers import TraitSerializer

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight= serializers.FloatField()
    sex= serializers.ChoiceField(choices=PetSex.choices,default=PetSex.DEFAULT)
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
      
    