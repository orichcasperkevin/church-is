from django.db.models import Sum,Avg

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date

from finance.models import *
from services.models import ServiceType

today = date.today()
def getPercentageIncrease(current,previous):
    percentage_increase =0
    try:
        percentage_increase = ((current - previous) / previous) * 100
    except:
        pass
    return percentage_increase

def getPercentageToTotal(figure,total):
    percentage = 0
    try:
        percentage = (figure/total)*100
    except:
        pass
    return percentage

class OfferingFromMembers(APIView):
    '''
        get:
        stats for offerings rom members.
    '''
    def get(self,request):
        dict = []

        for month in range(1,today.month + 1):
            total_by_members = Offering.objects.filter(member__isnull=False,date__month=month,date__year=today.year).aggregate(Sum('amount'))['amount__sum']
            total_by_members_last_month = Offering.objects.filter(member__isnull=False,date__month=month-1,date__year=today.year).aggregate(Sum('amount'))['amount__sum']
            avg_per_member = Offering.objects.filter(member__isnull=False,date__month=month).aggregate(Avg('amount'))['amount__avg']

            percentage_increase = getPercentageIncrease(total_by_members,total_by_members_last_month)

            dict.append({"month":month,"total_by_members":total_by_members,"avg_per_member":avg_per_member,"percentage_increase":percentage_increase})

        return Response(dict)

class OfferingFromService(APIView):
    def get(self,request):
        dict = []
        for month in range(1,today.month + 1):
            total_from_services = Offering.objects.filter(service__isnull=False,date__month=month,date__year=today.year).aggregate(Sum('amount'))['amount__sum'] or 0
            total_from_services_last_month = Offering.objects.filter(service__isnull=False,date__month=month-1,date__year=today.year).aggregate(Sum('amount'))['amount__sum'] or 0
            percentage_increase = getPercentageIncrease(total_from_services ,total_from_services_last_month )

            month_tuple = {"month":month,"total":total_from_services ,"percentage_increase":percentage_increase,"stats":[]}

            for type in ServiceType.objects.all():
                total_from_type =  Offering.objects.filter(service__type_id=type.id,service__isnull=False,date__month=month,date__year=today.year).aggregate(Sum('amount'))['amount__sum'] or 0
                avg_from_type =  Offering.objects.filter(service__type_id=type.id,service__isnull=False,date__month=month,date__year=today.year).aggregate(Avg('amount'))['amount__avg'] or 0
                total_from_type_last_month =  Offering.objects.filter(service__type_id=type.id,service__isnull=False,date__month=month-1,date__year=today.year).aggregate(Sum('amount'))['amount__sum'] or 0
                percentage_increase = getPercentageIncrease(total_from_type,total_from_type_last_month)
                percentage_to_total = getPercentageToTotal(total_from_type,total_from_services)

                month_tuple["stats"].append({"type":str(type),"total":total_from_type,"avg_per_service":avg_from_type,"percentage_increase":percentage_increase,"percentage_to_total":percentage_to_total})
            dict.append(month_tuple)
        return Response(dict)


class OfferingByType(APIView):
    def get(self,request):
        dict = []
        for month in range(1,today.month + 1):
            total_offering = Offering.objects.filter(member__isnull=False,date__month=month,date__year=today.year).aggregate(Sum('amount'))['amount__sum'] or 0
            total_offering_last_month = Offering.objects.filter(member__isnull=False,date__month=month-1,date__year=today.year).aggregate(Sum('amount'))['amount__sum'] or 0
            percentage_increase = getPercentageIncrease(total_offering,total_offering_last_month)

            month_tuple = {"month":month,"total":total_offering,"percentage_increase":percentage_increase,"stats":[]}

            for type in OfferingType.objects.all():
                total = Offering.objects.filter(member__isnull=False,date__month=month,date__year=today.year,type_id=type.id).aggregate(Sum('amount'))['amount__sum'] or 0
                total_last_month = Offering.objects.filter(member__isnull=False,date__month=month-1,date__year=today.year,type_id=type.id).aggregate(Sum('amount'))['amount__sum'] or 0
                avg_per_member = Offering.objects.filter(member__isnull=False,date__month=month,date__year=today.year,type_id=type.id).aggregate(Avg('amount'))['amount__avg'] or 0
                percentage_of_type_to_total = getPercentageToTotal(total,total_offering)
                percentage_increase = getPercentageIncrease(total,total_last_month)

                month_tuple["stats"].append({"type":str(type),"total":total,"percentage_to_total":percentage_of_type_to_total,"percentage_increase":percentage_increase,"avg_per_member":avg_per_member})
            dict.append(month_tuple)

        return Response(dict)

