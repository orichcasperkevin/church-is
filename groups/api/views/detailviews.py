from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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

    def delete(self, request, id):
        group = ChurchGroup.objects.get(id=id)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetGroupWhereNameLikePattern(APIView):
    '''
        get:
        returns a list of groups whose names contains the string pattern described in the slug parameter
    '''

    def get(self, request, pattern):
        result = ChurchGroup.objects.filter(name__icontains=pattern)
        data = ChurchGroupSerializer(result, many=True).data
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

class GetIndependentGroups(APIView):
    '''
        get:
        get the groups that are not within another group
    '''
    def get(self, request):
        church_group = ChurchGroup.objects.filter(group=None)
        data = ChurchGroupSerializer(church_group, many=True).data
        return Response(data)

class GetMembersOfChurchGroupWithId(APIView):
    '''
        get:
        get the members of a particular church group
    '''
    def get(self, request, id):
        church_group_membership = ChurchGroupMembership.objects.filter(church_group_id=id)
        data = ChurchGroupMembershipSerializer(church_group_membership, many=True).data
        return Response(data)

class CheckIfMemberIsInGroup(APIView):
    '''
        get:
        check if member exists in group
    '''
    def get(self,request,member_id,group_id):
        if ChurchGroupMembership.objects.filter(member__member_id=member_id,church_group_id=group_id).first():#if member exists in group
            return Response(True)
        else:
            return Response(False)


class GetChurchGroupsAMemberBelongsTo(APIView):
    '''
        get:
        get all the church_groups that a member with id <id> belongs to
    '''

    def get(self, request, id):
        church_group_membership = ChurchGroupMembership.objects.filter(member__member_id=id).order_by('-date_joined')
        data = ChurchGroupMembershipSerializer(church_group_membership, many=True).data
        return Response(data)
