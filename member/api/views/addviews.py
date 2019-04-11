from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from member.models import (Member,MemberContact,MemberAge,
                            MemberResidence,MemberRole,Role,
                            MemberMaritalStatus,Family,FamilyMembership,)

from member.api.serializers import (UserSerializer,MemberSerializer,CreateMemberSerializer,MemberContactSerializer,MemberAgeSerializer,
                                    MemberResidenceSerializer,MemberRoleSerializer,
                                    RoleSerializer,MemberMaritalStatusSerializer,
                                    FamilySerializer,FamilyMembershipSerializer,)

class addMember(APIView):
    '''

    '''
    def post(self,request):

        first_name = request.data.get("first_name")
        username = '@'+first_name.lower()
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        gender = request.data.get("gender")

        user = User(first_name = first_name, username = username, last_name = last_name, email= email)
        user.save()

        user_id = user.id

        queryset = User.objects.filter(id = user_id)
        member = []
        for member in queryset:
            member = member
        serializer = UserSerializer(member)
        member = serializer.data

        data = {'member':member,'gender':gender}
        serializer = CreateMemberSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
