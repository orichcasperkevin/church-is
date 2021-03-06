from datetime import datetime
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from finance.api.serializers import *
from finance.models import *

class PendingConfirmations(generics.ListCreateAPIView):
    queryset = PendingConfirmation.objects.all()
    serializer_class = PendingConfirmationSerializer

class ModesOfPayment(generics.ListCreateAPIView):
    '''
        a list of all modes of payment
    '''
    queryset = ModeOfPayment.objects.all()
    serializer_class = ModeOfPaymentSerializer

class OfferingType(generics.ListCreateAPIView) :
    '''
        a list of all offering types.
    '''
    #TODO name__icontains rose was a quick fix ...add endpoint for deleting offering type
    queryset = OfferingType.objects.all().exclude(name__icontains="rose").order_by('id')
    serializer_class = OfferingTypeSerializer

class IncomeTypeList(generics.ListCreateAPIView):
    '''
        a list of all income types
    '''
    queryset = IncomeType.objects.all().order_by('-id')
    serializer_class = IncomeTypeSerializer


class IncomeStats(APIView):
    '''
        statistics for all other types of income
    '''

    def get(self, response):
        total_this_month = 0.00
        total_this_year = 0.00

        stat_dict = {"total_this_month": None, "total_this_year": None}

        for data in Income.objects.filter(date__month=month):
            total_this_month = total_this_month + float(data.amount)

        for data in Income.objects.filter(date__year=year):
            total_this_year = total_this_year + float(data.amount)

        stat_dict["total_this_month"] = total_this_month
        stat_dict["total_this_year"] = total_this_year

        return Response(stat_dict)

class IncomeTypeOfID(APIView):
    '''
        income type with id <id>
    '''

    def get(self, request, id):
        income_type = IncomeType.objects.filter(id=id)
        data = IncomeTypeSerializer(income_type, many=True).data
        return Response(data)

class IncomeOfType(APIView):
    '''
        income of type with id <id>
    '''

    def get(self, request, id):
        income = Income.objects.filter(type_id=id)
        data = IncomeSerializer(income, many=True).data
        return Response(data)


class ExpenditureTypeList(generics.ListCreateAPIView):
    '''
        get:
        a list of all expenditure types
    '''
    queryset = ExpenditureType.objects.all().order_by('-id')
    serializer_class = ExpenditureTypeSerializer

class ExpenditureTypeOfID(APIView):
    '''
        expenditure type with id <id>
    '''

    def get(self, request, id):
        income_type = ExpenditureType.objects.filter(id=id)
        data = ExpenditureTypeSerializer(income_type, many=True).data
        return Response(data)

class ExpenditureOfType(APIView):
    '''
        get:
        expenditure of type with id <id>
    '''

    def get(self, request, id):
        expenditure = Expenditure.objects.filter(type_id=id)
        data = ExpenditureSerializer(expenditure, many=True).data
        return Response(data)

class ExpenditureStats(APIView):
    '''
        statistics for expenditures
    '''

    def get(self, response):
        total_this_month = 0.00
        total_this_year = 0.00

        stat_dict = {"total_this_month": None, "total_this_year": None}

        for data in Expenditure.objects.filter(date__month=month):
            total_this_month = total_this_month + float(data.amount)

        for data in Expenditure.objects.filter(date__year=year):
            total_this_year = total_this_year + float(data.amount)

        stat_dict["total_this_month"] = total_this_month
        stat_dict["total_this_year"] = total_this_year

        return Response(stat_dict)

class TitheForMember(APIView):
    '''
        tithes as given by member with id <id>
    '''

    def get(self, request, id):
        tithe = Tithe.objects.filter(member__member_id=id)[:50]
        data = TitheSerializer(tithe, many=True).data
        return Response(data)


class TitheStatsForMember(APIView):
    '''
        Tithe statistics for a member
    '''

    def get(self, request, id):
        tithe = Tithe.objects.filter(member__member_id=id)[:1]
        data = TitheSerializer(tithe, many=True).data
        return Response(data)


