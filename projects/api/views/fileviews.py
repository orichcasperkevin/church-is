import csv
import datetime

from django.db.models import Sum,Avg
from django.http import HttpResponse

from projects.models import *

def date_format(date_str):
    date = date_str.split("-")
    year = date[0]
    month = date[1]
    day = date[2]

    return {"year":year,"month":month,"day":day}

def get_project_general_stats_as_csv(request,date):
    filename = "projects_overall_stats_for" + date
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    #date = datetime.datetime(date)
    writer = csv.writer(response)
    date = date_format(date)
    writer.writerow(["name","start","stop","stop","description","required"])
    for project in Project.objects.filter(start__year=date["year"]):
        name = project.name
        start = project.start.strftime(" %a %d %b, %Y")
        stop = project.stop.strftime(" %a %d %b, %Y")
        description = project.description
        required = project.required_amount

        writer.writerow([name,start,stop,stop,description,required])
    total_required = Project.objects.filter(start__year=date["year"]).aggregate(Sum('required_amount'))['required_amount__sum'] or 0
    avg_required = Project.objects.filter(start__year=date["year"]).aggregate(Avg('required_amount'))['required_amount__avg'] or 0
    writer.writerow(["","","","","TOTAL",total_required])
    writer.writerow(["","","","","AVERAGE",round(avg_required,2)])

    return response

def get_project_contribution_stats_as_csv(request,project_id):
    project =  Project.objects.get(id=project_id)
    filename = "project_contributions_for" + project.name.strip().replace(" ","")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename'

    writer = csv.writer(response)
    writer.writerow([project.name.upper()])
    writer.writerow(["required amount:" + " " + str(project.required_amount)])
    writer.writerow([])

    writer.writerow(["MEMBERS"])
    writer.writerow(["member","amount","date"])
    for contribution in Contribution.objects.filter(project_id=project.id,member__member__isnull=False):
        member = contribution.member.member.first_name + " " + contribution.member.member.last_name
        amount = contribution.amount
        date = contribution.recorded_at.strftime(" %a %d %b, %Y")

        writer.writerow([member,amount,date])
    total = Contribution.objects.filter(project_id=project.id,member__member__isnull=False).aggregate(Sum('amount'))['amount__sum'] or 0
    average = Contribution.objects.filter(project_id=project.id,member__member__isnull=False).aggregate(Avg('amount'))['amount__avg'] or 0
    writer.writerow(["TOTAL:",total])
    writer.writerow(["AVERAGE:",round(average,2)])

    '''
        non members contributions.
    '''
    writer.writerow([])
    writer.writerow(["NON - MEMBERS"])
    writer.writerow(["name","amount","phone","date"])
    for contribution in Contribution.objects.filter(project_id=project.id,member__member__isnull=True):
        names = contribution.names
        amount = contribution.amount
        phone = contribution.phone
        date = contribution.recorded_at.strftime(" %a %d %b, %Y")

        writer.writerow([names,amount,phone,date])
    total = Contribution.objects.filter(project_id=project.id,member__member__isnull=True).aggregate(Sum('amount'))['amount__sum'] or 0
    average = Contribution.objects.filter(project_id=project.id,member__member__isnull=True).aggregate(Avg('amount'))['amount__avg'] or 0
    writer.writerow(["TOTAL:",total])
    writer.writerow(["AVERAGE:",round(average,2)])

    return response

def get_pledge_payments_as_csv(request,project_id):
        project =  Project.objects.get(id=project_id)
        filename = "project_contributions_for" + project.name.strip().replace(" ","")
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=filename'

        writer = csv.writer(response)
        writer.writerow([project.name.upper()])
        writer.writerow(["required amount:" + " " + str(project.required_amount)])
        writer.writerow([])

        writer.writerow(["MEMBERS"])
        writer.writerow(["member","pledge","settlement","amount_so_far","amount_remaining"])

        for pledge_settlement in PledgePayment.objects.filter(pledge__project_id=project_id,pledge__member__isnull=False):
            member = pledge_settlement.pledge.member.member.first_name + " " + pledge_settlement.pledge.member.member.last_name
            pledge = pledge_settlement.pledge.amount
            settlement = pledge_settlement.payment_amount
            amount_so_far = pledge_settlement.pledge.amount_so_far
            amount_remaining = pledge_settlement.pledge.remaining_amount

            writer.writerow([member,pledge,settlement,amount_so_far,amount_remaining])

        total = PledgePayment.objects.filter(pledge__project_id=project_id,pledge__member__isnull=False).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0
        average = PledgePayment.objects.filter(pledge__project_id=project_id,pledge__member__isnull=False).aggregate(Avg('payment_amount'))['payment_amount__avg'] or 0
        writer.writerow(["","TOTAL",total])
        writer.writerow(["","AVERAGE",round(average,2)])

        '''
         NON MEMBERS
        '''

        writer.writerow([])

        writer.writerow(["NON MEMBERS"])
        writer.writerow(["name","phone","pledge","settlement","amount_so_far","amount_remaining"])

        for pledge_settlement in PledgePayment.objects.filter(pledge__project_id=project_id,pledge__member__isnull=True):
            names = pledge_settlement.pledge.names
            phone = pledge_settlement.pledge.phone
            pledge = pledge_settlement.pledge.amount
            settlement = pledge_settlement.payment_amount
            amount_so_far = pledge_settlement.pledge.amount_so_far
            amount_remaining = pledge_settlement.pledge.remaining_amount

            writer.writerow([names,phone,pledge,settlement,amount_so_far,amount_remaining])

        total = PledgePayment.objects.filter(pledge__project_id=project_id,pledge__member__isnull=True).aggregate(Sum('payment_amount'))['payment_amount__sum'] or 0
        average = PledgePayment.objects.filter(pledge__project_id=project_id,pledge__member__isnull=True).aggregate(Avg('payment_amount'))['payment_amount__avg'] or 0
        writer.writerow(["","TOTAL",total])
        writer.writerow(["","AVERAGE",round(average,2)])

        return response
