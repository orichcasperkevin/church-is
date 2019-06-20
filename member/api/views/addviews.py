from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from member.models import (Member,MemberContact,MemberAge,
                            MemberResidence,Role,
                            MemberMaritalStatus,Family,FamilyMembership,)

from member.api.serializers import (UserSerializer,MemberSerializer,CreateMemberSerializer,
                                    MemberContactSerializer,MemberAgeSerializer,RoleMemberShipSerializer,
                                    MemberResidenceSerializer,
                                    RoleSerializer,MemberMaritalStatusSerializer,
                                    FamilySerializer,FamilyMembershipSerializer,)
from sms.africastalking.at import ChurchSysMessenger

messenger = ChurchSysMessenger("create member","test member 2")
class addMember(APIView):
    '''

    '''
    def post(self,request):

        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = '@'+first_name.lower()+last_name.lower()
        email = request.data.get("email")
        gender = request.data.get("gender")

        user = User(
                    first_name = first_name,
                    username = username,
                    last_name = last_name,
                    email= email
                    )
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

class AddMemberContact(APIView):
    '''
        post:
        add contact for a member.
    '''
    def post(self,request):

            member_id = request.data.get("member_id")
            queryset = Member.objects.filter(member_id=member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data

            postal = request.data.get("postal_address")
            phone = request.data.get("phone")
            contact = request.data.get("contact")

            data = {'member':member,'postal':postal, 'phone':phone, 'contact':contact}

            serializer = MemberContactSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddMemberD_O_B(APIView):
    '''
        post:
        add date of birth for a member
    '''
    def post(self,request):

            member_id = request.data.get("member_id")
            queryset = Member.objects.filter(member_id=member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data

            d_o_b = request.data.get("d_o_b")

            data = {'member':member,'d_o_b':d_o_b}

            serializer = MemberAgeSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddMemberResidence(APIView):
    '''
        post:
        add member residence
    '''
    def post(self,request):

            member_id = request.data.get("member_id")
            queryset = Member.objects.filter(member_id=member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data

            town = request.data.get("town")
            road = request.data.get("road")
            street = request.data.get("street")
            village_estate = request.data.get("village/estate")
            description = request.data.get("description")


            data = {'member':member,'town':town, 'road':road, 'street':street,
                    'village_estate':village_estate, 'description':description}

            serializer = MemberResidenceSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddMemberMaritalStatus(APIView):
    '''
        post:
        add member marital status
    '''
    def post(self,request):

            member_id = request.data.get("member_id")
            queryset = Member.objects.filter(member_id=member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data

            marital_status = request.data.get("status")

            data = {'member':member,'status':marital_status}

            serializer = MemberMaritalStatusSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddRoleMemberShip(APIView):
    '''
        post:
        add member role
    '''
    def post(self,request):

            member_id = request.data.get("member_id")
            queryset = Member.objects.filter(member_id=member_id)
            data = []
            for data in queryset:
                data = data
            serializer = MemberSerializer(data)
            member = serializer.data

            role_id = request.data.get("role_id")
            queryset = Role.objects.filter(id=role_id)
            data = []
            for data in queryset:
                data = data
            serializer = RoleSerializer(data)
            role = serializer.data

            data = {'member':member,'role':role}

            serializer = RoleMemberShipSerializer(data=data)
            if serializer.is_valid():
                created = serializer.save()

                role = Role.objects.get(id=role_id)
                member = Member.objects.get(member_id=member_id)
                user = User.objects.get(id = member.member.id)
                member_id = []
                starter_password = "darkaster4413"
                message = ' you have been admin of the Church MS, use ' + starter_password + ' as your starting password.'

                if (role.site_admin or role.member_admin or role.group_admin or role.event_admin or role.projects_admin or role.finance_admin ):
                    if (not user.has_usable_password()):
                        member_id.append(member.id)
                        receipient = messenger.receipients_phone_numbers(member_id)
                        user.set_password(starter_password)
                        messenger.send_message(receipient,message)
                        user.save()

                else:
                    pass
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