class TithesAndOfferings(APIView):
    '''
        get both tithes and offerings
    '''
    def get(self, request):
        params = dict(request.GET)
        if not len(params):
            #tithes
            tithe = Tithe.objects.all().order_by('-date')[:50]
            data = TitheSerializer(tithe, many=True).data
            #offerings
            offering = Offering.objects.all().order_by('-timestamp')[:50]
            data += OfferingSerializer(offering, many=True).data

            data.sort(reverse=True,key = lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
            return Response(data)
        else:
            # tithes
            tithe = Tithe.objects.filter(date__gte=params['from_date'][0],
                                        date__lte=params['to_date'][0])\
                                .order_by('-date')
            data = TitheSerializer(tithe, many=True).data
            #offerings
            offerings = Offering.objects.filter(date__gte=params['from_date'][0],
                                        date__lte=params['to_date'][0])\
                                .order_by('-date')
            data += OfferingSerializer(offerings, many=True).data
            data.sort(reverse=True,key = lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
            return Response(data)

class Tithes(APIView):
    '''
        tithes as given by members
    '''

    def get(self, request):
        params = dict(request.GET)
        if not len(params):
            tithe = Tithe.objects.all().order_by('-date')[:50]
            data = TitheSerializer(tithe, many=True).data
            return Response(data)
        else:
            tithe = Tithe.objects.filter(date__gte=params['from_date'][0],
                                        date__lte=params['to_date'][0])\
                                .order_by('-date')
            data = TitheSerializer(tithe, many=True).data
            return Response(data)



class TitheStats(APIView):
    '''
        statistics for tithes this month and this year
    '''

    def get(self, request):
        total_in_tithe_this_month = 0.00
        total_in_tithe_this_year = 0.00

        stat_dict = {"total_in_tithe_this_month": None, "total_in_tithe_this_year": None}

        for data in Tithe.objects.filter(date__month=month):
            total_in_tithe_this_month = total_in_tithe_this_month + float(data.amount)

        for data in Tithe.objects.filter(date__year=year):
            total_in_tithe_this_year = total_in_tithe_this_year + float(data.amount)

        stat_dict["total_in_tithe_this_month"] = total_in_tithe_this_month
        stat_dict["total_in_tithe_this_year"] = total_in_tithe_this_year

        return Response(stat_dict)

class OfferingByMember(APIView):
    '''
        offerings as given by member with id <id>
    '''

    def get(self, request, id):
        offering = Offering.objects.filter(member__member_id=id).order_by('-date')
        data = OfferingSerializer(offering, many=True).data
        return Response(data)

class OfferingStatsForMember(APIView):
    '''
        offerings stats for member with id <id>
    '''

    def get(self, request, id):
        offering = Offering.objects.filter(member__member_id=id)[:1]
        data = OfferingSerializer(offering, many=True).data
        return Response(data)

class OfferingThisMonth(APIView):
    '''
        offerings this month
    '''
    def get(self, request):
        params = dict(request.GET)
        if not len(params):
            offering = Offering.objects.all().order_by('-timestamp')[:50]
            data = OfferingSerializer(offering, many=True).data
            return Response(data)
        else:
            offerings = Offering.objects.filter(date__gte=params['from_date'][0],
                                        date__lte=params['to_date'][0])\
                                .order_by('-date')
            data = OfferingSerializer(offerings, many=True).data
            return Response(data)


class OfferingStats(APIView):
    '''
        statistics for offerings this month.
    '''

    def get(self, request, type_id):
        total_in_offerings_this_month = 0.00
        total_in_offerings_this_year = 0.00

        stat_dict = {"total_in_offerings_this_month": None, "total_in_offerings_this_year": None}

        for data in Offering.objects.filter(type_id=type_id,date__month=month,date__year=year):
            total_in_offerings_this_month = total_in_offerings_this_month + float(data.amount)

        for data in Offering.objects.filter(type_id=type_id,date__year=year):
            total_in_offerings_this_year = total_in_offerings_this_year + float(data.amount)

        stat_dict["total_in_offerings_this_month"] = total_in_offerings_this_month
        stat_dict["total_in_offerings_this_year"] = total_in_offerings_this_year

        return Response(stat_dict)
