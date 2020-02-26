from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from Clients.api.serializers import *
from Clients.models import *


class GetClient(APIView):
    '''
    get:
    get client using the name
    '''

    def get(self, request, id):
        client = Client.objects.filter(id=id)
        data = ClientSerializer(client, many=True).data
        return Response(data)

class GetClientDetail(APIView):
    def get(self, request, id):
        client_detail = ClientDetail.objects.filter(client_id=id)
        data = ClientDetailSerializer(client_detail,many=True).data
        return Response(data)

class GetChurchLogo(APIView):
    def get(self,request,id):
        church_logo = ChurchLogo.objects.filter(church_id=id)
        data = ChurchLogoSerializer(church_logo,many=True).data
        return Response(data)

class GetChurchStatements(APIView):
    def get(self,request,id):
        statements = ChurchStatement.objects.filter(church_id=id)
        data = ChurchStatementSerializer(statements,many=True).data
        return Response(data)

class GetChurchCoreValues(APIView):
    def get(self,request,id):
        value = ChurchCoreValue.objects.filter(church_id=id)
        data = ChurchCoreValueSerializer(value,many=True).data
        return Response(data)

class GetChurchPeriodicTheme(APIView):
    def get(self,request,id):
        themes = ChurchLogo.objects.filter(church_id=id)[:10]
        data = ChurchPeriodicThemeSerializer(themes,many=True).data
        return Response(data)
