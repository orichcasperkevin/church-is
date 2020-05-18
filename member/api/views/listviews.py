from datetime import date

from django.utils.timezone import now
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.api.serializers import *
from member.models import *

class MemberList(generics.ListCreateAPIView):
    '''
        get:
        return list of members
        post:
        create a new member
    '''
    queryset = Member.objects.all().order_by('-member__date_joined')
    serializer_class = MemberSerializer

class MemberWhereFirstNameLikePattern(APIView):
    '''
        get:
        returns a list of members whose first names contain the string pattern described in the slug parameter
    '''

    def get(self, request, pattern):
        result = Member.objects.filter(member__first_name__icontains=pattern)
        data = MemberSerializer(result, many=True).data
        return Response(data)

class MemberFilteredByGender(APIView):
    '''
        get:
        returns list of people filtered with gender
    '''

    def get(self, request, gender):
        if (gender == "M" or gender == "F"):
            members = Member.objects.filter(gender=gender)
        else:
            members = Member.objects.all()

        data = MemberSerializer(members, many=True).data
        return Response(data)

class MemberFilteredByAge(APIView):
    '''
        get:
        returns a list of members filtered by age
    '''

    def get(self, request, min_age, max_age,gender):
        current = now().date()
        min_date = date(current.year - min_age, current.month, current.day)
        max_date = date(current.year - max_age, current.month, current.day)
        members = MemberAge.objects.filter(d_o_b__gte=max_date,
                                           d_o_b__lte=min_date)

        if (gender == "M" or gender == "F"):
            members = members.filter(member__gender=gender)

        data = MemberAgeSerializer(members, many=True).data
        return Response(data)

class GetMembersWithAdminRoles(APIView):
    def get(self,request):
        #PATCH  creating an admin role for currently logged in member if name is
        #admin as I set to default or dorohkakz for dev server
        user = request.user
        if (user.username == 'dorohkakz' or user.username == 'admin'):
            if MemberRole.objects.filter(member__member=user,
                                             role__permission_level__lte=5)\
                                      .first():
                print("there exists an admin role for this user")
            else:
                print("no admin role found for member .adding...")
                role , __ = Role.objects.get_or_create(permission_level = 0,
                                                       is_group_role = False,
                                                       role="super admin",
                                                       description="can view, add and update anything")

                member = Member.objects.get(member=request.user)
                MemberRole.objects.create(member=member,role=role)



        members = MemberRole.objects.filter(role__permission_level__lt=5)
        data = MemberRoleSerializer(members,many=True).data

        return Response(data)

class RoleList(APIView):
    '''
        get:
        return list of member roles
    '''
    def get(self,request):
        roles = Role.objects.all()
        data = RoleSerializer(roles,many=True).data

        return Response(data)

    def post(self,request):
        serializer = RoleSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        role = Role.objects.get(id=request.data.get('role_id'))
        serializer = RoleSerializer(instance=role,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        role = Role.objects.get(id=request.data.get('role_id'))
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
