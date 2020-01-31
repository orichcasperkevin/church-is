from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from groups.api.serializers import GroupOfChurchGroupSerializer, ChurchGroupSerializer
from groups.models import GroupOfChurchGroups, ChurchGroup

class GroupOfChurchGroupsList(generics.ListCreateAPIView):
    '''
        a list of groups of church groups
    '''
    queryset = GroupOfChurchGroups.objects.all()
    serializer_class = GroupOfChurchGroupSerializer

class ChurchGroupList(generics.ListCreateAPIView):
    '''
        a list of church groups
    '''
    queryset = ChurchGroup.objects.all()
    serializer_class = ChurchGroupSerializer
