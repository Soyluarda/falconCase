from rest_framework import serializers
from .models import ExtendedUser
from riot.serializers import CharSerializer

class UserSerializer(serializers.ModelSerializer):
    char = CharSerializer(many=True)
    class Meta:
        model = ExtendedUser
        fields = ("id","username","char")
