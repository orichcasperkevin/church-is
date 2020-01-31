from datetime import date
from django.db.models import Sum,Avg

from rest_framework.views import APIView
from rest_framework.response import Response

from groups.models import *
from events.models import *

today = date.today()
#helpers
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

class MemberCountStats(APIView):
    def get(self,request):
        dict = []
        number_of_groups = ChurchGroup.objects.all().count()
        total_new_members_count = ChurchGroupMembership.objects.filter(date_joined__month__gt=today.month-3,date_joined__year=today.year).count()
        total_members_in_groups = ChurchGroupMembership.objects.all().count()
        dict.append({"number_of_groups":number_of_groups,"total_members_in_groups":total_members_in_groups,
                     "total_new_members_count":total_new_members_count,"stats":[]})
        for group in ChurchGroup.objects.all():
            members_count = group.number_of_members
            new_members_count = ChurchGroupMembership.objects.filter(church_group_id=group.id,date_joined__month__gt=today.month-3,date_joined__year=today.year).count()
            percentage_to_total = getPercentageToTotal(members_count,total_members_in_groups)

            group_tuple = {"group":str(group),"members_count":members_count,"percentage_to_total":percentage_to_total,
                            "new_members_count":new_members_count}
            dict[0]["stats"].append(group_tuple)
        return Response(dict)
class EventAttendanceStats(APIView):
    def get(self,request):
        dict = []
        for month in range(1,today.month + 1):
            total_attendance_this_month = MemberThatAttendedEvent.objects.filter(event__start_datetime__month=month).count()
            total_attendance_last_month = MemberThatAttendedEvent.objects.filter(event__start_datetime__month=month-1).count()
            percentage_increase = getPercentageIncrease(total_attendance_this_month,total_attendance_last_month)

            month_tuple = {"month":month,"total_attendance_this_month":total_attendance_this_month,"percentage_increase":percentage_increase}
            dict.append(month_tuple)
        return Response(dict)
