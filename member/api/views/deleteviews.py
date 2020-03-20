from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User
from member.models import Member

class BulkDeleteMembers(APIView):
    '''
        post:
        delete members whose ids are in member_is
    '''
    def post(self, request):
        member_ids = request.data.get("member_ids")

        for id in member_ids:
            member = Member.objects.get(member__id=id)
            member.delete()
            user = User.objects.get(id=id)
            user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
