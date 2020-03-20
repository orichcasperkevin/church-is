from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member, Role
from groups.models import ChurchGroup, ChurchGroupMembership

class RemoveMembersFromGroup(APIView):
    '''
    post:
    add a group
    '''
    def post(self,request):
        group_id = request.data.get("group_id")
        member_ids = request.data.get("member_ids")

        group = ChurchGroup.objects.get(id=group_id)
        for id in member_ids:
            membership = ChurchGroupMembership.objects.filter(member__member_id=id,church_group_id=group.id).first()
            if membership:
                membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
