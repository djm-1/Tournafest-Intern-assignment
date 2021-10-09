from django.urls import path, include
from rest_framework import routers
from .viewsets import *
router = routers.DefaultRouter()

router.register('discord_guild',GuildViewset,'guild')
router.register('discord_match_percentage',matchViewset,'match')

urlpatterns = [
    path('', include(router.urls)),
]