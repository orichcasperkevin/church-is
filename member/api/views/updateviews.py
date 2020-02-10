from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from member.models import *

def updateModelField(model_object,field,data):
    if data:
        #get model object field.
        attr = getattr(model_object,field)
        #change it to something else.
        setattr(model_object,field,data)
        #save.
        model_object.save()
    else:
        pass


class UpdateMemberData(APIView):
    '''
        patch:
        update user data, firstname lastname and middle name, gender etc
    '''
    def patch(self, request):
        member_id = request.data.get("member_id")

        try:
            user = User.objects.get(id=member_id)
            member  = Member.objects.get(member__id=member_id)
            member_marital_status = MemberContact.objects.get_or_create(member__member__id=member_id)
            member_age = MemberAge.objects.get_or_create(member__member__id=member_id)

            updateModelField(user,'first_name',request.data.get("first_name"))
            updateModelField(user,'last_name',request.data.get("last_name"))

            updateModelField(member,'middle_name',request.data.get("middle_name"))
            updateModelField(member,'gender',request.data.get("gender"))

            updateModelField(member_age,'d_o_b',request.data.get("d_o_b"))
            updateModelField(member_marital_status,'status',request.data.get("marital_status"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateMemberContact(APIView):
    '''
        patch:
        update user contact data.
    '''
    def patch(self, request):
        member_id = request.data.get("member_id")

        try:
            user = User.objects.get(id=member_id)
            member_contact = MemberContact.objects.get_or_create(member__member__id=member_id)

            updateModelField(user,'email',request.data.get("email"))

            updateModelField(member_contact,'phone',request.data.get("phone"))
            updateModelField(member_contact,'phone2',request.data.get("phone2"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateMemberResidence(APIView):
    '''
        patch:
        update user residence data.
    '''
    def patch(self, request):
        member_id = request.data.get("member_id")

        try:
            member_residence = MemberResidence.objects.get_or_create(member__member__id=member_id)

            updateModelField(member_residence,'town',request.data.get("town"))
            updateModelField(member_residence,'road',request.data.get("road"))
            updateModelField(member_residence,'street',request.data.get("street"))
            updateModelField(member_residence,'description',request.data.get("description"))

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
