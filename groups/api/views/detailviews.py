from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView

from groups.api.serializers import  ChurchGroupSerializer, ChurchGroupMembershipSerializer
from groups.models import  ChurchGroup,ChurchGroupMembership


class GetChurchGroupWithId(APIView):
    '''
    get:
    get the church group with the id <id>
    '''

    def get(self, request, id):
        church_group = ChurchGroup.objects.filter(id=id)
        data = ChurchGroupSerializer(church_group, many=True).data
        return Response(data)

class GetGroupsInGroupWithId(APIView):
    '''
        get:
        get the groups within a particular group of church groups
    '''
    def get(self, request, id):
        church_group = ChurchGroup.objects.filter(group_id=id)
        data = ChurchGroupSerializer(church_group, many=True).data
        return Response(data)

class GetMembersOfChurchGroupWithId(APIView):
    '''
        get:
        get the members of a particular church group
    '''
    def get(self, request, id):
        church_group_membership = ChurchGroupMembership.objects.filter(church_group_id=id).order_by('-date_joined')
        data = ChurchGroupMembershipSerializer(church_group_membership, many=True).data
        return Response(data)


class GetChurchGroupsAMemberBelongsTo(APIView):
    '''
        get:
        get all the church_groups that a member with id <id> belongs to
    '''

    def get(self, request, id):
        church_group_membership = ChurchGroupMembership.objects.filter(member__member_id=id).order_by('-date_joined')
        data = ChurchGroupMembershipSerializer(church_group_membership, many=True).data
        return Response(data)
