from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from groups.api.serializers import GroupOfChurchGroupSerializer, ChurchGroupSerializer, ChurchGroupMeetingSerializer
from groups.models import GroupOfChurchGroups, ChurchGroup, GroupMeeting

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


class ChurchGroupMeetingList(APIView):
    '''
        a list of church_group meetings with for a church_group with Id <id>
    '''

    def get(self, request, id):
        church_group_meeting = GroupMeeting.objects.filter(group_id=id)
        data = ChurchGroupMeetingSerializer(church_group_meeting, many=True).data
        return Response(data)
