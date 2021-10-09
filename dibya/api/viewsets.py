from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class matchViewset(viewsets.ModelViewSet):
    serializer_class=MatchSerializer
    queryset=user.objects.all()
    http_method_names = ['get','head']
    filter_backends = [DjangoFilterBackend]
    filterset_fields ='__all__'

    def list(self,request):
        print(request.GET)
        if 'guild_uid1' and 'guild_uid2' in request.GET:
            
            g1=request.GET['guild_uid1']
            g2=request.GET['guild_uid2']
            print(g1)
            print(g2)
            guild1=guild.objects.get(id=g1)
            guild2=guild.objects.get(id=g2)
            total_users=user.objects.all().count()
            common_users=0
            for player in guild1.members.all():
                if player in guild2.members.all():
                    common_users+=1
            percentage=(common_users/total_users)*100.0
            return Response({'match_percentage':percentage})
        
        else:
            return Response({'error':'Please input both fields!'})


class GuildViewset(viewsets.ModelViewSet):
    serializer_class=GuildSerializer
    queryset=guild.objects.all()
    