from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from services.api.serializers import *

from services.models import *

today = date.today()
day = today.day
month = today.month
year = today.year

class ServiceOnDateOfType(APIView):
    '''
        get:
        get a service of a particular type on a particular date
    '''

    def get(self, request, type_id, date):

        service = Service.objects.filter(date=date, type_id=type_id)
        data = ServiceSerializer(service, many=True).data
        return Response(data)

class ServiceItemsForService(APIView):
    '''
        get:
        get service items for a particular service
    '''

    def get(self, request, service_id):
        item = ServiceItem.objects.filter( service_id=service_id)
        data = ServiceItemSerializer(item, many=True).data
        return Response(data)

class GetBookingsForService(APIView):
    '''
        get:
        get bookings for a service
    '''

    def get(self, request, service_id):
        booking = Booking.objects.filter(service_id=service_id)
        data = BookingSerializer(booking, many=True).data
        return Response(data)

class GetBookingForMember(APIView):
    '''
        get:
        get booking for member.
    '''

    def get(self, request, phone_number):
        booking = Booking.objects.filter(phone_number=phone_number)[:100]
        data = BookingSerializer(booking, many=True).data
        return Response(data)
