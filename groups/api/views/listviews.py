from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.api.serializers import (FellowshipSerializer, FellowshipMeetingSerializer,
                                    CellGroupSerializer, CellGroupMeetingSerializer,
                                    ChurchGroupSerializer, ChurchGroupMeetingSerializer,
                                    MinistrySerializer, MinistryMeetingSerializer)
# TODO import each componet singly
from groups.models import (Fellowship, FellowshipMeeting, CellGroup, CellGroupMeeting, ChurchGroup, GroupMeeting,
                           Ministry, MinistryMeeting, )


class FellowshipList(generics.ListCreateAPIView):
    '''
        a list of fellowships
    '''
    queryset = Fellowship.objects.all()
    serializer_class = FellowshipSerializer


class FellowshipMeetingList(APIView):
    '''
        a list of fellowship meetings with for a fellowship with Id <id>
    '''

    def get(self, request, id):
        fellowship_meeting = FellowshipMeeting.objects.filter(fellowship_id=id)
        data = FellowshipMeetingSerializer(fellowship_meeting, many=True).data
        return Response(data)


class CellGroupList(generics.ListCreateAPIView):
    '''
        a list of cell groups
    '''
    queryset = CellGroup.objects.all()
    serializer_class = CellGroupSerializer


class CellGroupMeetingList(APIView):
    '''
        a list of cell groups meetings with for a cellGroup with Id <id>
    '''

    def get(self, request, id):
        cell_group_meeting = CellGroupMeeting.objects.filter(cell_group_id=id)
        data = CellGroupMeetingSerializer(cell_group_meeting, many=True).data
        return Response(data)


class ChurchGroupList(generics.ListCreateAPIView):
    '''
        a list of church groups
    '''
    queryset = ChurchGroup.objects.all()
    serializer_class = ChurchGroupSerializer


class ChurchGroupMeetingList(APIView):
    '''
        a list of church_group meetings with for a church_group with Id <id>
    '''

    def get(self, request, id):
        church_group_meeting = GroupMeeting.objects.filter(group_id=id)
        data = ChurchGroupMeetingSerializer(church_group_meeting, many=True).data
        return Response(data)


class MinistryList(generics.ListCreateAPIView):
    '''
        a list of ministries
    '''
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer


class MinistryMeetingList(APIView):
    '''
        a list of ministry meetings  for a ministry with Id <id>
    '''

    def get(self, request, id):
        ministry_meeting = MinistryMeeting.objects.filter(ministry_id=id)
        data = MinistryMeetingSerializer(ministry_meeting, many=True).data
        return Response(data)
