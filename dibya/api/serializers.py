from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model=user
        fields='__all__'

class GuildSerializer(ModelSerializer):
    class Meta:
        model=guild
        fields='__all__'

class MatchSerializer(ModelSerializer):
    class Meta:
        model=match
        fields='__all__'