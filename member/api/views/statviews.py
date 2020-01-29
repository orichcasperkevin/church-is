from rest_framework.views import APIView
from datetime import date

from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member,MemberAge,MemberMaritalStatus

today = date.today()

class NewMembersCount(APIView):
    '''
        get:
        get count of new  members for all months this year till today
    '''

    def get(self, request):
        dict = []
        for month in range(1,today.month + 1):
            count = Member.objects.filter(member__date_joined__month=month, member__date_joined__year=today.year).count()
            count_last_month =  Member.objects.filter(member__date_joined__month=month-1,member__date_joined__year=today.year).count()
            percentage_increase = 0
            try:
                percentage_increase = ((count - count_last_month) / count_last_month) * 100
            except:
                pass
            dict.append({month:count,'percentage_increase':percentage_increase})
        return Response(dict)

class AgeDistribution(APIView):
    '''
        the age distribution of the members in the church
    '''
    def dateRange(self,min,max):
        to_date = str(today.year - min) + "-01-01"
        from_date = str(today.year - max) + "-01-01"
        name = str(min) + "-" + str(max)

        return {"name":name,"from_date":from_date,"to_date":to_date}

    def appendData(self,date_ranges,dict,total):
        for date_range in date_ranges:
            name = str(date_range["name"])
            count = MemberAge.objects.filter(d_o_b__gt=date_range["from_date"],d_o_b__lt=date_range["to_date"]).count()

            percentage = 0
            try:
                percentage = (count / total) * 100
            except:
                pass

            dict.append({name:count,"percentage":percentage})

    def get(self,request):
        dict = []
        members_with_recorded_ages = MemberAge.objects.all().count()
        dict.append({"members_with_recorded_ages":members_with_recorded_ages})

        date_ranges = [self.dateRange(0,14),self.dateRange(15,25),self.dateRange(26,35),self.dateRange(36,60),self.dateRange(61,150)]
        self.appendData(date_ranges,dict,members_with_recorded_ages)

        return Response(dict)

class MaritalStatusDistribution(APIView):
    '''
        get:
        the distribution of marital status in the church
    '''
    def get(self,request):
        dict = []
        recorded_marital_status = MemberMaritalStatus.objects.all().count()
        dict.append({"recorded_marital_status":recorded_marital_status})

        #married
        married_count = MemberMaritalStatus.objects.filter(status="M").count()
        percentage = 0
        try:
            percentage = (married_count / recorded_marital_status) * 100
        except:
            pass
        dict.append({"married_count":married_count,"percentage":percentage})

        #single
        single_count = MemberMaritalStatus.objects.filter(status="S").count()
        percentage = 0
        try:
            percentage = (single_count / recorded_marital_status) * 100
        except:
            pass
        dict.append({"single_count":single_count,"percentage":percentage})

        #Widowed
        widowed_count = MemberMaritalStatus.objects.filter(status="W").count()
        percentage = 0
        try:
            percentage = (widowed_count / recorded_marital_status) * 100
        except:
            pass
        dict.append({"widowed_count":widowed_count,"percentage":percentage})

        #Divorced
        divorced_count = MemberMaritalStatus.objects.filter(status="D").count()
        percentage = 0
        try:
            percentage = (divorced_count / recorded_marital_status) * 100
        except:
            pass
        dict.append({"divorced_count":divorced_count,"percentage":percentage})

        return Response(dict)
