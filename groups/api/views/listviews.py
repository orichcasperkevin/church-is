from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from groups.models import (Fellowship,FellowshipMeeting,FellowshipMeetingRoster,FellowshipPhoto,
                        CellGroup,CellGroupMeeting,CellGroupMeetingRoster,CellGroupPhoto,
                        ChurchGroup,ChurchGroup,GroupMeeting,GroupMeetingRoster,GroupPhoto,
                        Ministry,MinistryMeeting,MinistryMeetingRoster,ministryPhoto, )

from groups.api.serializers import (FellowshipSerializer,FellowshipMeetingSerializer,
                                    CellGroupSerializer,CellGroupMeetingSerializer,
                                    ChurchGroupSerializer,ChurchGroupMeetingSerializer,
                                    MinistrySerializer,MinistryMeetingSerializer)

class FellowshipList(generics.ListCreateAPIView):
    '''
        a list of fellowships
    '''
    queryset = Fellowship.objects.all()
    serializer_class = FellowshipSerializer

class FellowshipMeetingList(generics.ListCreateAPIView):
    '''
        a list of fellowship meetings
    '''
    queryset = FellowshipMeeting.objects.all()
    serializer_class = FellowshipMeetingSerializer

class CellGroupList(generics.ListCreateAPIView):
    '''
        a list of cell groups
    '''
    queryset = CellGroup.objects.all()
    serializer_class = CellGroupSerializer

class CellGroupMeetingList(generics.ListCreateAPIView):
    '''
        a list of cell grou[] meetings
    '''
    queryset = CellGroupMeeting.objects.all()
    serializer_class = CellGroupMeetingSerializer

class ChurchGroupList(generics.ListCreateAPIView):
    '''
        a list of church groups
    '''
    queryset = ChurchGroup.objects.all()
    serializer_class = ChurchGroupSerializer

class ChurchGroupMeetingList(generics.ListCreateAPIView):
    '''
        a list of church group meetings
    '''
    queryset = GroupMeeting.objects.all()
    serializer_class = ChurchGroupMeetingSerializer

class MinistryList(generics.ListCreateAPIView):
    '''
        a list of ministries
    '''
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer

class MinistryMeetingList(generics.ListCreateAPIView):
    '''
        a list of ministry meetings
    '''
    queryset = MinistryMeeting.objects.all()
    serializer_class = MinistryMeetingSerializer