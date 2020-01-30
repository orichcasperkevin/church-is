from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date

from events.models import Event,GroupAttendingEvent,MemberThatAttendedEvent
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

class EventsCount(APIView):
    '''
        get:
        stats for event count
    '''
    def get(self,request):
        dict = []

        for month in range(1,today.month + 1):
            count = Event.objects.filter(start_datetime__month=month).count() or 0
            count_last_month = Event.objects.filter(start_datetime__month=month-1).count() or 0
            percentage_increase = getPercentageIncrease(count,count_last_month)

            dict.append({month:count,'percentage_increase':percentage_increase})

            return Response(dict)
class EventAttendance(APIView):
    '''
    get:
    stats for event attendance
    '''
    def get(self,request):
        dict = []
        # expected to attend.
        for month in range(1,today.month + 1):
            total_expected_to_attend = 0
            groups = GroupAttendingEvent.objects.filter(event__start_datetime__month=month)\
                                                .order_by('event').distinct('event')
            for group in groups:
                total_expected_to_attend += group.group.number_of_members

            #member that  attended events.
            attendee_members_count = MemberThatAttendedEvent.objects.filter(event__start_datetime__month=month).count() or 0
            percentage_attendance = getPercentageToTotal(attendee_members_count,total_expected_to_attend )

            dict.append({"month":month,"expected":total_expected_to_attend,"attended":attendee_members_count,
                            "percentage_attendance":percentage_attendance})

            return Response(dict)
