from datetime import date
from django.db.models import Sum,Avg

from rest_framework.views import APIView
from rest_framework.response import Response

from projects.models import *
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

class ProjectSizeStats(APIView):
    def get(self,request):
        dict = []
        projects_count = Project.objects.filter(start__year=today.year).count() or 0
        total_project_size = Project.objects.filter(start__year=today.year).aggregate(Sum('required_amount'))['required_amount__sum']
        for project in Project.objects.filter(start__year=today.year):
            size = project.required_amount
            percentage_to_total = getPercentageToTotal(size,total_project_size)
            project_tuple = {"project":str(project),"size":size,"percentage_to_total":percentage_to_total}
            dict.append(project_tuple)
        return Response(dict)

class ProjectFinancingStats(APIView):
    def get(self,request):
        dict = []
        for year in range(today.year,today.year + 1):
            projects_count = Project.objects.filter(start__year=year).count() or 0
            avg_size_this_year = Project.objects.filter(start__year=year).aggregate(Avg('required_amount'))['required_amount__avg'] or 0
            avg_size_last_year = Project.objects.filter(start__year=year-1).aggregate(Avg('required_amount'))['required_amount__avg'] or 0
            percentage_increase = getPercentageIncrease(avg_size_this_year,avg_size_last_year)

            avg_percentage_funded = 0
            year_tuple = {"year":year, "projects_count":projects_count,"avg_size_this_year":avg_size_this_year,"percentage_increase":percentage_increase,"months":[]}

            for month in range(1,13):
                projects_running = Project.objects.filter(start__year=year).count() or 0
                contribution_this_month = Contribution.objects.filter(recorded_at__month=month,recorded_at__year=year).aggregate(Sum('amount'))['amount__sum'] or 0
                contribution_last_month = Contribution.objects.filter(recorded_at__month=month-1,recorded_at__year=year).aggregate(Sum('amount'))['amount__sum'] or 0
                contribution_percentage_increase = getPercentageIncrease(contribution_this_month,contribution_last_month)

                settled_pledges_this_month = PledgePayment.objects.filter(payment_recorded_on__month=month,payment_recorded_on__year=year).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0
                settled_pledges_last_month = PledgePayment.objects.filter(payment_recorded_on__month=month-1,payment_recorded_on__year=year).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0
                settled_pledges_percentage_increase = getPercentageIncrease(settled_pledges_this_month,settled_pledges_last_month)
                raised_amount = 0
                raised_amount_last_month = 0

                for project in Project.objects.filter(start__year=year):
                    pledge_payment = PledgePayment.objects.filter(payment_recorded_on__month=month,payment_recorded_on__year=year,pledge__project__id=project.id).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0
                    contributions = Contribution.objects.filter(recorded_at__month=month,recorded_at__year=year,project_id=project.id).aggregate(Sum('amount'))['amount__sum'] or 0
                    raised_amount = pledge_payment + contributions

                    pledge_payment_last_month = PledgePayment.objects.filter(payment_recorded_on__month=month-1,payment_recorded_on__year=year,pledge__project__id=project.id).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0
                    contributions_last_month = Contribution.objects.filter(recorded_at__month=month-1,recorded_at__year=year,project_id=project.id).aggregate(Sum('amount'))['amount__sum'] or 0
                    raised_amount_last_month = pledge_payment + contributions

                required_amount = Project.objects.filter(start__year=year).aggregate(Sum('required_amount'))['required_amount__sum']
                percentage_funded = getPercentageToTotal(raised_amount,required_amount)
                funding_percentage_increase = getPercentageIncrease(raised_amount,raised_amount_last_month)

                data = {"month":month,"projects_running":projects_running,"contribution_this_month":contribution_this_month,
                        "contribution_percentage_increase":contribution_percentage_increase,"settled_pledges_this_month":settled_pledges_percentage_increase,
                        "percentage_funded":percentage_funded,"funding_percentage_increase":funding_percentage_increase}
                year_tuple["months"].append(data)
            dict.append(year_tuple)
        return Response(dict)
