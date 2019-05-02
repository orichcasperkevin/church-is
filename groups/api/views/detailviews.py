from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
#TODO import each componet singly
from groups.models import (Fellowship,FellowshipMembership,FellowshipMeeting,FellowshipMeetingRoster,FellowshipPhoto,
                        CellGroup,CellGroupMembership,CellGroupMeeting,CellGroupMeetingRoster,CellGroupPhoto,
                        ChurchGroup,ChurchGroupMembership,GroupMeeting,GroupMeetingRoster,GroupPhoto,
                        Ministry,MinistryMembership,MinistryMeeting,MinistryMeetingRoster,ministryPhoto, )

from groups.api.serializers import (FellowshipSerializer,FellowshipMembershipSerializer,FellowshipMeetingSerializer,
                                    CellGroupSerializer,CellGroupMembershipSerializer,CellGroupMeetingSerializer,
                                    ChurchGroupSerializer,ChurchGroupMembershipSerializer,ChurchGroupMeetingSerializer,
                                    MinistrySerializer,MinistryMembershipSerializer,MinistryMeetingSerializer)

class GetFellowshipWithId(APIView):
    '''
    get:
    get the fellowship with the id <id>
    '''
    def get(self,request,id):
        fellowship = Fellowship.objects.filter(id = id)
        data = FellowshipSerializer(fellowship,many=True).data
        return Response(data)

class GetMembersOfFellowshipWithId(APIView):
    '''
        get:
        get the members of a particular fellowship
    '''
    def get(self,request,id):
        fellowship_membership = FellowshipMembership.objects.filter(fellowship_id = id).order_by('-date_joined')
        data = FellowshipMembershipSerializer(fellowship_membership,many=True).data
        return Response(data)

class GetFellowshipsAMemberBelongsTo(APIView):
    '''
        get:
        get all the felloships that a member with id <id> belongs to
    '''
    def get(self,request,id):
        fellowship_membership = FellowshipMembership.objects.filter(member__member_id = id).order_by('-date_joined')
        data = FellowshipMembershipSerializer(fellowship_membership,many=True).data
        return Response(data)

class GetMembersOfFellowshipWithID_MatchPattern(APIView):
    '''
    get:
    get the members of a particular fellowship ,filter by a pattern
    '''
    def get(self,request,id,pattern):
        fellowship_membership = FellowshipMembership.objects.filter(fellowship_id = id,member__member__first_name__icontains=pattern)
        data =FellowshipMembershipSerializer(fellowship_membership,many=True).data
        return Response(data)

class GetCellGroupWithId(APIView):
    '''
    get:
    get the cell group with the id <id>
    '''
    def get(self,request,id):
        cell_group = CellGroup.objects.filter(id = id)
        data = FellowshipSerializer(cell_group,many=True).data
        return Response(data)

class GetMembersOfCellGroupWithId(APIView):
    '''
        get:
        get the members of a particular cell group
    '''
    def get(self,request,id):
        cell_group_membership = CellGroupMembership.objects.filter(cell_group_id = id).order_by('-date_joined')
        data =CellGroupMembershipSerializer(cell_group_membership,many=True).data
        return Response(data)

class GetCellGroupsAMemberBelongsTo(APIView):
    '''
        get:
        get all the cell-groups that a member with id <id> belongs to
    '''
    def get(self,request,id):
        cell_group_membership = CellGroupMembership.objects.filter(member__member_id = id).order_by('-date_joined')
        data = CellGroupMembershipSerializer(cell_group_membership,many=True).data
        return Response(data)

class GetMinistryWithId(APIView):
    '''
    get:
    get the ministry with the id <id>
    '''
    def get(self,request,id):
        ministry = Ministry.objects.filter(id = id)
        data = FellowshipSerializer(ministry,many=True).data
        return Response(data)

class GetMembersOfMinistryWithId(APIView):
    '''
        get:
        get the members of a particular ministry
    '''
    def get(self,request,id):
        ministry_membership = MinistryMembership.objects.filter(ministry_id = id).order_by('-date_joined')
        data =MinistryMembershipSerializer(ministry_membership,many=True).data
        return Response(data)

class GetMinistriesMemberBelongsTo(APIView):
    '''
        get:
        get all the ministries that a member with id <id> belongs to
    '''
    def get(self,request,id):
        ministry_membership = MinistryMembership.objects.filter(member__member_id = id).order_by('-date_joined')
        data = MinistryMembershipSerializer(ministry_membership,many=True).data
        return Response(data)


class GetChurchGroupWithId(APIView):
    '''
    get:
    get the church group with the id <id>
    '''
    def get(self,request,id):
        church_group = ChurchGroup.objects.filter(id = id)
        data = FellowshipSerializer(church_group,many=True).data
        return Response(data)

class GetMembersOfChurchGroupWithId(APIView):
    '''
        get:
        get the members of a particular church group
    '''
    def get(self,request,id):
        church_group_membership = ChurchGroupMembership.objects.filter(church_group_id = id).order_by('-date_joined')
        data =ChurchGroupMembershipSerializer(church_group_membership,many=True).data
        return Response(data)

class GetChurchGroupsAMemberBelongsTo(APIView):
    '''
        get:
        get all the church_groups that a member with id <id> belongs to
    '''
    def get(self,request,id):
        church_group_membership = ChurchGroupMembership.objects.filter(member__member_id = id).order_by('-date_joined')
        data = ChurchGroupMembershipSerializer(church_group_membership,many=True).data
        return Response(data)
