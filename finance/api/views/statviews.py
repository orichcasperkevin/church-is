from django.db.models import Sum,Avg

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date

from finance.models import Offering,OfferingType

today = date.today()
def getPercentageIncrease(current,previous):
    percentage_increase =0
    try:
        percentage_increase = ((current - previous) / previous) * 100
    except:
        pass
    return percentage_increase

class OfferingFromMembers(APIView):
    '''
        get:
        stats for offerings rom members.
    '''
    def get(self,request):
        dict = []

        for month in range(1,today.month + 1):
            total_by_members = Offering.objects.filter(member__isnull=False,date__month=month).aggregate(Sum('amount'))['amount__sum']
            total_by_members_last_month = Offering.objects.filter(member__isnull=False,date__month=month-1).aggregate(Sum('amount'))['amount__sum']
            avg_per_member = Offering.objects.filter(member__isnull=False,date__month=month).aggregate(Avg('amount'))['amount__avg']

            percentage_increase = getPercentageIncrease(total_by_members,total_by_members_last_month)

            dict.append({"month":month,"total_by_members":total_by_members,"avg_per_member":avg_per_member,"percentage_increase":percentage_increase})

        return Response(dict)

class OfferingByType(APIView):
    def get(self,request):
        dict = []
        for month in range(1,today.month + 1):
            total_offering = Offering.objects.filter(member__isnull=False,date__month=month).aggregate(Sum('amount'))['amount__sum']
            total_offering_last_month = Offering.objects.filter(member__isnull=False,date__month=month-1).aggregate(Sum('amount'))['amount__sum']
            percentage_increase = getPercentageIncrease(total_offering,total_offering_last_month)

            month_tuple = {"month":month,"total":total_offering,"percentage_increase":percentage_increase,"stats":[]}

            for type in OfferingType.objects.all():
                total = Offering.objects.filter(member__isnull=False,date__month=month,type_id=type.id).aggregate(Sum('amount'))['amount__sum']
                percentage_of_type_to_total = (total/total_offering)*100
                month_tuple["stats"].append({"type":str(type),"total":total,"percentage":percentage_of_type_to_total})
            dict.append(month_tuple)

        return Response(dict)
