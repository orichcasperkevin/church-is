from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from Clients.api.serializers import ClientSerializer,ClientDetailSerializer
from Clients.models import Client,ClientDetail


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
