from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from services.api.serializers import *

from services.models import *

class AddService(APIView):
    '''
        add a service
    '''

    def post(self, request):

        service_type_id = request.data.get("service_type_id")
        queryset = ServiceType.objects.filter(id=service_type_id)
        data = []
        for data in queryset:
            data = data
        serializer = ServiceTypeSerializer(data)
        type = serializer.data

        venue = request.data.get("venue")
        date = request.data.get("date")
        start = request.data.get("start")
        end = request.data.get("end")

        data = {'type': type, 'venue': venue, 'date': date, 'start': start, 'end': end }
        serializer = AddServiceSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddServiceItem(APIView):
    '''
        add a service item
    '''

    def post(self, request):

        service_id = request.data.get("service_id")
        queryset = Service.objects.filter(id=service_id)
        data = []
        for data in queryset:
            data = data
        serializer = ServiceSerializer(data)
        service = serializer.data

        action = request.data.get("action")
        value = request.data.get("value")

        data = {'service': service, 'action': action, 'value': value }
        serializer = ServiceItemSerializer(data=data)

        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddBooking(APIView):
    '''
        add booking
    '''

    def post(self, request):
        data = request.data
        serializer = BookingSerializer(data=data,partial=True)
        if serializer.is_valid():
            created = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
