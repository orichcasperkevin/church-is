import random

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser


from member.api.serializers import (UserSerializer, MemberSerializer, CreateMemberSerializer,
                                    MemberContactSerializer, MemberAgeSerializer, RoleMemberShipSerializer,
                                    MemberResidenceSerializer,
                                    RoleSerializer, MemberMaritalStatusSerializer,CSVFileSerializer)

from member.models import (Member, Role,)
from sms.africastalking.at import ChurchSysMessenger

messenger = ChurchSysMessenger("create member", "test member 2")


class addMember(APIView):
    '''

    '''

    def post(self, request):

        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        username = '@' + first_name.lower() + last_name.lower()
        email = request.data.get("email")
        gender = request.data.get("gender")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(first_name=first_name, username=username, last_name=last_name, email=email)
            user.save()
            user.set_unusable_password()
            user_id = user.id
        else:
            username = username + str(random.choice(range(100)))
            user = User(first_name=first_name, username=username, last_name=last_name, email=email)
            user.save()
            user.set_unusable_password()
            user_id = user.id

        queryset = User.objects.filter(id=user_id)
        member = []
        for member in queryset:
            member = member
        serializer = UserSerializer(member)
        member = serializer.data

        data = {'member': member, 'gender': gender}
        serializer = CreateMemberSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadCSV(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
      file_serializer = CSVFileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddMemberContact(APIView):
    '''
        post:
        add contact for a member.
    '''

    def post(self, request):

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
        email = request.data.get("email")

        data = {'member': member, 'postal': postal, 'phone': phone, 'contact': contact}

        serializer = MemberContactSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()

            member = Member.objects.get(member_id=member_id)
            user = User.objects.get(id=member.member.id)
            user.email = email
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddMemberD_O_B(APIView):
    '''
        post:
        add date of birth for a member
    '''

    def post(self, request):

        member_id = request.data.get("member_id")
        queryset = Member.objects.filter(member_id=member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        member = serializer.data

        d_o_b = request.data.get("d_o_b")

        data = {'member': member, 'd_o_b': d_o_b}

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

    def post(self, request):

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

        data = {'member': member, 'town': town, 'road': road, 'street': street,
                'village_estate': village_estate, 'description': description}

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

    def post(self, request):

        member_id = request.data.get("member_id")
        queryset = Member.objects.filter(member_id=member_id)
        data = []
        for data in queryset:
            data = data
        serializer = MemberSerializer(data)
        member = serializer.data

        marital_status = request.data.get("status")

        data = {'member': member, 'status': marital_status}

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

    def post(self, request):

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

        data = {'member': member, 'role': role}

        serializer = RoleMemberShipSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()

            role = Role.objects.get(id=role_id)
            member = Member.objects.get(member_id=member_id)
            user = User.objects.get(id=member.member.id)
            member_id = []
            starter_password = "nano-initial"
            message = 'You have been made admin of the Church MS, use ' + starter_password + ' as your starting password and '+  user.username + ' as your username'

            if (role.site_admin
                or role.member_admin
                or role.group_admin
                or role.event_admin
                or role.projects_admin
                or role.finance_admin):
                if (not user.check_password(user.password)):
                    member_id.append(member.id)
                    receipient = messenger.receipients_phone_numbers(member_id)
                    user.set_password(starter_password)
                    messenger.send_message(receipient, message)
                    user.save()

                else:
                    pass
            else:
                pass
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
