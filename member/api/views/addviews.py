import random
import os
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from member.api.serializers import *
from member.models import Member, Role
from sms.africastalking.at import ChurchSysMessenger

from member.resources.importCSV import CSVLoader
loader = CSVLoader()

STARTER_PASSWORD = "changeMe"

def getSerializerData(queryset,serializer_class):
    data = queryset[0]
    return serializer_class(data).data

class addMember(APIView):
    '''
        add member to church
    '''
    def post(self, request):

        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        middle_name = request.data.get("middle_name")
        username = first_name.lower() + last_name.lower()
        username = username.replace("'", "")
        username = username.replace(".", "")
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
        member = getSerializerData(queryset,UserSerializer)

        data = {'member': member, 'gender': gender,'middle_name':middle_name}
        serializer = CreateMemberSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadCSV(APIView):
    '''
        post:
        upload a csv file, check if the file is of valid type and format
    '''
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      loader.set_base_url(request.get_host())
      file_serializer = CSVFileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()

          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckCSV(APIView):
    '''
        post:
        check that the csv file sent has no
    '''

    def post(self, request):
            loader.set_base_url(request.get_host())
            file_name = request.data.get('file_name')
            column_config = request.data.get('column_config')
            try:
                loader.configure_CSV(file_name,column_config)
                loader.check_CSV(file_name)
                if (loader.errors):
                    errors = loader.errors
                    #get only the first 5 errors
                    return Response(errors[:5])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_201_CREATED)

class ImportDataFromCsv(APIView):
    '''
        post:
        import data from a csv file given the name
    '''

    def post(self, request):
            loader.set_base_url(request.get_host())
            loader.load(request.data.get("file_name"))
            try:
                loader.load(request.data.get("file_name"))
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_201_CREATED)

class AddMemberContact(APIView):
    '''
        post:
        add contact for a member.
    '''

    def post(self, request):

        queryset = Member.objects.filter(member_id=request.data.get("member_id"))
        member = getSerializerData(queryset,MemberSerializer)

        postal = request.data.get("postal_address")
        phone = request.data.get("phone")
        contact = request.data.get("contact")
        email = request.data.get("email")

        data = {'member': member, 'postal': postal, 'phone': phone, 'contact': contact}

        serializer = MemberContactSerializer(data=data)
        if serializer.is_valid():
            created = serializer.save()
            #create email
            if email != None and email != '':
                member = Member.objects.get(member_id=member_id)
                user = User.objects.get(id=member.member.id)
                user.email = email
                user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddMemberD_O_B(APIView):
    '''
        post:
        add date of birth for a member
    '''

    def post(self, request):

        d_o_b = request.data.get("d_o_b")
        member_id = request.data.get("member_id")

        queryset = Member.objects.filter(member_id=member_id)
        member = getSerializerData(queryset,MemberSerializer)

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
        member = getSerializerData(queryset,MemberSerializer)

        town = request.data.get("town")
        road = request.data.get("road")
        street = request.data.get("street")
        village_estate = request.data.get("village/estate")
        description = request.data.get("description")

        data = {'member': member, 'town': town, 'road': road, 'street': street,
                'village_estate': village_estate, 'description': description}

        serializer = MemberResidenceSerializer(data=data,partial=True)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddMemberMaritalStatus(APIView):
    '''
        post:
        add member marital status
    '''
    def post(self, request):

        marital_status = request.data.get("status")
        member_id = request.data.get("member_id")
        queryset = Member.objects.filter(member_id=member_id)
        member = getSerializerData(queryset,MemberSerializer)

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

        serializer = MemberRoleSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