class TitheStats(APIView):
    def get(self,request):
        dict = []
        for month in range(1,today.month + 1):
            total_this_month = Tithe.objects.filter(date__month=month).aggregate(Sum('amount'))['amount__sum']  or 0
            total_last_month = Tithe.objects.filter(date__month=month-1).aggregate(Sum('amount'))['amount__sum']  or 0
            avg_per_member = Tithe.objects.filter(member__isnull=False,date__month=month).aggregate(Avg('amount'))['amount__avg']  or 0
            percentage_increase = getPercentageIncrease(total_this_month,total_last_month)

            dict.append({"month":month,"total_this_month":total_this_month,"avg_per_member":avg_per_member,"percentage_increase":percentage_increase})

        return Response(dict)

class IncomeStats(APIView):
    def get(self,request):
        dict = []
        for month in range(1,today.month + 1):
            total_this_month = Income.objects.filter(date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0
            total_last_month = Income.objects.filter(date__month=month-1).aggregate(Sum('amount'))['amount__sum'] or 0
            percentage_increase = getPercentageIncrease(total_this_month,total_last_month)

            month_tuple = {"month":month,"total_this_month":total_this_month,"percentage_increase":percentage_increase,"stats":[]}

            for type in IncomeType.objects.all():
                total_for_type = Income.objects.filter(date__month=month,type_id=type.id).aggregate(Sum('amount'))['amount__sum'] or 0
                total_for_type_last_month = Income.objects.filter(date__month=month-1,type_id=type.id).aggregate(Sum('amount'))['amount__sum'] or 0
                percentage_to_total = getPercentageToTotal(total_for_type,total_this_month)
                percentage_increase = getPercentageIncrease(total_for_type,total_for_type_last_month)

                month_tuple['stats'].append({"type":str(type),"total_for_type":total_for_type,"percentage_to_total":percentage_to_total,"percentage_increase":percentage_increase})
            dict.append(month_tuple)

        return Response(dict)

class ExpenditureStats(APIView):
    def get(self,request):
        dict = []
        for month in range(1,today.month + 1):
            total_this_month = Expenditure.objects.filter(date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0
            total_last_month = Expenditure.objects.filter(date__month=month-1).aggregate(Sum('amount'))['amount__sum'] or 0
            percentage_increase = getPercentageIncrease(total_this_month,total_last_month)

            month_tuple = {"month":month,"total_this_month":total_this_month,"percentage_increase":percentage_increase,"stats":[]}

            for type in ExpenditureType.objects.all():
                total_for_type = Expenditure.objects.filter(date__month=month,type_id=type.id).aggregate(Sum('amount'))['amount__sum'] or 0
                total_for_type_last_month = Expenditure.objects.filter(date__month=month-1,type_id=type.id).aggregate(Sum('amount'))['amount__sum'] or 0
                percentage_to_total = getPercentageToTotal(total_for_type,total_this_month)
                percentage_increase = getPercentageIncrease(total_for_type,total_for_type_last_month)

                month_tuple['stats'].append({"type":str(type),"total_for_type":total_for_type,"percentage_to_total":percentage_to_total,"percentage_increase":percentage_increase})
            dict.append(month_tuple)

        return Response(dict)
